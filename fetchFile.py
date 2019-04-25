import base64


# read the file, decode base64, then return it to the enable()/disable()
def getApiKey():
    try:
        raw = open('ApiKey.txt', 'r')
        base = (raw.readline()).split(':')[1]
        raw.close()
        return base64.b64decode(base)

    except:
        print("File not accessible")
        return 0


# bugs-----\/-----\/----
def createFile():
    try:
        raw = open('ApiKey.txt', 'r')
        raw.close()
    except:
        raw = open('ApiKey.txt', 'w')
        usrInput = input("Enter your api key and press enter: ")
        raw.write("apikey:" + base64.b64encode(usrInput).encode('ascii'))
        raw.close()


if __name__ == "__main__":
    createFile()
