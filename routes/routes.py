from flask import session, request, render_template, redirect
from repository.database import check_user_info, create_user, get_history, get_requests, submit_request, get_stats, change_request_status

def get_login_page():
    session.clear()
    return redirect('http://127.0.0.1:5000/login')

def get_account():
    if 'user_id' in session:
        manager = session.get('manager',None)
        return render_template('account.html', manager = manager, name = session['name'])
    return redirect('http://127.0.0.1:5000/')

def get_submit_requests():
    if 'user_id' in session:
        if request.method == 'POST':
            submitted = submit_request(session['user_id'], request.form)
            return render_template('request.html', submitted = submitted)               
        return render_template('request.html')
    return redirect('http://127.0.0.1:5000/')

def get_history_page():
    if 'user_id' in session:
        if request.method == 'POST':
            if request.form.get('cancel'):
                change_request_status(request.form.get('cancel'), 'Cancelled')
        history = get_history(session['user_id'])
        stats = get_stats(session['user_id'])
        if history and stats:
            return render_template('history.html', history = history, stats = stats)
        return render_template('history.html')
    return redirect('http://127.0.0.1:5000/')

def get_approval_page():
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

def confirm_user_account():
    if request.method == 'POST':
        if check_user_info(request.form):
            create_user(request.form)
            return redirect('http://127.0.0.1:5000/account')
        return render_template('login.html', data = False)
    return render_template('login.html')