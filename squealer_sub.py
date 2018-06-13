#!/usr/bin/env python3
from pika import URLParameters as pika_URLParameters, BlockingConnection as pika_BlockingConnection
from pprint import pprint
from sys import exit 
import json

from telegram.ext import MessageHandler
import telegram 

# Utils 
import utils.loadconfig as config 
import utils.wplogging as wplogging


wplogging.logger.info('Setting up telegram bot...')
bot = telegram.Bot(token=config.TELEGRAM_BOT_TOKEN)

def callback(ch, method, properties, msg):
	msg = json.loads(msg.decode("utf-8"))
	pprint(msg)
	bot.sendMessage(chat_id=msg['chat_id'],text=msg['msg'],parse_mode="Markdown",disable_web_page_preview=1) 





wplogging.logger.info('Subsribing to rabbitmq...')

params = pika_URLParameters('amqp://'+str(config.RABBIT_USER)+':'+str(config.RABBIT_PASSWORD)+'@'+str(config.RABBIT_IP)+':'+str(config.RABBIT_PORT)+'/'+str(config.RABBIT_VHOST)+'?socket_timeout='+str(config.RABBIT_TIMEOUT))
connection = pika_BlockingConnection(params)
channel = connection.channel()
channel.exchange_declare(exchange=config.RABBIT_EXCHANGE)

result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue
channel.queue_bind(exchange=config.RABBIT_EXCHANGE,queue=queue_name,routing_key=config.RABBIT_ROUTING_KEY)
channel.basic_consume(callback, queue=queue_name, no_ack=True)
channel.start_consuming()

