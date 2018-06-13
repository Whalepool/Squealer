#!/usr/bin/env python3
from pika import URLParameters as pika_URLParameters, BlockingConnection as pika_BlockingConnection
from pprint import pprint
import json
import argparse

# Utils 
import utils.loadconfig as config 
import utils.wplogging as wplogging


# Args  
parser = argparse.ArgumentParser()
parser.add_argument('--msg', type=str, help='ca message to send to telegram', required=True)
parser.add_argument('--chat_id', type=int, help='a specific chat id to message to ', default=config.ADMIN_CHAT_ID)
args = parser.parse_args()



msg = {
	'chat_id': args.chat_id,
	'msg': args.msg
}



params = pika_URLParameters('amqp://'+str(config.RABBIT_USER)+':'+str(config.RABBIT_PASSWORD)+'@'+str(config.RABBIT_IP)+':'+str(config.RABBIT_PORT)+'/'+str(config.RABBIT_VHOST)+'?socket_timeout='+str(config.RABBIT_TIMEOUT))
connection = pika_BlockingConnection(params)
channel = connection.channel()
channel.exchange_declare(exchange=config.RABBIT_EXCHANGE)

channel.exchange_declare(exchange=config.RABBIT_EXCHANGE)   
channel.basic_publish(exchange=config.RABBIT_EXCHANGE, routing_key=config.RABBIT_ROUTING_KEY, body=json.dumps(msg))