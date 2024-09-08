import boto3

# Initialize a session using Boto3 and create an S3 client
# Create an S3 client
s3 = boto3.client(
    's3',
    aws_access_key_id='AKIAWRGHATJHIFCGP7B6',
    aws_secret_access_key='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'
)

# Define the bucket name and the object key (file path)
bucket_name = 'intern-project1'
object_key = 'requirements.txt'  # Replace with your actual file name in the "interns" folder

# Download the S3 object
response = s3.get_object(Bucket=bucket_name, Key=object_key)

# Read the content of the file
file_content = response['Body'].read().decode('utf-8')

# Print or process the file content
print(file_content)
