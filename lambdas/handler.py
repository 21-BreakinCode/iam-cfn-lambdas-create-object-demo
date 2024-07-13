import boto3

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    s3.put_object(Bucket=event['bucket'], Key='example.txt', Body='This is a test file.')
    return {
        'statusCode': 200,
        'body': 'File created successfully!'
    }