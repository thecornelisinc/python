import os
import json

def lambda_handler(event, context):
    region_name = os.environ.get("region_name")
    account_number= os.environ.get("account_number")
    bucket_name = os.environ.get("bucket_name")
    secret_code = os.environ.get("secret_code")

    # Logging the values (for debugging purposes)
    print(f"AWS Region: {region_name}")
    print(f"AWS Account ID: {account_number}")
    print(f"S3 Bucket Name: {bucket_name} ")
    print(f"Secret Code: {secret_code}")



    # Return a response with the environment variables
    return {
        "statusCode": 200,
        "body": json.dumps({
            "AWS Region": region_name,
            "AWS Account ID": account_number,
            "S3 Bucket Name": bucket_name,
            "Secret Code": secret_code
        })
    }


