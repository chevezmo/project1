from repository.connection import get_connection
from flask import session

def check_user_info(form) -> bool:
    username = form.get('username')
    password = form.get('password')
    connection = get_connection()
    cursor = connection.cursor()

    qry = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}';"
    cursor.execute(qry)
    record = cursor.fetchone()
    connection.close()
    if record:
        return True
    return False

def create_user(form):
    username = form.get('username')
    user_id, first_name, last_name, manager = get_user_info(username)
    session['user_id'] = user_id
    session['first_name'] = first_name
    session['last_name'] = last_name
    session['manager'] = manager

def get_user_info(username):
    try:
        connection = get_connection()
        cursor = connection.cursor()
        
        qry = f"SELECT user_id, first_name, last_name, manager FROM users WHERE username = '{username}';"
        cursor.execute(qry)
        record = cursor.fetchone()
        if record:
            return record
    except:
        print("Unable to retrieve user_id")
    finally:
        if connection is not None:
            connection.close()


def submit_request(user_id, form):
    description = form.get('description')
    amount = form.get('amount')
    expense_type = form.get('category')
    try:
        connection = get_connection()
        cursor = connection.cursor()

        qry = "INSERT INTO requests VALUES (default, %s, %s, %s, %s, %s);"
        cursor.execute(qry,(user_id, description, amount, expense_type, 'Pending'))
        connection.commit()
    except:
        connection.rollback()
        print("Unable to submit request")
    finally:
        if connection is not None:
            connection.close()

def get_history(user_id):
    try:
        connection = get_connection()
        cursor = connection.cursor()

        qry = f"SELECT * FROM requests WHERE user_id = '{user_id}';"
        cursor.execute(qry)
        records = cursor.fetchall()
        if records:
            return records
    except:
        print("No records available")
    finally:
        if connection is not None:
            connection.close()

def get_requests(user_id):
    try:
        connection = get_connection()
        cursor = connection.cursor()

        qry = f"""
        SELECT users.first_name, users.last_name, requests.description, requests.amount, requests.expense_type, requests.status, requests.request_id
        FROM requests
        JOIN users ON requests.user_id = users.user_id
        WHERE requests.user_id <> '{user_id}';
        """
        cursor.execute(qry)
        records = cursor.fetchall()
        if records:
            return records
    except:
        print("No records available")
    finally:
        if connection is not None:
            connection.close()

def get_stats(user_id):
    try:
        connection = get_connection()
        cursor = connection.cursor()

        qry = f"""
        SELECT
        COUNT(status) AS "Total Requests",
        SUM(CASE WHEN status = 'Pending' THEN 1 ELSE 0 END) AS "Total Pending",
        SUM(CASE WHEN status = 'Approved' THEN 1 ELSE 0 END) AS "Total Approved",
        SUM(CASE WHEN status = 'Rejected' THEN 1 ELSE 0 END) AS "Total Rejected",
        SUM(CASE WHEN status = 'Cancelled' THEN 1 ELSE 0 END) AS "Total Cancelled"
        FROM requests
        WHERE user_id = '{user_id}';
        """

        cursor.execute(qry)
        stats = cursor.fetchall()
        if stats:
            return stats
    except:
        print("No stats available")
    finally:
        if connection is not None:
            connection.close()