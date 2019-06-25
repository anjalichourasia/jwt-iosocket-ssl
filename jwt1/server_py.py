from flask import Flask, make_response, request, render_template, jsonify, redirect, url_for

import datetime
from functools import wraps
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    jwt_refresh_token_required, create_refresh_token,
    get_jwt_identity, set_access_cookies,
    set_refresh_cookies, unset_jwt_cookies
)
app = Flask(__name__)
app.config.from_object(__name__)
app.config['JWT_TOKEN_LOCATION'] = ['cookies']
app.config['JWT_ACCESS_COOKIE_PATH'] = '/'
app.config['JWT_REFRESH_COOKIE_PATH'] = '/template'
app.config['SECRET_KEY'] = "key12345"

USER_DATA = {'bro' : '12345','subham' : 'subham'}

jwt = JWTManager(app)
#mytoken = ""

@app.route('/')
def index():
   return render_template('login.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    
    if request.method == "POST":
        username = request.form['user']
        password = request.form['pass']
        for user_loop in USER_DATA:
            if user_loop == username and USER_DATA[user_loop] == password:
                # mytoken = create_access_token(identity=username, fresh=False, expires_delta=datetime.timedelta(seconds=10))
                #mytoken = jwt.encode({'user' : username, 'exp' : datetime.datetime.utcnow() + datetime.timedelta(seconds=10)}, app.config['SECRET_KEY'], algorithm='HS256')
                access_token = create_access_token(identity=username, expires_delta=datetime.timedelta(seconds=20))
                resp = jsonify({'login': True})
                set_access_cookies(resp, access_token)
                return resp, 200
                #return render_template('resource.html')
        else:
            return make_response('Username or Password is invalid')

    return render_template('login.html')

@app.route('/resource', methods=['GET'])
@jwt_required
def resource():
    #return jsonify({'currentUser' : get_jwt_identity()})
    return render_template('resource.html')

if __name__ == '__main__':
    app.run(debug=True)