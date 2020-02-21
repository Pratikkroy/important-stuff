package com.amazonaws.models.requests;

import lombok.Data;

@Data
public class FileParserHandlerRequest {
    String firstName;
    String lastName;

    public FileParserHandlerRequest(String firstName, String lastName) {
        this.firstName = firstName;
        this.lastName = lastName;
    }

    public FileParserHandlerRequest() {
    }
}
