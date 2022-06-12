from repository.connection import get_connection
from models.user import User

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

def create_user(form) -> User:
    username = form.get('username')
    user_id, first_name, last_name, manager = get_user_info(username)
    new_User = User(user_id, username, first_name, last_name, manager)
    return new_User

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


def submit_request(user: User, form):
    description = form.get('description')
    amount = form.get('amount')
    expense_type = form.get('category')
    try:
        connection = get_connection()
        cursor = connection.cursor()

        qry = "INSERT INTO requests VALUES (default, %s, %s, %s, %s, %s);"
        cursor.execute(qry,(user.user_id, description, amount, expense_type, 'Pending'))
        connection.commit()
    except:
        connection.rollback()
        print("Unable to submit request")
    finally:
        if connection is not None:
            connection.close()

def get_history(user: User):
    try:
        connection = get_connection()
        cursor = connection.cursor()

        qry = f"SELECT * FROM requests WHERE user_id = '{user.user_id}';"
        cursor.execute(qry)
        records = cursor.fetchall()
        if records:
            return records
    except:
        print("No records available")
    finally:
        if connection is not None:
            connection.close()