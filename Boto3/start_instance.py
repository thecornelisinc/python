import boto3
ec2_client=boto3.client('ec2')


response = ec2_client.start_instances(
    InstanceIds=[
        'i-0b4db7c84797f0477',
    ],
)

print(response)