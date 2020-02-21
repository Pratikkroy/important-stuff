/*
 * Copyright 2017 Amazon.com, Inc. or its affiliates. All Rights Reserved.
 *
 * Licensed under the Apache License, Version 2.0 (the "License"). You may not use this file except
 * in compliance with the License. A copy of the License is located at
 *
 * http://aws.amazon.com/apache2.0
 *
 * or in the "license" file accompanying this file. This file is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the
 * specific language governing permissions and limitations under the License.
 */

package com.amazonaws.handlers;

import com.amazonaws.services.lambda.runtime.events.S3Event;
import com.amazonaws.services.lambda.runtime.Context;
import com.amazonaws.services.lambda.runtime.RequestHandler;
import com.amazonaws.services.lambda.runtime.LambdaLogger;

import java.io.InputStream;

public class FileParserHandler implements RequestHandler<S3Event, Boolean> {

    public Boolean handleRequest(S3Event s3Event, Context context) {

        LambdaLogger logger = context.getLogger();
        logger.log(String.format("New File Added in the bucket"));

//        AmazonS3Client s3Client = new AmazonS3Client(new DefaultAWSCredentialsProviderChain());
//
//        for (S3EventNotificationRecord record : s3Event.getRecords()) {
//            String s3Key = record.getS3().getObject().getKey();
//            String s3Bucket = record.getS3().getBucket().getName();
//            context.getLogger().log("found id: " + s3Bucket+" "+s3Key);
//            // retrieve s3 object
//            S3Object object = s3Client.getObject(new GetObjectRequest(s3Bucket, s3Key));
//            InputStream objectData = object.getObjectContent();
//            //insert object into elasticsearch
//        }
        return true;

    }

}
