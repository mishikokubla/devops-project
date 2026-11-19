import socket

def health_check():
    return {

        "status": "healthy",
        "service": "devops-project",
        "version": "1.1",
        "hostname": socket.gethostname(),
	"environment": "development"
    }
if __name__ == "__main__":
    print(health_check())
