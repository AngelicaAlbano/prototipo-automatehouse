import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish
import random
import time
import configparser

broker="mqtt.thingspeak.com"
port=1883
config=configparser.ConfigParser()
config.read('conf')
topico=config['THINGSPEAK']['TOPICO_PUBLISH']
valor_movimento=0

while(True):
   valor_movimento= random.randint(0,1) # Se 1 -> ABRIU
   dados = "field1={:.2f}&status=ABRIU".format(valor_movimento)
   publish.single(payload=dados,topic=topico,port=port,hostname=broker)
   print(dados)
   time.sleep(20)
