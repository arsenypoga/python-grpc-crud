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

To generate the stub code run
```bash
protoc ./User.proto --python_out=./interfaces
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