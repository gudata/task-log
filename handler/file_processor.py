import os

import boto3
from DynamoDb import functionsDynamoDb
from datetime import date

def process_new_text_file(bucket, new_file):
    if os.path.splitext(new_file)[1] == ".txt" :
        file_name = new_file.split('/')[1]
        print(file_name)
        print('==================')
        
        if functionsDynamoDb.check_for_file(file_name) :
            print('The file already exists!')
        else :
            print('File not found, processing...')
            functionsDynamoDb.add_processed_file(file_name)
            
            today = date.today().strftime("%m-%d-%Y")
            
            s3 = boto3.resource('s3')
            copy_source = {
                'Bucket': bucket,
                'Key': new_file
            }
            
            new_bucket = bucket
            new_key = 'current/' + today + '/' + file_name
            s3.meta.client.copy(copy_source, new_bucket, new_key)
