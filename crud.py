from bottle import route, run
from bottle import get, post, request
import mysql.connector

cnx = mysql.connector.connect(user='root', password='12345', host='localhost', database='exposicion')

@route('/')
@get('/login')
def login():
        return '''
        <form action="/login" method="post">
            Username: <input name="username" type="text" />
            Password: <input name="password" type="password" />
            <input value="Login" type="submit" />
        </form>
    '''
@post('/login')
def do_login():
    username = request.forms.get('username')
    password = request.forms.get('password')
    if check_login(username, password):
        return "<p>Your login information was correct.</p>"
    else:
        return "<p>Login failed.</p>"





def check_login(username,password):
        result=False
        cursor = cnx.cursor(buffered=True)
        select=("SELECT * FROM user WHERE username='"+username+"' AND password='"+password+"'")
        cursor.execute(select)
        if not cursor.rowcount:
                result=False
        else:
                result=True
        cursor.close()
        return result

run(host='localhost', port=8080, debug=True)


