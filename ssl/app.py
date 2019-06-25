from flask import Flask, jsonify
import ssl
from werkzeug import serving

app = Flask(__name__)

context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
context.load_cert_chain("server.crt", "server.key")
#serving.run_simple("0.0.0.0", 80, app, ssl_context=context)

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    #context = ('cert.crt', 'key.key')
    app.run(host='localhost', port=5000, ssl_context=context, threaded=True, debug=True)
    #app.run(debug=True)