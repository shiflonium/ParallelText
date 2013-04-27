# -*- coding: utf-8 -*-

from books.models import BookInfo, BookTranslation
from languages.models import Languages

book_translations = [
    ["Bible_Genesis", "es"],
    ["Bible_Genesis", "ar"],
    ["Bible_Genesis", "el"],
    ["Bible_Genesis", "he"],
    ["Bible_Genesis", "ko"],
    ["Bible_Genesis", "la"],
    ["Bible_Genesis", "pt"],
    ["Bible_Genesis", "ru"],
    ["Bible_Genesis", "th"],
    ["Bible_Genesis", "uk"],
    ["Bible_Genesis", "zh"],
    ["Bible_Genesis", "en"],

    ["Quran", "bs"],
    ["Quran", "de"],
    ["Quran", "fr"],
    ["Quran", "hr"],
    ["Quran", "id"],
    ["Quran", "it"],
    ["Quran", "ja"],
    ["Quran", "ms"],
    ["Quran", "pl"],
    ["Quran", "sw"],
    ["Quran", "tr"],

    ]


def main():
    global book_translations
    global BookInfo
    global BookTranslation
    for tran in book_translations:
        book = BookInfo.objects.get(title="%s" % tran[0])
        lang = Languages.objects.get(abbr="%s" % tran[1])
        if (BookTranslation.objects.filter(
                book_id=book, language_id=lang).exists()
            == False):
            dj_tran = BookTranslation (book_id=book, language_id=lang)
            dj_tran.save()

main()


