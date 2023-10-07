import socket

def check_internet():
    try:
        # Connect to Google DNS to check internet connection status
        socket.create_connection(("8.8.8.8", 53))
        return True
    except OSError:
        pass
    return False
