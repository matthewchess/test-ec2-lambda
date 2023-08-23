import boto3
import json

def lambda_handler(event, context):
    ec2 = boto3.resource('ec2')
    
    instances_info = []
    
    # Iterate over all instances in the AWS account
    for instance in ec2.instances.all():
        instance_info = {
            'instance_id': instance.id,
            'instance_type': instance.instance_type,
            'launch_time': instance.launch_time.strftime('%Y-%m-%d %H:%M:%S'),
            'state': instance.state['Name'],
            'public_ip': instance.public_ip_address,
            'private_ip': instance.private_ip_address,
            'availability_zone': instance.placement['AvailabilityZone']
        }
        instances_info.append(instance_info)
    
    return {
        'statusCode': 200,
        'body': json.dumps(instances_info)
    }
