def health_check():
    return {
        "status": "ok",
        "service": "devops-project",
        "version": "1.0"
    }
if __name__ == "__main__":
    print(health_check())