import boto3

ecr_client = boto3.client("ecr")
repository_name = "my-new-cloud-native-repo"
response = ecr_client.create_repository(repositoryName=repository_name)

respository_uri = response['repository']['repositoryUri']
print(respository_uri)

# dckr_pat_xG3ZnKa7k2wz4qE7MEXj2C5SCsE
