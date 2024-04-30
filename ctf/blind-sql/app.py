from flask import Flask, render_template, request
import pymysql

conn = pymysql.connect(host='127.0.0.1', user='root', passwd='123', db='ctf')
cursor = conn.cursor()

app = Flask(__name__)

@app.route('/', methods=['GET'])
def login():
    id = request.args.get('id')
    passwd = request.args.get('passwd')
    
    if id is None or passwd is None:
        return render_template('login.html')
    
    cursor.execute(f"SELECT * FROM users WHERE id='{id}' and passwd='{passwd}'")
    
    user = cursor.fetchone()
    if user[0] == 'admin':
        return "Hello, admin!"
    elif user[0] == 'guest':
        return "Hello, guest!"
    else:
        return render_template('login.html')
    
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)