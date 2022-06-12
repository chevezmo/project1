from flask import Flask, request, render_template, redirect
from repository.database import check_user_info, create_user, get_history, submit_request

app = Flask(__name__)

@app.route('/')
def login():
    return redirect('http://127.0.0.1:5000/login')

@app.route('/account')
def account():
    return render_template('account.html')

@app.route('/request', methods=['GET', 'POST'])
def reimbursement():
    if request.method == 'POST':
        submit_request(current_user, request.form)
        return redirect('http://127.0.0.1:5000/account')
    return render_template('request.html')

@app.route('/history')
def history():
    data = get_history(current_user)
    return render_template('history.html', data = data)

@app.route('/approval')
def approval():
    return render_template('approval.html')

@app.route('/login' , methods=['GET', 'POST'])
def confirm_user():
    if request.method == 'POST':
        if check_user_info(request.form):
            global current_user
            current_user = create_user(request.form)
            return redirect('http://127.0.0.1:5000/account')
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)