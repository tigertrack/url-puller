# experimental code

from urllib.parse import urlparse

linklist = []

with open("bookmark.html") as file_object:
    bookmark = file_object.read()

while bookmark.lower().find('<a ') != -1 :
    
    start = bookmark.lower().find('<a ')
    stop = bookmark.lower().find('</a>')
    
    if bookmark[start:stop+4] != '':
        linklist.append(bookmark[start:stop+4])
    bookmark = bookmark[stop+4:]
    
with open('temp.html', "w") as temp:
    domain = ''
    for link in linklist:
        
        print(link, file=temp)

# print(*linklist, sep = '\n')