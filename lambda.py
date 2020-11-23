import json
import handler.file_processor as file_processor

def check_file(event, context):
    json_string = json.dumps(event).replace("'", "\"")
    converted_event = json.loads(json_string)    
    topics = converted_event['Records'][0]
    print(topics)
    print('====================')
    s3_event = topics['Sns']['Message']
    print(s3_event)
    print('====================')
    record = s3_event['Records'][0]
    print(record)
    print('====================')
    bucket_name = record["s3"]["bucket"]["name"]
    key = record["s3"]["object"]["key"]
    print(bucket_name)
    print('====================')
    print(key)
    print('====================')
    # for topic in event["Records"]:
    #     print('Topic:' + topic)
    #     print('==========================')
    #     s3_event = json.loads(topic["Sns"]["Message"])
    #     print("s3 event: " + s3_event)
    #     print('==========================')
    #     for record in s3_event["Records"]:
    #         bucket_name = record["s3"]["bucket"]["name"]
    #         print("Bucket: " + bucket_name)
    #         print('==========================')
    #         key = record["s3"]["object"]["key"]
    #         print("Key: " + key)
    #         print('==========================')
    #         file_processor.process_new_text_file(bucket_name, key)
    file_processor.process_new_text_file(bucket_name, key)
   