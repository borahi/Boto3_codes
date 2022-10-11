import boto3
from botocore.client import Paginator

iam = boto3.resource('iam')
count = 1
for user in iam.users.all():
    print (count, user.name)
    count+=1




