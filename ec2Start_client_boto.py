import boto3

client = boto3.client('ec2')
print ("Please enter your ec2 instance id:")
ec2_id = input()

print (client.describe_instances(InstanceIds =[ec2_id]))
print ("##### I am starting the instance" , ec2_id, "#####")
client.start_instances(InstanceIds =[ec2_id])

waiter = client.get_waiter('instance_running')
waiter.wait(InstanceIds=[ec2_id])

print("EC2 instance has been started")
