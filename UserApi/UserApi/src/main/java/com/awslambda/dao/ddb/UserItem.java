package com.awslambda.dao.ddb;

import lombok.Data;
import lombok.NoArgsConstructor;

import com.amazonaws.services.dynamodbv2.datamodeling.*;

@Data
@NoArgsConstructor
@DynamoDBTable(tableName="User")
public class UserItem {

    @DynamoDBHashKey(attributeName= "userId" )
    private String userId;

    @DynamoDBRangeKey(attributeName = "version")
    private Integer version;

    @DynamoDBAttribute(attributeName = "currentVersion")
    private Integer currentVersion;

    @DynamoDBAttribute(attributeName = "name")
    private Name name;

    @Data
    @DynamoDBDocument
    public static class Name {

        @DynamoDBAttribute(attributeName = "firstname")
        private String firstname;

        @DynamoDBAttribute(attributeName = "lastname")
        private String lastname;

    }

}