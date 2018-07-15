#Создать список с оценками учеников разных классов школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]

slist=[
    {'school_class': '5a', 'scores': [3,4,4,4,5,5,3,4,4,5]},
    {'school_class': '5b', 'scores': [4,2,2,5,3,3,5,4,5,5]},
    {'school_class': '5c', 'scores': [3,3,3,5,2,3,3,4,3,5]},
    {'school_class': '5v', 'scores': [5,4,4,4,5,5,5,4,4,5]}]

ascore = slist[0]['scores']
bscore = slist[1]['scores']
cscore = slist[2]['scores']
vscore = slist[3]['scores']
allscore=ascore+bscore+cscore+vscore

# Посчитать и вывести средний балл по всей школе.
result1 = sum(allscore) // len(allscore)
text='Cредний балл по всей школе: '
print(text + str(result1))
# Посчитать и вывести средний балл по каждому классу.
result2 = sum(ascore) // len(ascore)
text='Cредний балл по 5а классу: '
print(text + str(result2))
result3 = sum(bscore) // len(bscore)
text='Cредний балл по 5б классу: '
print(text + str(result3))
result4 = sum(cscore) // len(cscore)
text='Cредний балл по 5ц классу: '
print(text + str(result4))
result5 = sum(vscore) // len(vscore)
text='Cредний балл по 5в классу: '
print(text + str(result5))
