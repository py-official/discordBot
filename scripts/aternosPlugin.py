from python_aternos import Client
import python_aternos


print("Try to login in the aternos's account")
print(f"Login: {login}")
print(f"Password: {password}")
try:
    account = Client.from_credentials(login, password)
except:
    print("Error of logging in aternos")
else:
    print("Successful!!\nGetting server data")
    server = account.list_servers()[0]
def Start():
    print("Try to starting minecraft server")
    try:
        server.start()
        pass
    except python_aternos.aterrors.ServerStartError:
        print("Server has already started")
        return "ErrorServerHasAlreadyStarted"
    else:
        print("Starting server")
        return "ErrorNo"

def Stop():
    try:
        server.stop()
        pass
    except:
        pass
    else:
        print("Stopping server")
        return "ErrorNoStop"


