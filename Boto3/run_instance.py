import boto3

client= boto3.client('ec2')

response = client.run_instances(
    BlockDeviceMappings=[
        {
            'DeviceName': '/dev/sdf',
            'Ebs': {
                'KmsKeyId': 'e83c424c-30f2-49e7-a439-88ad806f246b',
                'VolumeSize': 8,
                'Encrypted': True
            },
        },
    ],
    ImageId='ami-05b10e08d247fb927',
    InstanceType='t2.micro',
    KeyName='terraform',
    MaxCount=1,
    MinCount=1,
    SecurityGroupIds=[
        'sg-0391978c596199e34',
    ],
    SubnetId='subnet-05112cd245227fc6a',
    TagSpecifications=[
        {
            'ResourceType': 'instance',
            'Tags': [
                {
                    'Key': 'Name',
                    'Value': 'WebServer',
                },
            ],
        },
    ],
)
print(response)

