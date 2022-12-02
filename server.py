import socket
import pprint
from message import Message
from mongo_driver import Mongo


class Server:
    __HOST = '127.0.0.1'
    __PORT = 28059
    __conn = None
    __addr = None
    __mongo = None

    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__mongo = Mongo()

    def start_server(self):
        self.sock.bind((self.__HOST, self.__PORT))

        print(f"Listening {(self.__HOST, self.__PORT)}")

        self.sock.listen()

    def accept_connection(self):
        try:
            self.__conn, self.__addr = self.sock.accept()
        except Exception as ex:
            print(f"Exception {ex.__class__} with {ex.__str__()}")
            self.sock.close()

    def receive_message(self):
        data = self.__conn.recv(1024)
        obj = data.decode('utf-8').split(',')
        if data:
            try:
                received_message = Message(
                    obj[0], obj[1], obj[2], obj[3], obj[4], '%%').objectify_message()
                print("rec : ", received_message)
                try:
                    self.__mongo.connect_database()
                    all_messages = self.__mongo.get_all_messages()
                    print("all messages : ", all_messages)
                    print("total messages : ", len(all_messages))
                    if len(all_messages) == 0:
                        self.__mongo.insert_data(
                            received_message)
                    else:
                        self.__mongo.update_message(
                            received_message['imei'], received_message)

                except Exception as ex:
                    print(
                        f"MongoDB Exception {ex.__class__} with {ex.__str__()}")
                finally:
                    self.__mongo.close_connection()
            except Exception as ex:
                print(
                    f"Receiving Message Exception {ex.__class__} with {ex.__str__()}")
        else:
            return
        return data

    def get_conn(self):
        return self.__conn

    def get_adddress(self):
        return self.__addr

    def end_connection(self):
        try:
            self.sock.shutdown(socket.SHUT_RD)
            self.sock.close()
        except Exception as ex:
            print(
                f"Close Connection Exception {ex.__class__} with {ex.__str__()}")
            self.sock.close()


if __name__ == '__main__':
    data = ""
    server = Server()
    server.start_server()
    while True:
        try:
            server.accept_connection()
            with server.get_conn():
                print("conn in with/while : ", server.get_conn())
                while True:
                    try:
                        data = server.receive_message()
                        if not data:
                            break
                    except Exception as ex:
                        print(
                            f"Message Exception is {ex.__class__} with {ex.__str__}")

        except KeyboardInterrupt:
            print("process interrupted with keyboard")
            server.end_connection()
            break
