import paho.mqtt.client as mqtt
import paho.mqtt.subscribe as subscribe
import time
import json
import configparser
import pygame
pygame.init()
pygame.mixer.music.load('musica.mp3')

def on_message(client,userdate,message):
    dados=json.loads(str(message.payload.decode()))
    if dados['field1'] == '1.00':
        pygame.mixer.music.play()
        print("Tocar musica na sala")
    else:
        pygame.mixer.music.stop()

broker="mqtt.thingspeak.com"
port=1883
config=configparser.ConfigParser()
config.read('conf')
topico=config['THINGSPEAK']['TOPICO_SUBSCRIBE']
username=config['THINGSPEAK']['USERNAME']
password=config['THINGSPEAK']['MQTT_API_KEY']
subscribe.callback(on_message,qos=0,topics=topico,hostname=broker,port=port,client_id="clisub",auth={'username':username,'password':password})

while (True):
    time.sleep(20)