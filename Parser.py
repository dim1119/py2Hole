import urllib.request
import json
import fetchFile    #importing fileFile to get the functuins
contents = urllib.request.urlopen("http://pi.hole/admin/api.php").read()    #reading the contents of the json page

#getting seperately the content of what we want and using functions we return it to the main function

def getClients():
    return json.loads(contents)['unique_clients']

def getStatus():
    return json.loads(contents)['status']

def getPrivacylevel():
    return json.loads(contents)['privacy_level']

def getPercentage():
    return json.loads(contents)['ads_percentage_today']

def disable():
    cred=fetchFile.getApiKey().decode('ascii')          #using the API key to turn on or off the server
    if cred!=0:
        return urllib.request.urlopen("http://pi.hole/admin/api.php?disable&auth="+cred).read()
    else:
        exit()

def enable():
    cred=fetchFile.getApiKey().decode('ascii')
    if cred!=0:
        return urllib.request.urlopen("http://pi.hole/admin/api.php?enable&auth="+cred).read()
    else:
        exit()

#dictionary for each function
FUNCTION_MAP={
    'clients':getClients,
    'status':getStatus,
    'privacy':getPrivacylevel,
    'percentage':getPercentage,
    'disable':disable,
    'enable':enable
}
