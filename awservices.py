import boto3

s3 = boto3.resource('s3')

bucket = s3.Bucket('pywombat') 

for obj in bucket.objects.all(): 
    print(obj.key) 

s3.create_bucket(Bucket='pywombatsystemfiles', 
        CreateBucketConfiguration={ 
        'LocationConstraint': 'us-east-2'  
    })

# Some collections support extra arguments to filter the returned data set, which are passed into the underlying service operation. Use the filter() method to filter the results:

 for bucket in s3.buckets.all(): 
    print(bucket.name) 


kwargs = {
    'Bucket':'customepywombat',
    'suffix':'/*.py',
}
result = s3.list_objects_v2(**kwargs)

for obj in result.get('Contents', []):
    print(obj['Key'])