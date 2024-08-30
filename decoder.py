#Google doc decoder and reader
import requests
import sys
from bs4 import BeautifulSoup

input = 'https://docs.google.com/document/d/e/2PACX-1vSHesOf9hv2sPOntssYrEdubmMQm8lwjfwv6NPjjmIRYs_FOYXtqrYgjh85jBUebK9swPXh_a5TJ5Kl/pub'

#Get input argument
if(len(sys.argv) != 2):
    print("Input argument not found. Using default string.")
else:
    input = sys.argv[1]

# Get raw HTML
try:
    r = requests.get(input)
except:
    print("ERROR: unable to access google doc.")
    exit()

#Find table using BeautifulSoup parser
soup = BeautifulSoup(r.content, 'lxml').find(lambda tag:tag.name=='table')

#Data Validation
if list(soup.select('tr')[0].stripped_strings) != ['x-coordinate', 'Character', 'y-coordinate']:
    print("Error: unable to read table.")
    exit()

#Convert to list
l = []
for e in soup.select('tr')[1:]:
    l.append(list(e.stripped_strings))

#Cast to int for better data sorting
for i in l:
    i[0] = int(i[0])
    i[2] = int(i[2])

# Sort by cords
l.sort(key=lambda a : (-a[2], a[0]))

# Print code
last = l[0]

for e in l:
    if(e[2] != last[2]): print('\n', end='')
    print(' ' * (e[0] - last[0] - 1) + e[1], end='')
    last = e





