import boto3

ecr = boto3.client('ecr')

repository_name = 'monitoring-app'
response = ecr.create_repository(repository_name=repository_name)

repository_uri = response['repository']['repositoryUri']
print(repository_uri)