# coding=utf-8
from flask import Flask, request,render_template
import moudle
import json

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('add_word.html')


@app.route('/add_words', methods=['POST'])
def add_words():
    user = request.form.get('user')
    words_json = request.form.get('words')
    result = moudle.add_words(user,words_json)
    return result


@app.route('/add_word_temp',methods=['POST'])
def add_word_temp():
	user = "browser-temp"
	words = []
	word = {}
	word['word'] = request.form.get('word')
	word['soundMark'] = request.form.get('sound_mark')
	word['mean'] = request.form.get('mean')
	word['sentence'] = request.form.get('sentence')
	word['time'] = moudle.time_stamp()
	words.append(word)
	words_json = json.dumps(words,ensure_ascii=False)
	result = moudle.add_words(user,words_json)
	result = json.loads(result)
	if result['failNum'] != 0:
		return json.dumps(result,ensure_ascii=False)
	return render_template('add_word.html')


@app.route('/get_update',methods=['GET'])
def get_update():
	user = request.args.to_dict()['user']
	result = moudle.get_update_words(user)
	return result


if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8080)
