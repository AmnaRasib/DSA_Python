import queue
import time

request_queue=queue.Queue()

def addRequests(request):
    print(f"Request Received: {request}")
    request_queue.put(request)
def Process_requests():
    while not request_queue.empty():
        request=request_queue.get()
        print(f"Processing Requests: ",request)
        request_queue.task_done()

requests = ["User1", "User2", "User3", "User4"]
for req in requests:
    addRequests(req)
# Process all requests
print("\nProcessing requests...\n")
Process_requests()
print("\nAll requests processed.")