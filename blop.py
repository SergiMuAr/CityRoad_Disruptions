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


@bcn_mobilitat => 123851794

@transitc32nord => 412411621

@catinformacio => 262606630

@maticatradio => 59775384

@rac1 => 18577646

@catalunyaradio => 7679392

@clubracc => 155930023

@interiorcat => 110647916

@tv3cat => 28373820

@324cat => 8330472

@gencat => 27477225

@equipviari => 274008117

@mossos => 110946158

@bomberscat => 110946582

@emergenciescat => 121146038

@transit => 112385035

@tmb_barcelona => 115624105

@bcn_ajuntament => 423369901

@policia => 23791197