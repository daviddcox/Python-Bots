# we import the Twilio client from the dependency we just installed
from twilio.rest import Client

# the following line needs your Twilio Account SID and Auth Token
client = Client("ACd94f02a9cc549d19aa241af4b0da8856", "f87664f1f3b65c3e250f49dc65c0cb83")

# change the "from_" number to your Twilio number and the "to" number
# to the phone number you signed up for Twilio with, or upgrade your
# account to send SMS to any phone number
client.messages.create(to="+13179228684",
                       from_="+12344071982",
                       body="Hey")
