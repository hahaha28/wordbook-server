from dbutil import word_table,user_table
import json
import time

'''
向数据库添加单词
user 是用户标识的字符串
words_json 是客户端发来的单词的json数据
return 返回给客户端的json数据，代表是否有错误信息
'''
def add_words(user,words_json):
	error_list = []
	word_list = json.loads(words_json)
	print(type(word_list))
	for word in word_list:
		print(word['word'])
		result = word_table.find_one({'word':word['word']})
		if result != None:
			# 单词已存在数据库，加入错误列表
			error_word = {}
			error_word['word'] = word['word']
			error_word['reason'] = '单词已存在数据库'
			error_list.append(error_word)
			continue
		# 添加用户和修改时间属性
		word['user'] = user
		word['modifyTime'] = time_stamp()
		# 加入数据库
		print(type(word))
		print(word)
		word_table.insert_one(word)
	error_json = {}
	error_json['failNum'] = len(error_list)
	error_json['words'] = error_list
	# 返回 json 数据，代表是否有错误信息
	return json.dumps(error_json,ensure_ascii=False)
	

'''
获取某位用户需要更新的单词
user 用户的标识字符串
return 返回给客户端的json数据
'''
def get_update_words(user):
	# 获取用户上次更新时间
	user_data = user_table.find_one({'user':user})
	update_time = 0
	if user_data == None:
		user_table.insert_one({'user':user})
	else:
		update_time = user_data['updateTime']
	# 查找数据库中修改时间大于更新时间，且添加（修改）者不是该用户的所有单词
	results = word_table.find({'$and':[{'modifyTime':{'$gt':update_time}},{'user':{'$ne':user}}]})
	result_json = []
	for word in results:
		del word['_id']
		result_json.append(word)
	# 设置该用户的更新时间
	user_table.update_one({'user':user},{'$set':{'updateTime':time_stamp()}})
	return json.dumps(result_json,ensure_ascii=False)


# 返回时间戳（毫秒级）
def time_stamp():
	return int(round(time.time())*1000)



