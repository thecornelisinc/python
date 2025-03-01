import boto3
import json

# Initialize EC2 client
ec2_client = boto3.client("ec2")

def lambda_handler(event, context):
    try:
        # Describe Network Interfaces
        network_interfaces = ec2_client.describe_network_interfaces()
        print(f"Existing Network Interfaces: {json.dumps(network_interfaces, indent=2)}")

        # Get first available subnet
        subnets = ec2_client.describe_subnets()["Subnets"]
        subnet_id = subnets[0]["SubnetId"]  # Select first subnet

        # # Create a new Network Interface
        response = ec2_client.create_network_interface(
            SubnetId=subnet_id,
            Description="Lambda-created ENI",
            Groups=[],  # Add security group IDs if needed
            PrivateIpAddress="10.0.16.20"  # Ensure this IP is free in the subnet
        )

        network_interface_id = response["NetworkInterface"]["NetworkInterfaceId"]
        print(f"Created Network Interface ID: {network_interface_id}")

        return {"statusCode": 200, "body": json.dumps("Lambda executed successfully!")}

    except Exception as e:
        return {"statusCode": 500, "body": json.dumps({"error": str(e)})}
