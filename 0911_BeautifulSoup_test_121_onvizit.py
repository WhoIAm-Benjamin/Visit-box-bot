import os, shutil
import re 
from bs4 import BeautifulSoup
import pathlib
file = pathlib.Path("1.html")
news = [] 
f_save = open('_SAVE.txt', 'w')

with open("1.html", "r", encoding="utf-8") as f_input:
    contents = f_input.read()
 
soup = BeautifulSoup(contents, 'lxml')
#    print(soup.select("[data-id]"))
#    print("\n")
news=str(soup.select("[data-id]"))
#print(news)
words=str(soup.select('[style="padding: 0px; vertical-align: middle;"]'))

# ищем названия графических файлов (капчи), их тут по идее находит 8 штук, но ориганальных только 4, потом они повторяются
# файлы идут именно в том порядке, как они появляются на экране
pattern = r'([a-f\d]{10}\.[jpgepn]{3,4})' 
match_4 = re.findall(pattern, news) 

path = 'c:/1_files/'
moveto = 'c:/Save/'

for i in range(0, 4):
    print(match_4[i]) 
    f_save.write(match_4[i]+'\n')
    src = path+match_4[i]
    dst = moveto+match_4[i]
    shutil.move(path+match_4[i],moveto+match_4[i])

# ищем слова: автомобиль, кошка, собака и т.д. [всего 12 вариантов]
pattern = r'<b>([а-я]*)</b>' 
match_1 = re.findall(pattern, words)
#print(words)
print(match_1[0])
f_save.write(match_1[0]+'\n')
f_input.close()
f_save.close()

###########################################################################
shutil.rmtree(path, ignore_errors=True) #- удаляет НЕтолько пустую папку, а ЛЮБУЮ
#os.remove("/tmp/<file_name>.txt")
os.remove("1.html")
###########################################################################
