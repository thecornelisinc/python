def lambda_handler(event, context):
    print(f"Function Name: {context.function_name}")
    print(f"Memory Limit: {context.memory_limit_in_mb} MB")
    print(f"AWS Request ID: {context.aws_request_id}")
    print(f"Log Group: {context.log_group_name}")
    print(f"Log Stream: {context.log_stream_name}")
    
    return {"statusCode": 200, "body": "Lambda executed successfully!"}
