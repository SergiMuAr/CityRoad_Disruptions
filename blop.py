from KafkaProd import * 
import json
from bson import json_util

kafka_producer = KafkaClPr()

data = { 'tweet ': 'Això representa un tweet qualssevol',
    'Autor' : 'sam',
}  

print ("HOLA1", str(json.dumps(data, default=json_util.default).encode('utf-8')))
# kafka_producer.publish_message('test', "twAuthor",str(json.dumps(data, default=json_util.default).encode('utf-8')))
kafka = KafkaConsumer('test', auto_offset_reset='earliest',
                            bootstrap_servers=['localhost:9092'], api_version=(0, 10), consumer_timeout_ms=-1)

for msg in kafka: 
    print ("HOLA2",msg.value)
    txt = msg.value.decode("utf-8")  
    print ("HOLA3",txt)
    # print (json.loads(txt)['tweet'])

