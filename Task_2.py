text = str(input("Введите текст: ")).lower()
text = text.replace(" ", "_")

# Б, В, Г, Д, Ж, З, Й, К, Л, М, Н, П, Р, С, Т, Ф, Х, Ц, Ч, Ш, Щ.
alf_consonants = "БВГДЖЗЙКЛМНПРСТФХЦЧШЩ".lower()
alf_volwes = "аоуиыэеёюя".lower()

number_of_consonants = 0
number_of_volwes = 0
number_of_spaces = 0
words_number = 0

most_frequent_words = []
chars = {}

for el in text:
    if el in chars.keys():
        chars[el] += 1
    else:
        chars[el] = 1

    if el == "_":
        number_of_spaces += 1
    elif el in alf_consonants:
        number_of_consonants += 1
    elif el in alf_volwes:
        number_of_volwes += 1

words = text.split(" ")

words_number = len(words)

char_list = []

for char, count in chars.items():
    char_list.append((char, count))

for i in range(len(char_list)):
    for j in range(i+1, len(char_list)):
        if char_list[i][1] < char_list[j][1]:
            char_list[i], char_list[j] = char_list[j], char_list[i]

k = 1
for char, count in char_list:
    print(f"{k}){char}:{count}")
    k += 1
    if k == 4:
        break

print(f"Количество гласных символов: {number_of_volwes}")
print(f"Количество согласных символов: {number_of_consonants}")
print(f"Количество пробелов: {number_of_spaces}")
print(f"Количество слов: {words_number}")

print(f"Топ 3 самых встречающихся символов: {char_list[:3]}")
k = 0
for el in char_list:
    print(el[0], end=" ")
    k += 1
    if k == 3:
        break
