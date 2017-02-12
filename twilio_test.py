
from twilio.rest import TwilioRestClient

account_sid = "AC41c4e6078ea0396040c374f1a87ae420" # Your Account SID from www.twilio.com/console
auth_token  = "0c6d15f9f9352c85d2a54d2558906348"  # Your Auth Token from www.twilio.com/console

client = TwilioRestClient(account_sid, auth_token)

dict = {"+17325527269" : "+18478499720"}



message = client.messages.create(body="Hello from Python",
    to="+17325527268",    # Replace with your phone number
    from_="+18482246552") # Replace with your Twilio number

print(message.sid)
