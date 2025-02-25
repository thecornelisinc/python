import boto3

# List of instance IDs to start
instance_ids = [
    "i-09e34b32b6e0b98e1",
    "i-0f1a779ab0eb7105b",
    "i-032d8e0b4531789f7"
]

# Create an EC2 client
ec2 = boto3.client('ec2')

# Loop through each instance and start it
for instance_id in instance_ids:
    print(f"Starting instance: {instance_id}")
    response = ec2.start_instances(InstanceIds=[instance_id])
    print(f"Response for {instance_id}:")
    print(response)


