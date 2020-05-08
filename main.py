# TODO add directory input, so all supported file with directory will be parsed
# TODO add the ability to export into csv, txt, or bookmark manager html format
# TODO add the ability to sort url per domain basis
# TODO move the exported file to a folder

from html.parser import HTMLParser
import magic
import time

class BookmarkSorter(HTMLParser):
    
    def __init__(self):
        super(BookmarkSorter, self).__init__()
        self.string_data = ''
        self.record = False
        self.stats = 0

    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            self.string_data += '<a '
            for attr in attrs:
                self.string_data += '{}="{}" '.format(attr[0], attr[1])
            self.string_data += '>'
            self.record = True
            self.stats += 1
        else:
            self.record = False
    
    def handle_data(self, data):
        data = data.strip()
        data = data.replace('\n', '')
        data = " ".join(data.split())
        if data and self.record == True :
            self.string_data += data + '</a>'
        elif not data and self.record == True :
            self.string_data += '\n'

    def pull_url(self, string):
        
        self.feed(string)
        # return self.string_data

    def export(self):
        ts = int(time.time())
        filename = "export_{}.html".format(ts)
        with open(filename, 'w') as file:
            file.write(self.string_data.replace('\n\n', '\n'))


filename = input("Welcome to bookmark-sorter! please type your filename: ")

try:
    with open(filename) as file:
        allowed = ['text/html']
        mime = magic.Magic(mime=True)
        if mime.from_file(filename) in allowed:
            content = file.read()
            sorter = BookmarkSorter()
            sorter.pull_url(content)
            sorter.export()
            print(f"Export file created. {sorter.stats} URL pulled from the file.")
        else:
            print("File cannot be processed. Currently we only accept [" + "/".join(allowed) + "]. Terminating session...")

except FileNotFoundError:
    print("Cannot found input file, terminating session...")
    exit()


