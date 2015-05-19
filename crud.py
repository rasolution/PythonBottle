from bottle import route, run,redirect,get, post, request,template,response
from functions import check_login,all_products
from conection import conectar
from json import dumps

conection=conectar()

@route('/')

@get('/login')
def login():
    return template('Templates/index.tpl')

@post('/login')
def do_login():
    username = request.forms.get('username')
    password = request.forms.get('password')
    if check_login(username, password, conection):
        redirect("/products")
    else:
        return "<p>Login failed.</p>"


@get('/products')
def products():
    return template('Templates/products.tpl')

@get('/products.json')
def products():
    table=all_products(conection)
    response.content_type = 'application/json'
    return dumps(table)

@get('/products/create')
def products_create():
    return "create producto"

run(host='localhost', port=8080, debug=True)


