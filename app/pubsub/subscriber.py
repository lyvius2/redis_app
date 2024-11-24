import redis
import threading

r = redis.Redis(host='redis-stack', port=6379, db=0, decode_responses=True)

pubsub = r.pubsub()
pubsub.subscribe('redis_channel')

def handle_message(message):
    print(f"Received message: {message['data']}")
    
def listen_for_message():
    for message in pubsub.listen():
        if message['type'] == 'message':
            handle_message(message)
            
thread = threading.Thread(target=listen_for_message)
thread.start()
