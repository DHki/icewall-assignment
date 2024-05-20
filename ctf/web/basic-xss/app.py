from flask import Flask, request, render_template, session
from secret import FLAG
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
        driver.add_cookie({"name":"flag", "value":f"{FLAG}"})
        driver.get(url)
    except Exception as e:
        driver.quit()
        print(e)
        return False
    driver.quit()
    return True


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', memo="Welcome to Basic XSS!! Can Cookie Share?")
        
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
        if not read_url(f'{param}'):
            return '<script>alert("wrong??");history.go(-1);</script>'

        return '<script>alert("good");history.go(-1);</script>'
            



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)