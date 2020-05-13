# Kinesis Data Analytics
        data_analytics = analytics.CfnApplication(self, "DataAnalytics",
          application_name = config.name("DeliveryStreamAnalytics")  ,
          application_code = config.sql(),
          inputs = [
            {
            "inputSchema" : {
              "recordColumns" : [
                {
                "name" : "UserId",
                "sqlType" : "INTEGER",
                "mapping" : "$.endpoint.User.UserId"
                },
                {
                "name" : "Id",
                "sqlType" : "VARCHAR(8)",
                "mapping" : "$.endpoint.Id"
                },
                {
                "name" : "event_type",
                "sqlType" : "VARCHAR(8)",
                "mapping" : "$.event_type"
                },
                {
                "name" : "event_timestamp",
                "sqlType" : "BIGINT",
                "mapping" : "$.event_timestamp"
                },
              ],
              "recordEncoding" : "UTF-8",
              "recordFormat" : {
                "mappingParameters" : {
                  "JSONMappingParameters" : { 
                    "recordRowPath" : "$"
                  }
                },
                "recordFormatType" : "JSON"
              }
            },
            "kinesisFirehoseInput" : {
              "resourceArn" : delivery_stream_s3,
              "roleArn" : analytics_iam_role.role_arn,
            },
            "namePrefix" : "SourceStream",
          }]
        )
        
        # Kinesis Data Analytics Output
        analytics_output = analytics.CfnApplicationOutput(self, "AnalyticsOutput",
          application_name = data_analytics.ref,
          output = {
            "name": "DESTINATION_SQL_STREAM",
            "destinationSchema" : {
              "recordFormatType" : "JSON"
            },
            "kinesisFirehoseOutput" : {
              "resourceArn" : delivery_stream_elasticsearch.attr_arn,
              "roleArn" : analytics_iam_role.role_arn,
            }
          }
        )
        
        analytics_anomaly_output = analytics.CfnApplicationOutput(self, "AnalyticsAnomalyOutput",
          application_name = data_analytics.ref,
          output = {
            "name": "DESTINATION_SQL_STREAM_01",
            "destinationSchema" : {
              "recordFormatType" : "JSON"
            },
            "lambdaOutput" : {
              "resourceArn" : anomaly_detection.function_arn,
              "roleArn" : analytics_iam_role.role_arn,
            }
          }
        )
