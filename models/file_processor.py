import os

import boto3
from dynamo_db import dynamo_db
from datetime import date


def is_key_in_scope(name):
    return os.path.splitext(name)[1] == ".txt" 

def get_basename(key):
    return key.split('/')[1] 

def new_text_file(bucket, key):
    if not is_key_in_scope(key) :
        return False
    
    file_name = get_basename(key)
    
    if not dynamo_db.check_for_file(file_name) :
      
        dynamo_db.add_processed_file(file_name)
            
        today = date.today().strftime("%m-%d-%Y")
            
        s3 = boto3.resource('s3')
        copy_source = {
            'Bucket': bucket,
            'Key': key
        }
            
        new_bucket = bucket
        new_key = 'current/' + today + '/' + file_name
        s3.meta.client.copy(copy_source, new_bucket, new_key)
        return True
