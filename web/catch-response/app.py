from flask import Flask, request

app = Flask(__name__)

ret_form = '''<form method="post">
        <input type="text" name="input" required>
        <button>Submit</button>
    </form>'''

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        value = request.form.get('input')
        return f'<script>alert("hello, {value}")</script>' + ret_form
    else:
        return ret_form

@app.route('/test', methods=['GET', 'POST'])
def test():
    req_method = request.method
    return f'You sended request as {req_method}'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
