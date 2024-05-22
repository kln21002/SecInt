from locust import User, task, between, events
import socket
import time

class TcpUser(User):
    wait_time = between(1, 2.5)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def on_start(self):
        self.client.connect(('10.120.48.195', 4000))

    def on_stop(self):
        self.client.close()

    @task
    def send_message(self):
         message = 'simple message'
         start_time = time.time()
         self.client.sendall(message.encode())
         while True:
             data = self.client.recv(1024)
             if data:
                 break
         response_time = time.time() - start_time
         self.environment.events.request.fire(request_type="tcp", name="send_message", response_time=response_time*1000, response_length=0, context={}, exception=None)