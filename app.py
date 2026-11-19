import socket

def health_check():
    return {
        "status": "ok",
        "service": "devops-project",
        "version": "1.1",
        "hostname": socket.gethostname()
    }
if __name__ == "__main__":
    print(health_check())