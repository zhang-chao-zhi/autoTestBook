from flask import Flask, jsonify
from flask import request
import time, hashlib

app = Flask(__name__)

login_html = '''
<html>
<head>
    <title>Login Page</title>
</head>
<body>
    <form action="/doLogin" method="post">
        Account: <input type="text" name="account"> <br>
        Password: <input type="text" name="password"> <br>
        <input type="submit" value="Submit">
        <input type="reset" value="reset">
    </form>
</body>
</html>
'''


@app.route('/', methods=['GET', 'POST'])
def login_index():
    return login_html


@app.route('/doLogin', methods=['POST'])
def do_login():
    if request.method == 'POST':
        account = request.form['account']
        password = request.form['password']

        if account == 'freePHP' and password == 'lovePython':
            timestamp = time.time()
            prev_str = account + password + str(timestamp)
            token = hashlib.md5(prev_str.encode(encoding='UTF-8')).hexdigest()
            json_data = [
                {'token': token, 'user_id': 101}
            ];
            return jsonify({'data': json_data, 'result': True, 'errorMsg': ''})
        else:
            return jsonify({'data':[], 'result': False, 'errorMsg': 'Account and password is not matched!'})


if __name__ == '__main__':
    app.run(debug=True)
