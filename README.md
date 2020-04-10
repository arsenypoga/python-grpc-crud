# GRPC example CRUD application in Python

This is a basic skeleton for the GRPC application in python. Improvements tbd.

## Installation
To install this application, at first ensure that you have python3 and pip. After doing so run 
```bash
pip install pipenv
```
to install pipenv virtual environment manager.

With that out of the way, install the project dependencies with
```bash
pipenv install
```

The building of the python protobuf code is ignored on purpose, no need to upload same code twice.
To generate the code needed, ensure that you have protoc compiler installer, or install it with pip using the `grpcio-tools` package.

To generate the stub code run. This generates both message classes and the Client/Server classes.
```bash
python -m grpc_tools.protoc -I. --python_out=./interfaces --grpc_python_out=./interfaces ./User.proto
```
Which will generate the `User_pb2.py` code in the `interfaces` folder.

## Running the code
Every new terminal session you have to load the virtual environment with 
```bash
pipenv shell
```

After doing so you can run the code with 
```bash
python ./start.py {client, server} # With either client or server parameter to start it.
```

The server will simply run on a given port. 
The client code starts a shell session with command autocompletion.
Command list is:
 * list_all_users

## Possible errors

For whatever reason python might not like the the interface code is generated, which can cause an error like `No module named 'User_pb'`. To fix this, open the file in question (User_pb2_grpc.py) and edit the import line to `from . import User_pb2 as User__pb2`