import datetime
import json
import requests
import pandas as pd
from copy import deepcopy

from twilio.rest import Client


def twi(mess):
    account_sid = "<ENtery your account SID for TWILIO>"
    auth_token  = "<ENTER YOUR account token for TWILIO>"
    client = Client(account_sid, auth_token)
    message = client.messages.create(to="<To be senyt to>", from_="<TWILIO_NUMBER>",body=mess)


#Pincode where you want to check for vaccine
PINCODE = "REPLACE with PINCODE"


base = datetime.datetime.today()
date_list = [base + datetime.timedelta(days=x) for x in range(1)]
date_str = [x.strftime("%d-%m-%Y") for x in date_list]


final_df = None
for INP_DATE in date_str:
    URL = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin?pincode={}&date={}".format(PINCODE, INP_DATE)
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    print(URL)
    result=(requests.get(URL,headers=headers))
    print(result.content.decode())
    response = requests.get(URL, headers = headers)
    print(response.content.decode())
    data = json.loads(response.content)


df = pd.json_normalize(data['sessions'])
print(df)
df = df.drop(['center_id','state_name','from','to','lat','block_name','long','session_id','slots','fee','district_name'],axis=1)
df = df[df.columns.dropna()]

df_1 = df.loc[df['min_age_limit'] == "ENTER THE AGE LIMIT WITHOUT QUOTES"]



if df_1.empty:
    print("No center")

else:
    print(df_1.astype(str))
    twi("sample message to see the error")







    

