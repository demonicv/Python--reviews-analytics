data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line.strip())
		count += 1
		if count % 1000 == 0:
			print(len(data))
print('檔案讀取完畢，共有', len(data), '筆資料')

sum_len = 0
for d in data: 
	sum_len = sum_len + len(d)
print('每一筆留言的平均長度為: ', sum_len/len(data), '的字')

new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('共有', len(new), '筆資料小於100')

#文字計數
wc = {} # word_count
number = 0
for d in data:
	words = d.split()
	for word in words:	
		if word in wc:
			wc[word] += 1
		else:
			wc[word] = 1 #新增新的key進wc字典
for word in wc :
	if wc[word] > 1000000:
		print(word, wc[word])
# if keyword in wc:
# 	print(f'{keyword} 出現過 {wc[keyword]} 次數')
# else:
# 	print('defind this word')

while True:
		keyword = input('請輸入您想查詢的字: ')
		if keyword == 'q':
			break
		if word in wc:
			print(keyword, '出現過的次數為: ', wc[keyword])
		else:
			print('這個字沒有出現過!')
print('感謝使用本查詢功能')









