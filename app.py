import redis
import requests

redis_client = redis.Redis(host='localhost', port=6379)

def handle_new_information(channel, data):
    # Extract relevant data from Redis message
    # Prepare data for sending to REST API
    # ...

    # Send data to REST API
    response = requests.post('http://example.com/api/new-information', json=data)
    if response.status_code != 200:
        # Handle error
        pass

redis_client.subscribe(**{'new-information': handle_new_information})
