# -*- coding: utf-8 -*-
from books.models import BookInfo

books = [
    ["Bible_Genesis", "Moses", 50],
    ["Quran", "Muhammad",113]
    ]


def main():
    global books
    global BookInfo
    for book in books:
        if (BookInfo.objects.filter(
                title="%s" % book[0],
                author="%s" % book[1],
                chaps="%d" % book[2]).exists()
              == False):
            dj_book = BookInfo(title="%s" % book[0],
                               author="%s" % book[1],
                               chaps="%d" % book[2])
            dj_book.save()

main()


