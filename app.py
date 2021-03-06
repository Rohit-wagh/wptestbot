from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/sms", methods=['POST'])
def sms_reply():
    """Respond to incoming calls with a simple text message."""
    # Fetch the message
    msg = request.form.get('Body')

    if(msg=='hi'):

    # Create reply
        resp = MessagingResponse()
        resp.message("You said: {}".format('Hello how are you'))

        return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
