from zeus import client
from flask import Flask
import random
import datetime

app = Flask(__name__)


class ZeusAlert():
    def __init__(self):
        self.api = client.ZeusClient(os.getenv("ZEUS_TOKEN"),
                                     os.getenv("ZEUS_API_HOST"))
        self.log = os.getenv("ZEUS_KEY")
        self.key = os.getenv("ZEUS_KEY")

    def _send_to_zeus(self, msg):
        logs = [{self.key: msg}]
        self.api.sendLog(self.log, logs)

    def trigger(self, alertdata):
        self._send_to_zeus(alertdata)



@app.route("/")
def hello():
    zeus = ZeusAlert()
    timestamp = datetime.datetime.now().time()
    msg = "Secret Message is %s" % str(random.randint(1,100))
    zeus.trigger(msg)
    return msg


if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')
