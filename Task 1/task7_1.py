print('\n'*100)

letters = ['а', 'я', 'у', 'ю', 'о', 'е', 'ё', 'э', 'и', 'ы']

# song='пара-ра-рам рам-пам-папам па-ра-па-дам' 
song = input("Enter the song in Russian language: ").lower()
yes = 'Парам пам-пам'
no = 'Пам парам'

def did(str_1):
    count = 0
    for i in range(len(str_1)):
        if str_1[i] in letters:
            count += 1
    return count

arr = list(map(did, song.split()))

print(f"This is a string for cheking our program ---->  {arr}")
yes = 'Парам пам-пам'
no = 'Пам парам'
if arr.count(arr[0]) == len(arr) and arr[0] != 0:
    print(yes)

else:
    print(no)

# This is the solution with 2 "for"

# def counter_ritm(my_string):
#   new_my_string=my_string.split()
#   ritm=[]
#   count=0
#   for i in range(len(new_my_string)):
#     count=0
#     for j in new_my_string[i]:
#       if j in letters:
#         count+=1
#     ritm.append(count)
#   print(ritm)
#   if ritm.count(ritm[0])==len(ritm) and ritm[0]!=0:
#     print(yes)

#   else:
#     print(no)

# counter_ritm(song)
