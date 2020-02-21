package com.amazonaws.handlers;

import com.amazonaws.models.requests.FileParserHandlerRequest;
import com.amazonaws.services.lambda.runtime.Context;
import com.amazonaws.services.lambda.runtime.LambdaLogger;
import com.amazonaws.services.lambda.runtime.RequestHandler;
import com.amazonaws.utils.GatewayResponse;
import com.amazonaws.utils.StatusCode;

public class ApiHandler implements RequestHandler<FileParserHandlerRequest, GatewayResponse> {

    public GatewayResponse handleRequest(FileParserHandlerRequest request, Context context) {

        LambdaLogger logger = context.getLogger();
        logger.log(String.format("Log output: Hello "));

        return new GatewayResponse(StatusCode.HTTP_200_OK, "Response");

    }
}
