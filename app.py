from flask import Flask, session
from flask_session.__init__ import Session
from routes.routes import get_login_page, get_account, get_submit_requests, get_history_page, get_approval_page, confirm_user_account

app = Flask(__name__)
SESSION_TYPE = 'filesystem'
app.config.from_object(__name__)
Session(app)

@app.route('/set/')
def set():
    session['key'] = 'value'
    return 'ok'

@app.route('/get/')
def get():
    return session.get('key', 'not set')

@app.route('/')
def login():
    return get_login_page()

@app.route('/account')
def account():
    return get_account()

@app.route('/request', methods=['GET', 'POST'])
def reimbursement():
    return get_submit_requests()

@app.route('/history', methods = ['GET', 'POST'])
def history():
    return get_history_page()

@app.route('/approval', methods=['GET', 'POST'])
def approval():
    return get_approval_page()

@app.route('/login' , methods=['GET', 'POST'])
def confirm_user():
    return confirm_user_account()

if __name__ == '__main__':
    app.run(debug=True)