i = 0
while i < 3:
	password = input('請輸入密碼: ')
	if password == 'a123456':
		print('登入成功')
		break
	else:
		print('密碼錯誤! 還有' + str(2-i) + '次機會')
		i = i + 1
