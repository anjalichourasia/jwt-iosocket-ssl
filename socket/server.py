from flask import Flask, render_template
from flask_socketio import send, SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = '12345'
socketio = SocketIO(app)

@socketio.on('message')
def message_handle(msg):
    print("Message is "+msg)
    send(msg, broadcast=True)

@app.route('/')
def load():
    return render_template('index.html')

if __name__ == '__main__':
    socketio.run(app, debug=True)