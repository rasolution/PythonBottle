import pymysql

def check_login(username, password, conection):
        result = False
        cursor = conection.cursor()
        select = ("SELECT * FROM user WHERE username='"+username+"' AND password='"+password+"'")
        cursor.execute(select)
        if not cursor.rowcount:
                result = False
        else:
                result = True
        cursor.close()
        return result


def all_products(conection):
    cursor = conection.cursor(pymysql.cursors.DictCursor)
    select = (" SELECT id,name,price FROM products ")
    cursor.execute(select)
    rows = cursor.fetchall()
    cursor.close()
    return rows

def create_product(name, price, conection):
    cursor = conection.cursor()
    select = ("INSERT INTO products (name,price) values (%s, %s)")
    product_data=(name, price)
    cursor.execute(select, product_data)
    cursor.close()
    conection.commit()