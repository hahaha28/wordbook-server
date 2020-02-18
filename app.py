from flask import Flask, request
import moudle

app = Flask(__name__)


@app.route('/')
def hello_world():
    return "hello"


@app.route('/add_words', methods=['POST'])
def add_words():
    user = request.form.get('user')
    words_json = request.form.get('words')
    result = moudle.add_words(user,words_json)
    return result


@app.route('/get_update',methods=['GET'])
def get_update():
	user = request.args.to_dict()['user']
	result = moudle.get_update_words(user)
	return result


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
