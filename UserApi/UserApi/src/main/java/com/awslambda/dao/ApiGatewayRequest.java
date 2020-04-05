package com.awslambda.dao;

import com.fasterxml.jackson.databind.ObjectMapper;

import java.util.HashMap;
import java.util.Map;

public class ApiGatewayRequest {

    public static Map<Object,Object> parseRequestBody(String requestString){
        try{
            return new ObjectMapper().readValue(requestString, HashMap.class);
        }
        catch(Exception pex){
            pex.printStackTrace();
            return null;
        }
    }
}
