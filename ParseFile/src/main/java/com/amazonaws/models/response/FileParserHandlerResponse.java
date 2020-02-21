package com.amazonaws.models.response;

import lombok.Data;

@Data
public class FileParserHandlerResponse {

    String greetings;

    public FileParserHandlerResponse(String greetings) {
        this.greetings = greetings;
    }

    public FileParserHandlerResponse() {
    }

}
