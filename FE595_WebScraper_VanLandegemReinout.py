from lxml import html

import requests
from bs4 import BeautifulSoup

men = []
women = []
for _ in range(50):
    r = requests.get('https://theyfightcrime.org/')
    #print(r.text[0:500])


    soup = BeautifulSoup(r.text, 'html.parser')

    line = str(soup('p')[1].string)

    loc1 = line.find("She's")
    loc2 = line.find("They")

    hes = line[:loc1]
    shes = line[loc1:loc2]

    print(hes)
    print(shes)

    men.append(hes)
    women.append(shes)

with open('Men.txt', 'w') as txt:
    txt.write('\n'.join(men))
    txt.close()

with open('Women.txt', 'w') as txt:
    txt.write('\n'.join(women))
    txt.close()








