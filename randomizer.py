import random

tab = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

#for i in range(50):
#    first_letter = tab[random.randint(0, len(tab)-1)]
#    second_letter = tab[random.randint(0, len(tab)-1)]
#    while second_letter == first_letter:
#        second_letter = tab[random.randint(0, len(tab)-1)]
#    print(first_letter + " " + second_letter)

try:
    with open('test_file_3', "r") as f:
        data=f.read()
except:
    print("File open error. Check filename!")
datastr = str(data)
for letter in tab:
    replaceto=letter+'{'+str(random.randint(-5, 16))+'}'
    datastr=datastr.replace(letter, replaceto)

print(datastr)