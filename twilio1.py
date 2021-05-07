from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC3b46312e72402fee71d0d0625a1d10b4"
# Your Auth Token from twilio.com/console
auth_token  = "8caf4f4e4725750c00ff96a48b6dde8d"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+919916304046", 
    from_="+13344633400",
    body="Hello from Python!")

print(message.sid)
