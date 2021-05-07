import datetime
import json
import requests
import pandas as pd
from copy import deepcopy

from twilio.rest import Client


def twi(mess):
    account_sid = "AC3b46312e72402fee71d0d0625a1d10b4"
    auth_token  = "8caf4f4e4725750c00ff96a48b6dde8d"
    client = Client(account_sid, auth_token)
    message = client.messages.create(to="+919916304046", from_="+13344633400",body=mess)



PINCODE = "273001"


base = datetime.datetime.today()
date_list = [base + datetime.timedelta(days=x) for x in range(1)]
date_str = [x.strftime("%d-%m-%Y") for x in date_list]


final_df = None
for INP_DATE in date_str:
    #URL = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/calendarByPin?pincode={}&date={}".format(PINCODE, INP_DATE)
    URL = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin?pincode={}&date={}".format(PINCODE, INP_DATE)
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    #print(URL)
    #result=(requests.get(URL,headers=headers))
    #print(result.content.decode())
    response = requests.get(URL, headers = headers)
    #print(response.content.decode())
    data = json.loads(response.content)


df = pd.json_normalize(data['sessions'])
print(df)
df = df.drop(['center_id','state_name','from','to','lat','block_name','long','session_id','slots','fee','district_name'],axis=1)
df = df[df.columns.dropna()]

df_1 = df.loc[df['min_age_limit'] == 45]

if df_1.empty:
    print("No center")

else:
    print(df_1.astype(str))
    twi("sample message to see the error")






'''print(data['sessions'])
Center_Name = data['sessions'][0]['center_id'])
Center_Address = 
Age =
Slots = 

for i in data:
    print("Center:",i['name'])
    print("Address:",i['address'])
    print("Slots:",i['slots'])
'''






    

