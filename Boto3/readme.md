# Important links:

- Documentation:
    https://boto3.amazonaws.com/v1/documentation/api/latest/index.html#

- Installation
    https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html#installation

- Configuration
    https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html#configuration

- Available Services:
    https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/index.html




# Configuration

a. Configure AWS Credentials
    [default]
    aws_access_key_id = AKIA*************
    aws_secret_access_key = *************


b. Configure Boto3 Programmatically

    import boto3

    session = boto3.Session(
        aws_access_key_id="AKIA*************",
        aws_secret_access_key="*************",
        region_name="us-east-1"
    )

    s3_client = session.client("s3")
