import boto3

# Initialize a session using Amazon EC2
ec2 = boto3.resource('ec2')

def create_instance():
    # Define the AMI ID for Ubuntu 20.04 LTS
    ami_id = 'ami-0a91d140d4f4c8c1f'  # Example for Ubuntu 20.04 in us-east-1 (change according to your region)

    # Create an EC2 instance
    instances = ec2.create_instances(
        ImageId=ami_id,             # The AMI ID of the Ubuntu image
        InstanceType='t2.micro',    # The instance type
        MinCount=1,                 # Minimum number of instances to launch
        MaxCount=1,                 # Maximum number of instances to launch
        KeyName='your-key-pair',    # Replace with your key pair name
        SecurityGroupIds=['sg-0abcd1234efgh5678'],  # Replace with your security group ID
        SubnetId='subnet-0abcd1234efgh5678'         # Replace with your subnet ID
    )

    print('Waiting for instance to start...')
    instance = instances[0]
    instance.wait_until_running()

    # Reload the instance attributes
    instance.load()

    print(f'Instance ID: {instance.id}')
    print(f'Public IP Address: {instance.public_ip_address}')
    print(f'Private IP Address: {instance.private_ip_address}')


def list_instances():
    # Describe EC2 instances
    instances = ec2.instances.all()

    for instance in instances:
        print(f'Instance ID: {instance.id}')
        print(f'State: {instance.state["Name"]}')
        print(f'Public IP Address: {instance.public_ip_address}')
        print(f'Private IP Address: {instance.private_ip_address}')
        print('---')

if __name__ == "__main__":
    action = input("Enter 'create' to create a new instance or 'list' to list existing instances: ").strip().lower()
    
    if action == 'create':
        create_instance()
    elif action == 'list':
        list_instances()
    else:
        print("Invalid option. Please enter 'create' or 'list'.")
