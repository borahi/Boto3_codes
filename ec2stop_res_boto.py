import boto3

ec2 = boto3.resource("ec2")
print ("Please enter your ec2 machine instance id:")
ec2_id = input()

instance = ec2.Instance(ec2_id)
# print (dir(instance))  ## to print all possible options## 
print ("instance Name is:" ,instance.tags)

print (instance.instance_id)
print ("instance image id is:" ,instance.image_id)
print ("instance typr is:" ,instance.instance_type)
print ("instance root device type is:" ,instance.root_device_type)
print ("instance pvt ip is:", instance.private_ip_address)
print ("##### I am stopping the instance" , ec2_id, "#####" )

instance.stop()
instance.wait_until_stopped()

print ("##### Machine has been stopped and down now")


