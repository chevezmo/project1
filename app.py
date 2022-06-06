from flask import Flask, request, render_template, redirect, url_for
from repository.database import check_user_info

app = Flask(__name__)

@app.route('/')
def login():
    return redirect('http://127.0.0.1:5000/login')

@app.route('/request')
def reimbursement():
    return render_template('request.html')

@app.route('/history')
def history():
    return render_template('history.html')

@app.route('/approval')
def approval():
    return render_template('approval.html')

@app.route('/login' , methods=['GET', 'POST'])
def confirm_user():
    if request.method == 'POST':
        if check_user_info(request.form):
            return render_template('account.html')
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)