package com.amazonaws.utils;

import lombok.Data;

@Data
public class GatewayResponse {

    private final int statusCode;
    private final String body;

    public GatewayResponse(final int statusCode, final String body){
        this.statusCode = statusCode;
        this.body = body;
    }

}
