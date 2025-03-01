# What is AWS Lambda?

AWS Lambda is the compute service for serverless. You can run code without servers, it invokes based on events 
you configure, and it scales automatically based on demand. 


# Key Benefits:

    - You can run code without provisioning or maintaining servers.
    - It initiates functions for you in response to events.
    - It scales automatically.
    - It provides built-in code monitoring and logging via Amazon CloudWatch.

# Key Components
    - Functions
        - Runtime
        - Event
        - Concurrrency
        - Trigger
        - Layers
        - configuration:
            * Environment Variables
            * Attaching Functions to VPC
            * 

# Function
    A function is a resource that you can invoke to run your code in AWS Lambda

# Runtime
    Lambda runtimes allow functions in different languages to run in the same base runtime environment. 
    Supported language: https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtimes.html#runtimes-supported
    


# Event
    An event is a JSON formatted document that contains data for a function to process

# Concurrency 
    Concurrency is the number of requests your function is serving at any given time

# Trigger
    A trigger is a resource or configuration that invokes a Lambda function. 
    This includes AWS services that can be configured to invoke a function, applications you develop, and event source mappings

# Lamda Function requirements
    To create a lambda function, you need to:
    - Define permissions for the function using AWS IAM.
    - Specifgy what events will invoke the function
    - Provide the code, dependencies, and Libraries needed to run the code
    - Configure runtime parameters such as:
        * Memory
        * Timeout
        * Concurrency

# IAM Role for AWS Lambda Function Execution
    AWS Lambda have two set of permission. 
     a. Execution Role (IAM Role Attached to Lambda)
        Permissions that your Lambda functions need to perform API actions and access other AWS resources
        E.g AWSLambdaBasicExecutionRole

     b. Resource-Based Policy (IAM Policy Attached to AWS Resources)
        Permissions that other AWS users and entities need to access your Lambda functions
        E.g AWSLambdaRole


# Creating your Basic First Lambda Function
  Follow this steps to create a basic lambda function:
    a. Go to Lambda Home Page
    b. Choose Create function
    c. Select Author from scratch
    d. In the Basic information pane, for Function name, enter my_Simple_function
    e. For Runtime, choose Python 3.13
    f. Leave architecture set to x86_64, and then choose Create function.

# Review the Lambda Lunction 
    Follow this step to review the lambda function
    a. Choose the Code tab.
    b. Paste the one of the code into the lambda_function.py tab, replacing the code that Lambda created.
    c. Invoke the Lambda function using the console code editor
        * In the TEST EVENTS section of the console code editor, choose Create test event.
        * For Event Name, enter sampleEventTrigger.
        * n the Event JSON section, replace the default JSON with the following:
            * The Data that you want to pass to the function when called. 
            E.g fruits = ["ORANGE", "APPLE", "BANANA", "APPLE"]  ==> ensure to convert to Json as the event is in json
              The above will will be converted to:
              {"fruits": ["ORANGE", "APPLE", "BANANA", "APPLE"]}
    d. Choose Save.
    e. Test your function and view invocation records

# Advance Example: 
https://docs.aws.amazon.com/lambda/latest/dg/services-apigateway-tutorial.html


# Clean Delete the Sample function.


# Understanding Event and Context
    Event:
        Contains the data sent to the Lambda function.

    Context:
        Provides runtime information about the Lambda execution.

# Event Parameter:
    - The event parameter contains the input data that triggers the Lambda function.
    - The structure of event varies depending on the triggering service (e.g., SampleTest, API Gateway, S3, SNS, DynamoDB).

      Examples 1. s3 Event:

        {
        "Records": [
            {
            "eventSource": "aws:s3",
            "eventName": "ObjectCreated:Put",
            "s3": {
                "bucket": { "name": "my-bucket" },
                "object": { "key": "image.jpg" }
            }
            }
        ]
        }
        To get the name of the bucket: event['Records'][0]['s3']['bucket']['name'] 
        Output:                        "my-bucket"

     Example 2: API Gateway
        {
            "httpMethod": "POST",
            "body": "{\"name\": \"Sam\", \"title\": \"Engineer\", \"company\": \"Amazon\"}",
            "queryStringParameters": { "id": "123" }
        }

        To get the body: event['body']
        Output: "{"name": "Sam", "title": "Engineer", "company": "Amazon"}"

# Context Parameter:
    Key Attributes in context are:

    * context.function_name:   	        Name of the Lambda function
    * context.function_version:	        Version of the function
    * context.invoked_function_arn:	    ARN of the function
    * context.memory_limit_in_mb:	    Memory allocated to the function
    * context.aws_request_id:     	    Unique request ID for this execution
    * context.log_group_name:     	    CloudWatch Log Group name
    * context.log_stream_name:          CloudWatch Log Stream name


# Configuration:
    - Configuring function memory 
    - Configuring ephemeral storage 
    - Configure Lambda function timeout ==> Not more than 15 minutes/ 900 seconds 
    - Environment Variable

# Working with Environment Variable
        * Creating Lambda environment variables
        * Retrieving Lambda environment variables
            - Example: 
                region = os.environ['AWS_REGION']
                region = os.environ.get('AWS_REGION')
        * There are some in-built lambda variable that you can't set but can use them. See link below
            https://docs.aws.amazon.com/lambda/latest/dg/configuration-envvars.html#configuration-envvars-runtime

# Giving Lambda functions access to resources in an Amazon VPC
    - By Default, Every Lambda function runs inside a VPC that is owned and managed by the Lambda service. 
    - These VPCs are maintained automatically by Lambda and are not visible to customers
    - You can give your Lambda function access to resources hosted in an Amazon VPC by attaching your function to the VPC through the private subnets that contain the resources
    - When you attached your lambda function to a VPC owned and managed by you,this configuration has no effect on the Lambda-managed VPC your function runs inside
    - Before you attached Lambda to A VPC managed by you, ensure the following:
        a. Lambda invoke permission
            use this AWS_Managed_permission ==> AWSLambdaVPCAccessExecutionRole 
            To Create your customer managed permission see required acctions in the link below
                https://docs.aws.amazon.com/lambda/latest/dg/configuration-vpc.html#configuration-vpc-permissions

    - How to Attach a new Lambda Function to a VPC in your account
        Follow this steps:
        a. Follow the steps you learn above to create a function
        b. Before saving the function, under Additional Configurations:
            - check "enable VPC" then select your preferred VPC.
            - Select a Subent
            - Select Security Group

    - How to Attach existing function to VPC:
        Follow this steps:
        a. Open the Lambda function
        b. Choose configuration Lab from the lambda, then VPC
            - check "enable VPC" then select your preferred VPC.
            - Select a Subent
            - Select Security Group

# Granting Internet access to Lambda when attached to a VPC
    - By default , the Lambda Function have internet access.
    - When you attached a Lamdba function to your VPC,if the Function need to use internet access from that vpc, then you have to configure the vpc to have internet access. 

# Printing to the log
    - To send basic output to the logs, you can use a print method in your function
    - Using Log libery called logging read more about the library here https://docs.python.org/3/library/logging.html
    - Using the Logger:
        a. import logging Module: 
            Handles logging of messages for debugging, tracking execution flow, and monitoring
        b. Setting Up Logging
            logger = logging.getLogger()   ==>  Gets the root logger (global logging instance).
            logger.setLevel("INFO")         ==> Configures logging to capture INFO-level messages and above (INFO, WARNING, ERROR, CRITICAL).
        c. useage
            Example: logger.info('ENVIRONMENT VARIABLES')
            Logs the message "ENVIRONMENT VARIABLES" to CloudWatch Logs.



print("region_name)

logger.info(region_name)
