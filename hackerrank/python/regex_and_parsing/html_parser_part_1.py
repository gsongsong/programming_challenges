# https://www.hackerrank.com/challenges/html-parser-part-1/problem

from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print('Start :', tag)
        if attrs:
            self.print_attrs(attrs)
    def handle_endtag(self, tag):
        print('End   :', tag)
    def handle_startendtag(self, tag, attrs):
        print('Empty :', tag)
        if attrs:
            self.print_attrs(attrs)
    def print_attrs(self, attrs):
        if not attrs:
            return
        for attr in attrs:
            print('->', attr[0], '>', attr[1])

if __name__ == '__main__':
    n = int(input())
    my_html_parser = MyHTMLParser()
    for _ in range(n):
        my_html_parser.feed(input().strip())
