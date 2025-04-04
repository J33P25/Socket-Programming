import socket
import threading
import os
import mimetypes
from datetime import datetime

# Server Configuration
HOST = 'localhost'
PORT = 8080
ROOT_DIR = "www"

# Handle Client Requests
def handle_client(client_connection):
    try:
        request = client_connection.recv(1024).decode('utf-8')
        print(f"Request:\n{request}")

        if not request:
            return

        # Parse the HTTP Request
        request_line = request.splitlines()[0]
        method, path, _ = request_line.split()

        print(f"Requested resource: {path}")

        # Default file for root path "/"
        if path == "/":
            path = "/index.html"

        # Build file path
        file_path = os.path.join(ROOT_DIR, path.strip("/"))

        # Serve Static Files for GET Requests
        if method == "GET":
            try:
                if path == "/datetime":
                    response_body = f"<h1>{datetime.now()}</h1>".encode('utf-8')
                    response_header = "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n"
                else:
                    content_type, _ = mimetypes.guess_type(file_path)
                    with open(file_path, "rb") as file:
                        response_body = file.read()
                    response_header = f"HTTP/1.1 200 OK\r\nContent-Type: {content_type or 'text/html'}\r\n\r\n"
            except FileNotFoundError:
                response_body = b"<h1>404 Not Found</h1>"
                response_header = "HTTP/1.1 404 Not Found\r\nContent-Type: text/html\r\n\r\n"

        # Handle POST Requests
        elif method == "POST":
            if path == "/submit_form":
                # Parse POST Data
                content_length = int(request.split('Content-Length: ')[1].split("\r\n")[0])
                post_data = request[-content_length:]  # Extract POST data from the request body
                print(f"Received POST Data: {post_data}")

                # Respond to POST
                response_body = f"<h1>Form submitted successfully!</h1><p>Received Data: {post_data}</p>".encode('utf-8')
                response_header = "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n"
            else:
                response_body = b"<h1>404 Not Found</h1>"
                response_header = "HTTP/1.1 404 Not Found\r\nContent-Type: text/html\r\n\r\n"

        else:
            response_body = b"<h1>405 Method Not Allowed</h1>"
            response_header = "HTTP/1.1 405 Method Not Allowed\r\nContent-Type: text/html\r\n\r\n"

        # Send the Response
        client_connection.sendall(response_header.encode() + response_body)

    except Exception as e:
        print(f"Error: {e}")
    finally:
        client_connection.close()

# Main Server Loop
def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(5)
    print(f"Serving HTTP on {HOST}:{PORT} (Root Directory: {ROOT_DIR})")

    try:
        while True:
            client_connection, client_address = server_socket.accept()
            print(f"New connection from {client_address}")
            threading.Thread(target=handle_client, args=(client_connection,)).start()
    except KeyboardInterrupt:
        print("\nShutting down the server...")
    finally:
        server_socket.close()

if __name__ == "__main__":
    main()
