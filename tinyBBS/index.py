from flask import Flask, jsonify
from flask import request

app = Flask(__name__)

board = '''
<html>
<head>
    <title>message board</title>
</head>
<body>
    <form action="/add" method="post">
        Message: <input type="text" name="message"> <br>
        <input type="submit" value="Submit">
    </form>
</body>
</html>
'''

# 留言板页面
@app.route('/', methods=['GET', 'POST'])
def bbs_index():
    return board


# 新增留言接口
@app.route('/add', methods=['POST'])
def add_comment():
    forbidden_dict = ['sex', 'shit', 'party']
    if request.method == 'POST':
        message = request.form['message']
        # 数据验证判断
        if len(message) < 20:
            return jsonify({'data': [], 'result': False, 'errorMsg': 'The message is too short,min is 20 character'})
        elif len(message) > 140:
            return jsonify({'data': [], 'result': False, 'errorMsg': 'The message is too long,max is 140 character'})
        elif message in forbidden_dict:
            return jsonify({'data': [], 'result': False,
                            'errorMsg': 'The message includes forbidden words,which might be livid or policitic'})
        with open('message.txt', 'a') as f:
            f.write(message + '\n')
            json_data = [
                {'id': 1, 'value': message}
            ];
        return jsonify({'data': json_data, 'result': True, 'errorMsg': ''})
    else:
        return "Invalid request!!!"


if __name__ == '__main__':
    app.run(debug=True) # 正式环境可以不设置debug模式
