# /usr/bin/env python
# Download the twilio-python library from twilio.com/docs/libraries/python
import os
from twilio.rest import Client

# Find these values at https://twilio.com/user/account
# To set up environmental variables, see http://twil.io/secure
account_sid = '[account_sid]'
auth_token = '[auth_token]'

client = Client(account_sid, auth_token)

client.api.account.messages.create(
    to="[number to recibe the sms]",
    from_="[number that gave the web]",
    body="[Message you want to send]")
