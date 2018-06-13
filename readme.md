# Squealer Rabbitmq telegram relay bot 
*bot by [@whalepoolbtc](https://t.me/whalepoolbtc) - [https://whalepool.io](https://whalepool.io)*   

This is a simple bot to allow you to relay messages to telegram 
  

### Requirements
Install pip requirements `sudo pip3.6 install -r requirements.txt`  
  

### Setup config
`cp config.sample.yaml config.yaml`  
Edit the config.yaml file accordingly  
  
### Run
To run the subscriber, who connects to rabbit, awaits messages then sends to telegram:  
`python3.6 squealer_sub.py`  
  
To push a message to telegram, from bash type:  
```bash
python3.6 squealer_pub.py --msg="... [msg string goes here] ..." 
```
  
## squealer_pub.py arguments
| Arg | Type | Default | Required | Explanation | 
| --- | --- | --- | --- | --- | 
| msg | string | - | Yes | Message to be send to telegram | 
| chat_id | int | config.ADMIN_CHAT_ID | No | An specific chat id to msg to (ie, yourself for testing)  |
  
## To do 
- Send pictures / Picture arguments  
- Validate msg input isn't too long for telegram, spew error warning  
- Sanitise/Remove unwanted formatting characters from string that can conflict with telegram markdown parsing   
   
For more info join [@whalepoolbtc](https://t.me/whalepoolbtc) on telegram   

![Profile pic](squealer.png)    
------ 


  