import boto3
import os
import json
# Initialize S3 client
client = boto3.client("s3")
# Create the bucket
# try:
#     response = client.create_bucket(
#         Bucket="lambdabucketfortraining20251",
#         CreateBucketConfiguration={
#             'LocationConstraint':"us-east-2"  # Required for regions other than 'us-east-1'
#         }

#     )

#     print("Bucket created successfully:", response)

# except Exception as e:
#     print("Error creating bucket:", str(e))





event = {
    "name": "yemi",
    "key": "45743",
    "state": "kansas"
}


def lambda_handler(event, context):
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": f'{event['key']} is the key',
        }),
    }


# response = app_handler("options", event = {"key": "password"} )
response = lambda_handler(event, "context")

print(response)




