import boto3
import os
import sys
import uuid
from urllib.parse import unquote_plus
from PIL import Image
import PIL.Image


s3_client = boto3.client('s3')

def convert_image(image_path, convert_path):
    image = Image.open(image_path)
    image = image.convert('RGB')
    image.save(convert_path, 'webp')

def lambda_handler(event, context):

    for record in event['Records']:

        bucket = record['s3']['bucket']['name'] # nombre del bucket origen
        bucket_dest = 'takiya' # nombre del bucket final
        key = unquote_plus(record['s3']['object']['key'])  # nombre del archivo y su extensión

        unique_code = str( uuid.uuid4() )
        orig_path = key.split('.')[0]
        orig_extension = key.split('.')[1]
        final_extension = ".webp"

        download_path = '/tmp/{}.{}'.format( unique_code, orig_extension )
        convert_path = '/tmp/{}{}'.format( uuid.uuid4(), final_extension )

        try:
            s3_client.download_file(bucket, key, download_path)
            convert_image(download_path, convert_path)
            s3_client.upload_file(convert_path, bucket_dest, orig_path + final_extension)
            s3_client.delete_object(Bucket=bucket, Key=key)
            print("Successfully. File converted : {} to {}".format(key, orig_path + final_extension))
        except Exception as e:
            print('- Error: -> {}'.format(e))
            raise e
        finally:
            os.remove(download_path)
            os.remove(convert_path)
    return True
