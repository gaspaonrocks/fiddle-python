#!/usr/bin/env python3
import time
from http.server import HTTPServer
from server import Server

HOST_NAME = 'localhost'
PORT_NUMBER = 8765

if __name__ == '__main__':
    httpd = HTTPServer((HOST_NAME, PORT_NUMBER), Server)
    print(time.asctime(), f'Server UP - {HOST_NAME}:{PORT_NUMBER}')
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    print(time.asctime(), f'Server DOWN - {HOST_NAME}:{PORT_NUMBER}')