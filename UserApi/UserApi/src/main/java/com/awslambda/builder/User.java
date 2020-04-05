package com.awslambda.builder;

import com.amazonaws.services.dynamodbv2.AmazonDynamoDB;
import com.amazonaws.services.dynamodbv2.AmazonDynamoDBClientBuilder;
import com.amazonaws.services.dynamodbv2.datamodeling.DynamoDBMapper;
import com.amazonaws.services.dynamodbv2.datamodeling.DynamoDBQueryExpression;
import com.amazonaws.services.dynamodbv2.model.AttributeValue;
import com.amazonaws.services.dynamodbv2.model.ComparisonOperator;
import com.amazonaws.services.dynamodbv2.model.Condition;
import com.awslambda.dao.ddb.UserItem;
import org.json.simple.JSONObject;
import org.json.simple.JSONArray;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class User {

    static DynamoDBMapper mapper;
    static {
        AmazonDynamoDB client = AmazonDynamoDBClientBuilder.standard().build();
        mapper = new DynamoDBMapper(client);
    }

    public Boolean createUser(String firstname, String lastname){
        try {

            String userId = String.valueOf(System.currentTimeMillis());
            UserItem.Name name = new UserItem.Name();
            name.setFirstname(firstname);
            name.setLastname(lastname);

            UserItem userItem_v0 = new UserItem();
            userItem_v0.setUserId(userId);
            userItem_v0.setVersion(0);
            userItem_v0.setName(name);
            userItem_v0.setCurrentVersion(1);

            UserItem userItem_v1 = new UserItem();
            userItem_v1.setUserId(userId);
            userItem_v1.setName(name);
            userItem_v1.setVersion(1);

            mapper.save(userItem_v0);
            mapper.save(userItem_v1);


        }
        catch(Exception ex){
            ex.printStackTrace();
            return false;

        }
        return true;
    }

    public UserItem getUser(String userId){
        try {
            return mapper.load(UserItem.class, userId, 0);
        }
        catch(Exception ex){
            ex.printStackTrace();
            return null;
        }
    }

    public List<UserItem> getuserHistory(String userId, Integer limit){
        try {
            Map<String, AttributeValue> eav = new HashMap<>();

            UserItem userItem = new UserItem();
            userItem.setUserId(userId);
            DynamoDBQueryExpression<UserItem> queryExpression = new DynamoDBQueryExpression<UserItem>()
                    .withHashKeyValues(userItem);

            if(limit != -1){
                Condition rangeKeyCondition = new Condition()
                        .withComparisonOperator(ComparisonOperator.LE.toString())
                        .withAttributeValueList(new AttributeValue().withN(limit.toString()));
                System.out.println("Condition str ... "+ rangeKeyCondition);
                queryExpression.withRangeKeyCondition("version", rangeKeyCondition);
            }

            List<UserItem> userHistoryList = mapper.query(UserItem.class, queryExpression);
            return userHistoryList;
        }
        catch(Exception ex){
            ex.printStackTrace();
            return null;
        }
    }

    public boolean updateUser(String userId, Map<Object,Object> updatedValues){
        try {
            UserItem.Name name = new UserItem.Name();
            name.setFirstname((String)updatedValues.get("firstname"));
            name.setLastname((String)updatedValues.get("lastname"));


            UserItem userItem_v0 = this.getUser(userId);
            userItem_v0.setCurrentVersion(userItem_v0.getCurrentVersion()+1);
            userItem_v0.setName(name);


            UserItem currentUserItem = new UserItem();
            currentUserItem.setUserId(userItem_v0.getUserId());
            currentUserItem.setVersion(userItem_v0.getCurrentVersion());
            currentUserItem.setName(name);

            mapper.save(userItem_v0);
            mapper.save(currentUserItem);
        }
        catch(Exception ex){
            ex.printStackTrace();
            return false;
        }
        return true;
    }

    private Map<String, Object> toMap(UserItem userItem){
        Map<String, Object> map = new HashMap<>();
        Map<String, String> name = new HashMap<>();
        name.put("firstname", userItem.getName().getFirstname());
        name.put("lastname", userItem.getName().getLastname());

        map.put("userId", userItem.getUserId());
        map.put("version", userItem.getVersion());
        map.put("currentVersion", userItem.getCurrentVersion());
        map.put("name", name);

        return map;
    }

    public String toJSONString(UserItem userItem){
        return new JSONObject(this.toMap(userItem)).toJSONString();
    }

    public String toJSONString(List<UserItem> userItemList){
        ArrayList<Map> jsonStringList = new ArrayList<>();
        for(UserItem userItem: userItemList){
            jsonStringList.add(this.toMap(userItem));
        }
        return JSONArray.toJSONString(jsonStringList);
    }
}
