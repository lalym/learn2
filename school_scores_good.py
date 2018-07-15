scores = [
	{'school_class': '5a', 'scores': [3,4,4,4,5,5,3,4,4,5]},
	{'school_class': '5b', 'scores': [4,2,2,5,3,3,5,4,5,5]},
	{'school_class': '5c', 'scores': [3,3,3,5,2,3,3,4,3,5]},
	{'school_class': '5v', 'scores': [5,4,4,4,5,5,5,4,4,5]},
	]


amount = 0
count = 0


for i in scores:

	for d in i['scores']:
		amount += d
		count += 1
	print('Класс: {}, Cредний балл: {}'.format(i['school_class'], amount/count))


print('Cредний балл по всей школе: {}'.format(amount/count))