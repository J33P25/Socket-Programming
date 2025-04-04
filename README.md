# Lightweight Web Server Implementation

## Project Overview

This project demonstrates the design and implementation of a lightweight HTTP web server capable of handling basic **GET** and **POST** requests. 
The server delivers static HTML content, serves other files (e.g., CSS, JavaScript, images), and optionally handles dynamic responses. 
This implementation was developed to understand HTTP protocols, socket programming, and the client-server architecture.

---

## Features:
- **GET Requests**: Retrieve static files (e.g., HTML, CSS, JavaScript) from the server.
- **POST Requests**: Submit form data to the server for processing.
- **Dynamic Responses**: The server can return the current date and time for specific requests (e.g., `/datetime`).
- **Error Handling**: Returns 404 for not found resources and 405 for unsupported methods.
- **Multi-threaded**: Concurrent processing of multiple client requests using threading.

---

## Server-Side Implementation

1. **Socket Setup**:
   - The server is implemented using Python’s `socket` library.
   - The server creates a TCP socket (`AF_INET`, `SOCK_STREAM`), binds to the specified `localhost` and port `8080`, and listens for incoming connections.

2. **Request Handling**:
   - The server processes client requests in a multithreaded manner using Python's `threading` module, allowing multiple simultaneous connections.
   - It listens for `GET` and `POST` requests:
     - **GET**: The server serves static files from the `www/` directory.
     - **POST**: The server processes form data sent from the client and returns a response.
   - Dynamic content (e.g., current date and time) is generated for specific endpoints (e.g., `/datetime`).
   - Proper error handling is implemented:
     - Returns `404 Not Found` for invalid paths.
     - Returns `405 Method Not Allowed` for unsupported HTTP methods.

3. **Multi-threading**:
   - Each incoming client connection is handled in a separate thread, allowing the server to handle multiple requests concurrently.

---

## Client-Side Implementation

1. **Socket Connection**:
   - The client creates a socket and connects to the server’s `localhost:8080`.
   
2. **Request Construction**:
   - The user is prompted to input the desired resource (e.g., `/index.html` or `/datetime`).
   - A valid HTTP `GET` or `POST` request is constructed and sent to the server.

3. **Response Handling**:
   - The client receives the server’s response, decodes it, and prints the response body and headers.

---

## Requirements:
- **Python 3.x**

### External Libraries:
- Python's standard `socket`, `threading`, and `mimetypes` modules are used in this project, so no additional libraries are required.

---

## Running the Server

1. Clone the repository:
   ```bash
   git clone https://github.com/J33P25/Socket-Programming.git
