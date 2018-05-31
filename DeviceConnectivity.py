import requests, socket

class NetworkConnection:
    
    #Verifying device connection status and returning local IP
    def device_status(self):
        try:
            #Verifying IPV4 connectivity and DNS resolution
            requests.get("http://www.msftncsi.com", timeout=3)
            #Returning device IP address if connnection found
            return socket.gethostbyname(socket.gethostname())
        except requests.ConnectionError:
            pass
        return False

    def main(self):        

if __name__ == "__main__":
    DeviceConnectivity = NetworkConnection()
    DeviceConnectivity.main()
