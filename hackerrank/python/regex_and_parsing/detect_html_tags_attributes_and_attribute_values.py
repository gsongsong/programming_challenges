# https://www.hackerrank.com/challenges/detect-html-tags-attributes-and-attribute-values/problem

from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        if attrs:
            self.print_attrs(attrs)
    def handle_endtag(self, tag):
        pass
    def handle_startendtag(self, tag, attrs):
        print(tag)
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
