from http.server import HTTPServer

from peer_session import upserver

host_name = "localhost"
server_port = 8080

if __name__ == "__main__":
    web_server = HTTPServer((host_name, server_port), upserver.UpServer)
    print(f"Server listening http://{host_name}:{server_port}")

    try:
        web_server.serve_forever()
    except KeyboardInterrupt:
        pass

    web_server.server_close()
    print("Server stopped.")
