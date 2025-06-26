import os
from twilio.rest import Client

def test_twilio_call():
    # Set your credentials here or use environment variables for security
    account_sid = "AC49ad2ec74c10420cce73eff4f9a2a4c1"
    auth_token = "e958a59722ece628fcbe90b24eb6d361"
    client = Client(account_sid, auth_token)

    call = client.calls.create(
        url="http://demo.twilio.com/docs/voice.xml",
        to="+918523024169",
        from_="+16202979736"
    )

    print("Call SID:", call.sid)
    return call.sid

if __name__ == "__main__":
    test_twilio_call()
