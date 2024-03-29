from flask import Flask, request, render_template, session
from secret import ADMIN_COOKIE, FLAG
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

app = Flask(__name__)
app.secret_key = 'this is secret key'

def read_url(url):
    
    try:
        service = Service(executable_path="/chromedriver")
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        options.add_argument('--no-sandbox')
        
        driver = webdriver.Chrome(service=service, options=options)
        driver.implicitly_wait(3)
        driver.set_page_load_timeout(3)
        driver.get("http://127.0.0.1:8000/")
        driver.add_cookie({"name":"user", "value":f"{ADMIN_COOKIE}"})
        driver.get(url)
    except Exception as e:
        driver.quit()
        print(e)
        return False
    driver.quit()
    return True


@app.route('/', methods=['GET'])
def index():
    ret_message = None
    user = request.cookies.get('user')
    
    if user and user == ADMIN_COOKIE:
        ret_message = f'Hello, admin! {FLAG}'
    else:
        ret_message = 'Hello, guest!'
        
    return render_template('index.html', memo=ret_message)
        
@app.route("/vuln")
def vuln():
    param = request.args.get("param", "/vuln?param=your input")
    return param

@app.route("/req", methods=["GET", "POST"])
def flag():
    if request.method == "GET":
        return render_template("req.html")
    elif request.method == "POST":
        param = request.form.get("param", '')
        if not read_url(f'http://127.0.0.1:8000/vuln?param=f{param}'):
            return '<script>alert("wrong??");history.go(-1);</script>'

        return '<script>alert("good");history.go(-1);</script>'

@app.route("/test", methods=['GET', 'POST'])
def test():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        if username == 'admin' and password == '123':
            session['user'] = 'admin'
    
    if 'user' in session:
        user = session['user']
    else:
        user = 'guest'
    
    return render_template('login.html', user=user)
            

        


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)