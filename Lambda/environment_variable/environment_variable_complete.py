import os
import json
import boto3

sts_client = boto3.client("sts")
def lambda_handler(event, context):
    # Get environment variables
    aws_region = os.environ.get("AWS_REGION")  # Default to 'us-east-1' if not set
    aws_account_id = os.environ.get("AWS_ACCOUNT_ID", sts_client.get_caller_identity()["Account"])
    s3_bucket_name = os.environ.get("S3_BUCKET_NAME", "my_default_bucket")
    secret_code = os.environ.get("SECRET_CODE", "000000-000000-00000")

    # Logging the values (for debugging purposes)
    print(f"AWS Region: {aws_region}")
    print(f"AWS Account ID: {aws_account_id}")
    print(f"S3 Bucket Name: {s3_bucket_name}")
    print(f"Secret Code: {secret_code}")

    # Return a response with the environment variables
    return {
        "statusCode": 200,
        "body": json.dumps({
            "AWS Region": aws_region,
            "AWS Account ID": aws_account_id,
            "S3 Bucket Name": s3_bucket_name,
            "Secret Code": secret_code
        })
    }
lambda_handler("a", "b")