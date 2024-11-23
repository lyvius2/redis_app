import redis

r = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)

pubsub = r.pubsub()

while True:
    message = input("Enter message to publish (or 'exit' to quit): ")
    if message.lower() == 'exit':
        break
    r.publish('redis_channel', message)
    
pubsub.close()
