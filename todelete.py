import profile
import boto3
from botocore.config import Config

my_config = Config(
    region_name = 'ap-south-1',
    signature_version = 'v4',
    retries = {
        'max_attempts': 10,
        'mode': 'standard'
    }
)

cfn=boto3.client('cloudformation', config=my_config)

cfn.delete_stack(StackName='new-stack')