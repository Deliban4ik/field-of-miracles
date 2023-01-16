import random

database_words={
    "Как у западных и южных славян назывались селение, деревня, курень?": "жупа",
    "Что использовали в Китае для глажки белья вместо утюга?":"Сковорода",
    "Ювелиры часто говорят, что бриллиантам необходимо это.":"Одиночество",
    "Какого слова нет в языке народов Арктики?":"Война"
}

start_points=15
count=0
spaces=[]

random_word=random.randint(0, len(database_words)-1)

for question, answer in database_words.items():
    
    if count==random_word:
        answer=answer.lower()
        break
    else:
        count+=1

for i in answer:
    spaces.append("_")

print(question)
print(f"У вас {start_points} очков")
print(" ".join(spaces))

while "_" in spaces:
    action=input("Ввести букву или сразу отгадать слово?\n").lower()
    if action == "отгадать слово":
        player_answer=input("Введите слово: ").lower()
        if player_answer!=answer:
            print("К сожалению вы не отгадали слово и проиграли(((")
            break
        else:
            print("Вы отгадали слово и выиграли")
            break
    elif action == "ввести букву":
        player_letter=input("Введите букву: ").lower()
        if player_letter not in answer:
            start_points-=1
            print(f"Вы назвали неверную букву. Вы потеряли 1 очко, теперь у вас очков: {start_points}")
        else:
            start_points+=1
            print(f"Вы отгадали слово и получили 1 очко. У вас очков: {start_points}")
            count=answer.find(player_letter)
    else:
        print("Введите корректное действие!!!")
        continue

    spaces[count]=answer[count]
    print(" ".join(spaces))


