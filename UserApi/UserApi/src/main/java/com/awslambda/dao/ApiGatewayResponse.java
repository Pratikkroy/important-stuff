package com.awslambda.dao;

import com.amazonaws.services.lambda.runtime.events.APIGatewayProxyResponseEvent;
import org.json.simple.JSONObject;
import org.json.simple.parser.JSONParser;

import java.util.Collections;
import java.util.HashMap;
import java.util.Map;

public class ApiGatewayResponse {

    public static void generateResponse(APIGatewayProxyResponseEvent apiGatewayProxyResponseEvent, String responseMessage) {
        apiGatewayProxyResponseEvent.setHeaders(Collections.singletonMap("timeStamp", String.valueOf(System.currentTimeMillis())));
        apiGatewayProxyResponseEvent.setStatusCode(200);

        Map<Object,Object> responseBodyMap = new HashMap<>();
        responseBodyMap.put("data", responseMessage);
        responseMessage = convertMapToJSONString(responseBodyMap);
        apiGatewayProxyResponseEvent.setBody(responseMessage);


    }

    public static void generateResponse(APIGatewayProxyResponseEvent apiGatewayProxyResponseEvent, Map<Object, Object> responseMessageMap) {
        String responseMessage = convertMapToJSONString(responseMessageMap);
        generateResponse(apiGatewayProxyResponseEvent,responseMessage);
    }

    private static String convertMapToJSONString(Map<Object, Object> map){
        return new JSONObject(map).toJSONString();
    }
}
