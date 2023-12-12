#!/bin/bash
#Compile protos into server folder
python -m grpc_tools.protoc -I./protos --python_out=./server --pyi_out=./server --grpc_python_out=./server ./protos/*.proto
#Compile protos into client folder
python -m grpc_tools.protoc -I./protos --python_out=./client --pyi_out=./client --grpc_python_out=./client ./protos/*.proto
