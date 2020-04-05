package com.awslambda.handlers;

import java.util.List;
import java.util.Map;

import com.amazonaws.services.lambda.runtime.Context;
import com.amazonaws.services.lambda.runtime.RequestHandler;
import com.amazonaws.services.lambda.runtime.events.APIGatewayProxyRequestEvent;
import com.amazonaws.services.lambda.runtime.events.APIGatewayProxyResponseEvent;
import com.awslambda.builder.User;
import com.awslambda.dao.ApiGatewayRequest;
import com.awslambda.dao.ApiGatewayResponse;
import com.awslambda.dao.ddb.UserItem;


public class UserApiHandler implements RequestHandler<APIGatewayProxyRequestEvent, APIGatewayProxyResponseEvent> {

    public APIGatewayProxyResponseEvent handleRequest(APIGatewayProxyRequestEvent apiGatewayProxyRequestEvent, Context context) {
        APIGatewayProxyResponseEvent apiGatewayProxyResponseEvent = new APIGatewayProxyResponseEvent();
        try {

            switch (apiGatewayProxyRequestEvent.getHttpMethod().toUpperCase()){
                case "POST":
                    return this.post(apiGatewayProxyRequestEvent, context);

                case "GET":
                    return this.get(apiGatewayProxyRequestEvent, context);

                case "PUT":
                    return this.put(apiGatewayProxyRequestEvent, context);

                default:
                    ApiGatewayResponse.generateResponse(apiGatewayProxyResponseEvent, "INVALID_HTTP_METHOD");
            }

        } catch (Exception e) {
            e.printStackTrace();
            ApiGatewayResponse.generateResponse(apiGatewayProxyResponseEvent, e.getMessage());
        }

        return apiGatewayProxyResponseEvent;
    }

    private APIGatewayProxyResponseEvent post(APIGatewayProxyRequestEvent apiGatewayProxyRequestEvent, Context context){
        APIGatewayProxyResponseEvent apiGatewayProxyResponseEvent = new APIGatewayProxyResponseEvent();
        String requestBodyString = apiGatewayProxyRequestEvent.getBody();
        Map<Object,Object> requestBodyMap = ApiGatewayRequest.parseRequestBody(requestBodyString);
        String responseString = "";

        User user = new User();
        if(user.createUser((String)requestBodyMap.get("firstname"), (String)requestBodyMap.get("lastname"))){
            responseString = "SUCCESS";
        }
        else {
            responseString = "UNSUCCESS";
        }
        ApiGatewayResponse.generateResponse(apiGatewayProxyResponseEvent, responseString);
        return apiGatewayProxyResponseEvent;
    }

    private APIGatewayProxyResponseEvent get(APIGatewayProxyRequestEvent apiGatewayProxyRequestEvent, Context context){
        APIGatewayProxyResponseEvent apiGatewayProxyResponseEvent = new APIGatewayProxyResponseEvent();
        Map<String, String> pathParameters = apiGatewayProxyRequestEvent.getPathParameters();
        Map<String, String> queryParameters = apiGatewayProxyRequestEvent.getQueryStringParameters();
        String responseString = "";
        User user = new User();

        if(apiGatewayProxyRequestEvent.getPath().endsWith("history/")){
            Integer count = -1;
            try{
                if(queryParameters!=null && queryParameters.containsKey("count")) {
                    count = Integer.parseInt(queryParameters.get("count"));
                    if(count<0){
                        throw new NumberFormatException("Number should be greater than Zero");
                    }
                }
            }
            catch(NumberFormatException nfex){
                nfex.printStackTrace();
                throw nfex;
            }

            List<UserItem> userHistoryList = user.getuserHistory(pathParameters.get("userId"),count);
            responseString = user.toJSONString(userHistoryList);
        }
        else {
            UserItem userItem = user.getUser(pathParameters.get("userId"));
            responseString = user.toJSONString(userItem);
        }
        ApiGatewayResponse.generateResponse(apiGatewayProxyResponseEvent, responseString);
        return apiGatewayProxyResponseEvent;
    }

    private APIGatewayProxyResponseEvent put(APIGatewayProxyRequestEvent apiGatewayProxyRequestEvent, Context context){
        APIGatewayProxyResponseEvent apiGatewayProxyResponseEvent = new APIGatewayProxyResponseEvent();
        Map<String, String> pathParameters = apiGatewayProxyRequestEvent.getPathParameters();
        String requestBodyString = apiGatewayProxyRequestEvent.getBody();
        Map<Object,Object> requestBodyMap = ApiGatewayRequest.parseRequestBody(requestBodyString);
        String responseString = "";

        User user = new User();
        if(user.updateUser(pathParameters.get("userId"), requestBodyMap)){
            responseString = "SUCCESS";
        }
        else {
            responseString = "UNSUCCESS";
        }
        ApiGatewayResponse.generateResponse(apiGatewayProxyResponseEvent, responseString);
        return apiGatewayProxyResponseEvent;
    }
}
