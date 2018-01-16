import boto3

from docker_name import GetRandomName

def main():
    GetRandomName()

def lambda_handler(event, context)
    ec2 = boto3.resource('ec2')
    name = GetRandomName()
    instance_id = event['detail']['EC2InstanceId']
    ec2.create_tags(Resources=[instance_id], Tags=[{'Key':'docker-name', 'Value':name}])
)

main()