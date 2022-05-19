import boto3
from botocore.config import Config
import sys

print(str(sys.argv[1]))
print(str(sys.argv[2]))
print(str(sys.argv))

my_config = Config(
    region_name = 'ap-south-1',
    signature_version = 'v4',
    retries = {
        'max_attempts': 10,
        'mode': 'standard'
    }
)

cfn_session=boto3.session.Session(aws_access_key_id=str(sys.argv[1]),aws_secret_access_key=str(sys.argv[2]), region_name='ap-south-1')

cfn=cfn_session.client('cloudformation', config=my_config)

print(cfn.create_stack(StackName=str(sys.argv[2]),
 TemplateURL='https://for-practice-inkwell.s3.ap-south-1.amazonaws.com/task.yml',
 Parameters=[
        {
            'ParameterKey': 'InstanceTypeChoice',
            'ParameterValue': (str(sys.argv[1])),
            'UsePreviousValue': True,
            'ResolvedValue': 'string'
        },
    ]))