import boto3

# Initialize a session using Amazon EC2
ec2 = boto3.resource('ec2')

# Define the AMI ID for Ubuntu 20.04 LTS
# Note: AMI IDs vary by region. Replace with the appropriate AMI ID for your region.
ami_id = 'ami-04a81a99f5ec58529'  # Example for Ubuntu 20.04 in us-east-1 (change according to your region)

# Create an EC2 instance
instances = ec2.create_instances(
    ImageId=ami_id,             # The AMI ID of the Ubuntu image
    InstanceType='t2.micro',    # The instance type
    MinCount=1,                 # Minimum number of instances to launch
    MaxCount=1,                 # Maximum number of instances to launch
    KeyName='mytestserver1',    # Replace with your key pair name
    SecurityGroupIds=['sg-015f047bdfe767637'],  # Replace with your security group ID
    SubnetId='subnet-0cfe0437f9c7bdb16 '         # Replace with your subnet ID
)

print('Waiting for instance to start...')
instance = instances[0]
instance.wait_until_running()

# Reload the instance attributes
instance.load()

print(f'Instance ID: {instance.id}')
print(f'Public IP Address: {instance.public_ip_address}')
print(f'Private IP Address: {instance.private_ip_address}')

