#!/bin/bash

# NOTE: This script starts the server. To kill the server, either use ctrl+C in bash window or:
# netstat -ano | findstr :<Your Port Number>
# taskkill /F /PID <The Given PID>

# Set default values for port and host
host="localhost"
port="50051"

# Check if they are provided as arguments
if [ $# -eq 2 ]; then
    host="$1"
    port="$2"
elif [ $# -eq 1 ]; then
    host="$1"
fi

# Start the server with the host and port
python -u ./parallelreddit_server.py "$host" "$port" 

# Keep the window open
$SHELL

