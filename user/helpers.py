from decouple import config
import requests

def send_smscode(code,phone):
    apikey = config("apikey")
    header = {
        'apikey': apikey,
    }
    data = {
        "message":code,
        "receptor": phone,
        "linenumber":"10008566"
    }
    response = requests.post("https://api.ghasedak.me/v2/sms/send/simple",data=data,headers=header)