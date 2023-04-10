def upload_file(bucket, local_path, mediafile_key, mimetype = 'image/png'):
    try:
        import boto3

        s3 = boto3.client('s3')
        s3.upload_file(local_path, bucket, mediafile_key,
                                    ExtraArgs={
                                        "ContentType": mimetype
                                    }
        
        print('File uplouded')
        return True

    except Exception as err:
        print(err)
        return None
