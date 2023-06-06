import os

import boto3
from botocore.client import Config

ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY", "")
ACCESS_SECRET_KEY = os.environ.get("AWS_SECRET_KEY", "")
BUCKET_NAME = os.environ.get("AWS_BUCKET_NAME", "")
REGION = os.environ.get("AWS_REGION", "")
FILE_URL_EXPR_TIME = 100
HAS_AWS_SUPPORT = ACCESS_KEY_ID and ACCESS_SECRET_KEY + BUCKET_NAME and REGION

s3_obj = None


def generate_s3_object():
    global s3_obj
    if s3_obj is None:
        s3_obj = boto3.resource(
            's3',
            aws_access_key_id=ACCESS_KEY_ID,
            aws_secret_access_key=ACCESS_SECRET_KEY,
            config=Config(signature_version='s3v4')
        )
    return s3_obj


def upload(data: bytes, file_name: str, generate_presigned_url: bool = False) -> str:
    generate_s3_object().Bucket(BUCKET_NAME).put_object(Key=file_name, Body=data)
    if generate_presigned_url:
        client = boto3.client(
            's3',
            aws_access_key_id=ACCESS_KEY_ID,
            aws_secret_access_key=ACCESS_SECRET_KEY,
            region_name=REGION,
            config=Config(signature_version='s3v4', region_name=REGION),
            endpoint_url='https://s3.' + REGION + '.amazonaws.com'
        )
        return client.generate_presigned_url(
            ClientMethod='get_object',
            Params={
                'Bucket': BUCKET_NAME,
                'Key': file_name,

            },
            ExpiresIn=FILE_URL_EXPR_TIME,
        )

    return file_name


def download(file_name):
    return generate_s3_object().Bucket(BUCKET_NAME).download_file(file_name, file_name)
