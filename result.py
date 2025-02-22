

response ={
    "Reservations": [
        {
            "ReservationId": "r-0bb1deda2cdcf9c37",
            "OwnerId": "357225030460",
            "Groups": [],
            "Instances": [
                {
                    "Architecture": "x86_64",
                    "BlockDeviceMappings": [
                        {
                            "DeviceName": "/dev/xvda",
                            "Ebs": {
                                "AttachTime": "2025-02-22T06:26:25+00:00",
                                "DeleteOnTermination": True,
                                "Status": "attached",
                                "VolumeId": "vol-0590ec0e7e273e363"
                            }
                        }
                    ],
                    "ClientToken": "b07933c3-5005-4677-9e1d-1abe3d813b5e",
                    "EbsOptimized": False,
                    "EnaSupport": True,
                    "Hypervisor": "xen",
                    "NetworkInterfaces": [
                        {
                            "Association": {
                                "IpOwnerId": "amazon",
                                "PublicDnsName": "ec2-54-165-249-250.compute-1.amazonaws.com",
                                "PublicIp": "54.165.249.250"
                            },
                            "Attachment": {
                                "AttachTime": "2025-02-22T06:26:25+00:00",
                                "AttachmentId": "eni-attach-0d045339400632e0f",
                                "DeleteOnTermination": True,
                                "DeviceIndex": 0,
                                "Status": "attached",
                                "NetworkCardIndex": 0
                            },
                            "Description": "",
                            "Groups": [
                                {
                                    "GroupId": "sg-0c8ced18bdb456229",
                                    "GroupName": "launch-wizard-6"
                                }
                            ],
                            "Ipv6Addresses": [],
                            "MacAddress": "12:00:10:d5:31:c5",
                            "NetworkInterfaceId": "eni-0fc80f083fca6ab89",
                            "OwnerId": "357225030460",
                            "PrivateDnsName": "ip-172-31-93-159.ec2.internal",
                            "PrivateIpAddress": "172.31.93.159",
                            "PrivateIpAddresses": [
                                {
                                    "Association": {
                                        "IpOwnerId": "amazon",
                                        "PublicDnsName": "ec2-54-165-249-250.compute-1.amazonaws.com",
                                        "PublicIp": "54.165.249.250"
                                    },
                                    "Primary": True,
                                    "PrivateDnsName": "ip-172-31-93-159.ec2.internal",
                                    "PrivateIpAddress": "172.31.93.159"
                                }
                            ],
                            "SourceDestCheck": True,
                            "Status": "in-use",
                            "SubnetId": "subnet-08b6d0a3e341a30ea",
                            "VpcId": "vpc-0ab56c59dbf88caaa",
                            "InterfaceType": "interface"
                        }
                    ],
                    "RootDeviceName": "/dev/xvda",
                    "RootDeviceType": "ebs",
                    "SecurityGroups": [
                        {
                            "GroupId": "sg-0c8ced18bdb456229",
                            "GroupName": "launch-wizard-6"
                        }
                    ],
                    "SourceDestCheck": True,
                    "Tags": [
                        {
                            "Key": "Name",
                            "Value": "demi"
                        }
                    ],
                    "VirtualizationType": "hvm",
                    "CpuOptions": {
                        "CoreCount": 1,
                        "ThreadsPerCore": 1
                    },
                    "CapacityReservationSpecification": {
                        "CapacityReservationPreference": "open"
                    },
                    "HibernationOptions": {
                        "Configured": False
                    },
                    "MetadataOptions": {
                        "State": "applied",
                        "HttpTokens": "required",
                        "HttpPutResponseHopLimit": 2,
                        "HttpEndpoint": "enabled",
                        "HttpProtocolIpv6": "disabled",
                        "InstanceMetadataTags": "disabled"
                    },
                    "EnclaveOptions": {
                        "Enabled": False
                    },
                    "BootMode": "uefi-preferred",
                    "PlatformDetails": "Linux/UNIX",
                    "UsageOperation": "RunInstances",
                    "UsageOperationUpdateTime": "2025-02-22T06:26:25+00:00",
                    "PrivateDnsNameOptions": {
                        "HostnameType": "ip-name",
                        "EnableResourceNameDnsARecord": True,
                        "EnableResourceNameDnsAAAARecord": False
                    },
                    "MaintenanceOptions": {
                        "AutoRecovery": "default"
                    },
                    "CurrentInstanceBootMode": "legacy-bios",
                    "InstanceId": "i-09e34b32b6e0b98e1",
                    "ImageId": "ami-05b10e08d247fb927",
                    "State": {
                        "Code": 16,
                        "Name": "running"
                    },
                    "PrivateDnsName": "ip-172-31-93-159.ec2.internal",
                    "PublicDnsName": "ec2-54-165-249-250.compute-1.amazonaws.com",
                    "StateTransitionReason": "",
                    "AmiLaunchIndex": 2,
                    "ProductCodes": [],
                    "InstanceType": "t2.micro",
                    "LaunchTime": "2025-02-22T17:35:40+00:00",
                    "Placement": {
                        "GroupName": "",
                        "Tenancy": "default",
                        "AvailabilityZone": "us-east-1a"
                    },
                    "Monitoring": {
                        "State": "disabled"
                    },
                    "SubnetId": "subnet-08b6d0a3e341a30ea",
                    "VpcId": "vpc-0ab56c59dbf88caaa",
                    "PrivateIpAddress": "172.31.93.159",
                    "PublicIpAddress": "54.165.249.250"
                }
            ]
        }
    ]
}

print(response["Reservations"][0]["Instances"][0]["Architecture"])