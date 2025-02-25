import boto3
import subprocess
import json

# Create an EC2 client
ec2 = boto3.client("ec2")

# Specify your instance ID
instance_id = "i-09e34b32b6e0b98e1"

# Retrieve instance details
response = ec2.describe_instances(InstanceIds=[instance_id])
state = response["Reservations"][0]["Instances"][0]["State"]["Name"]
print("Instance state:", state)

# Start or stop the instance based on its state
if state == "stopped":
    print("Starting the instance")
    ec2.start_instances(InstanceIds=[instance_id])
else:
    print("Stopping the instance")
    ec2.stop_instances(InstanceIds=[instance_id])


# Stop and Start Instance with AWS CLI Command with subprocess
# Example 1:
# response = subprocess.run(["aws", "ec2", "describe-instances", "--instance-ids", "i-09e34b32b6e0b98e1"], capture_output=True, text=True)
# data = json.loads(response.stdout)
# # print(data)
# state = data["Reservations"][0]["Instances"][0]["State"]["Name"]
# print(state)
# if state == "stopped":
#     print("Start the instance")
#     subprocess.run(["aws", "ec2", "start-instances", "--instance-ids", "i-09e34b32b6e0b98e1"])
# else: 
#     print("stop the instance")
#     subprocess.run(["aws", "ec2", "stop-instances", "--instance-ids", "i-09e34b32b6e0b98e1"])


