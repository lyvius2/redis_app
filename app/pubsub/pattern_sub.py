import redis
import threading

r = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)

patten = 'redis_*'

pubsub = r.pubsub()
pubsub.psubscribe(patten)

def listen_for_pmessages():
    for message in pubsub.listen():
        if message['type'] == 'pmessage':
            print(f"Pattern: {message['pattern']}, Channel: {message['channel']}, Message: {message['data']}")
            
thread = threading.Thread(target=listen_for_pmessages)
thread.start()
