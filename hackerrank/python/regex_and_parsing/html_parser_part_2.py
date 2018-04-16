# https://www.hackerrank.com/challenges/html-parser-part-1/problem

from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_comment(self, data):
        data = data.split('\n')
        if len(data) > 1:
            print('>>> Multi-line Comment')
        else:
            print('>>> Single-line Comment')
        for d in data:
            print(d)
    def handle_data(self, data):
        if data == '\n':
            return
        print('>>> Data')
        print(data)

if __name__ == '__main__':
    n = int(input())
    my_html_parser = MyHTMLParser()
    html = '\n'.join([input() for _ in range(n)])
    my_html_parser.feed(html)
