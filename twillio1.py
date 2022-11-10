import temp.keys2 as keys2
from twilio.rest import Client

client = Client(keys2.accountSID,keys2.authToken)

TwilioNumber = '+17432025260'

myCellPhone = '+18326490489'

textmessage = client.messages.create(to=myCellPhone,from_=TwilioNumber,
                body="Hi there!")

print(textmessage.status)

# make a phone call

call = Client.calls.create(url="http://demo.twilio.com/docs/voice.xml",
                            to=myCellPhone,from_=TwilioNumber)