import grpc

from interfaces import User_pb2_grpc, User_pb2
from prompt_toolkit import PromptSession
from prompt_toolkit.completion import WordCompleter


def start(port=8000):
    completer = WordCompleter(["list_all_users"])
    session = PromptSession(completer=completer)
    channel = grpc.insecure_channel(f"localhost:{port}")
    stub = User_pb2_grpc.UserServiceStub(channel)
    while True:
        try:
            text = session.prompt("grpc-client >>>")
        except KeyboardInterrupt:
            continue
        except EOFError:
            break

        if text == "list_all_users":
            message = User_pb2.Empty()
            response = stub.ListAllUsers(message)
            print(response)
    print("Exiting!")
