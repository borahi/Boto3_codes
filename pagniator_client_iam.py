import boto3

client = boto3.client("iam")
paginator = client.get_paginator('list_users')
page_it = paginator.paginate()

for user in page_it:
    for username in user:
        print (username)