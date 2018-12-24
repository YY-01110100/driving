country = input('请问你是哪国人：')
age = input('请输入年龄： ')
age = int(age)
if country == '中国':
	if age >= 18:
		print('你可以开车')
	else:
		print('你不可以开车')
elif country == '美国':
	if age >= 16:
		print('你可以开车')
	else:
		print('你不可以开车')
else:
	print('你只能输入中国或者美国')
