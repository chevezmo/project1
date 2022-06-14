from flask import Flask, session, request, render_template, redirect
from flask_session.__init__ import Session
from repository.database import check_user_info, create_user, get_history, get_requests, submit_request, get_stats, change_request_status

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
    session.clear()
    return redirect('http://127.0.0.1:5000/login')

@app.route('/account')
def account():
    if 'user_id' in session:
        manager = session.get('Manager',None)
        return render_template('account.html', data = manager)
    return redirect('http://127.0.0.1:5000/')

@app.route('/request', methods=['GET', 'POST'])
def reimbursement():
    if 'user_id' in session:
        if request.method == 'POST':
            submit_request(session['user_id'], request.form)
            return redirect('http://127.0.0.1:5000/account')
        return render_template('request.html')
    return redirect('http://127.0.0.1:5000/')


@app.route('/history')
def history():
    if 'user_id' in session:
        history = get_history(session['user_id'])
        stats = get_stats(session['user_id'])
        if history and stats:
            return render_template('history.html', history = history, stats = stats)
        return render_template('history.html')
    return redirect('http://127.0.0.1:5000/')

@app.route('/approval', methods=['GET', 'POST'])
def approval():
    if 'user_id' in session:
        if session['manager']:
            if request.method == 'POST':
                if request.form.get('approve'):
                    change_request_status(request.form.get('approve'), 'Approved')
                if request.form.get('reject'):
                    change_request_status(request.form.get('reject'), 'Rejected')
            data = get_requests(session['user_id'])
            if data:
                return render_template('approval.html', data = data)
            return render_template('approval.html')
        return redirect('http://127.0.0.1:5000/account')
    return redirect('http://127.0.0.1:5000/')

@app.route('/login' , methods=['GET', 'POST'])
def confirm_user():
    if request.method == 'POST':
        if check_user_info(request.form):
            create_user(request.form)
            return redirect('http://127.0.0.1:5000/account')
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)