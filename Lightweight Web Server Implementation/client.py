import socket

# Client Configuration
SERVER_HOST = 'localhost'
SERVER_PORT = 8080

def main():
    # Prompt the user for the resource
    resource = input("Enter the resource to request (e.g., /index.html, /about.html, /datetime): ")

    # Create a socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((SERVER_HOST, SERVER_PORT))

    # Handle GET or POST requests
    if resource == "/submit_form":
        data = input("Enter form data to submit (e.g., name=John&age=30): ")
        post_request = f"POST {resource} HTTP/1.1\r\nHost: {SERVER_HOST}\r\nContent-Length: {len(data)}\r\n\r\n{data}"
        client_socket.sendall(post_request.encode())
        response = client_socket.recv(4096).decode('utf-8')
        print("Server Response:\n", response)
    else:
        # Send GET Request
        request = f"GET {resource} HTTP/1.1\r\nHost: {SERVER_HOST}\r\n\r\n"
        client_socket.sendall(request.encode())
        response = client_socket.recv(4096).decode('utf-8')
        print("Server Response:\n", response)

    # Close the connection
    client_socket.close()

if __name__ == "__main__":
    main()
