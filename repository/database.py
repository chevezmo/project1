from repository.connection import get_connection
def check_user_info(form):
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

