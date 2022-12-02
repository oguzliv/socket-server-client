import socket
import time
import random
from message import Message


class Client:
    HOST = '127.0.0.1'
    PORT = 28059

    def __init__(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.lock_status = 0

    def start_connection(self):
        try:
            self.socket.connect((self.HOST, self.PORT))
            print(f"Client connected to {(self.HOST, self.PORT)}")
        except ConnectionRefusedError:
            print(f"Connection refused to server at {(self.HOST, self.PORT)}")

    def end_connection(self):
        try:
            self.socket.shutdown()
            self.socket.close()
        except Exception as ex:
            print(
                f"Ending Connection Exception {ex.__class__} has occured with {ex.__str__}")

    def send_message(self):
        mess = Message(imei='123456789123456', lock_status=self.lock_status,
                       battery=random.randrange(20, 90), network_value=22, charging_status=0, eol='%%')
        mess_bytes = bytes(mess.__str__(), 'utf-8')
        self.lock_status = 1 if self.lock_status == 0 else 0
        self.socket.sendall(mess_bytes)


if __name__ == '__main__':
    try:
        client = Client()
        client.start_connection()
        while True:
            try:
                client.send_message()
                time.sleep(60)
            except Exception as ex:
                print(f"Exception is {ex.__class__} with {ex.__str__}")
                break

    except KeyboardInterrupt:
        print("process interrupted with keyboard")
        client.end_connection()
