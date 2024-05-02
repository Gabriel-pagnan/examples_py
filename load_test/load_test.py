import time
import requests
import threading

def send_request():
    endpoint = 'http://localhost:8080/api/lkjahsd'

    try:
        response = requests.get(endpoint)
        print(f'Status code: {response.status_code}')
    except Exception as error:
        print(str(error))

def load_test(num_requests: int, interval: int):
    for _ in range(num_requests):
        send_request()
        time.sleep(interval)

num_requests = 1000
interval = 0.01 #seconds

threads = []
for _ in range(10):
    thread = threading.Thread(
        target=load_test, 
        args=(num_requests, interval)
    )
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print('Load test completed.')