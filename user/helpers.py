from json import loads
from decouple import config
import requests
from .models import Subscription

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


def pay_with_idpay(order_id,user):
        subscription = Subscription.objects.get(id=order_id)
        headers = {
        "X-API-KEY":config("IDPAY_APIKEY",cast=str),
        "X-SANDBOX": "true",    
        }
        data = {
            "order_id":subscription.id,
            "phone":user.phone,
            "amount":subscription.price,
            "callback":"http://localhost:8000/api/subscription/buy/",
        }
        response = requests.post("https://api.idpay.ir/v1.1/payment",headers=headers, json=data)
        dic = loads(response.content)
        return dic