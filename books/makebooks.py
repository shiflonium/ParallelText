from books.models import BookInfo, BookTranslation
from Languages.models import Languages

bible=BookInfo(title="Bible Genesis", author="Moses", chaps=50)
quran=BookInfo(title="Quran", author="Muhammad", chaps=113)
bible.save()
quran.save()

# genesis languages
es=Languages.objects.get(abbr="ES")
ar=Languages.objects.get(abbr="AR")
el=Languages.objects.get(abbr="EL")
he=Languages.objects.get(abbr="HE")
ko=Languages.objects.get(abbr="KO")
la=Languages.objects.get(abbr="LA")
pt=Languages.objects.get(abbr="PT")
ru=Languages.objects.get(abbr="RU")
th=Languages.objects.get(abbr="TH")
uk=Languages.objects.get(abbr="UK")
zh=Languages.objects.get(abbr="ZH")
en=Languages.objects.get(abbr="EN")


c=BookTranslation(book_id=bible, language_id=es)
d=BookTranslation(book_id=bible, language_id=ar)
e=BookTranslation(book_id=bible, language_id=el)
f=BookTranslation(book_id=bible, language_id=he)
g=BookTranslation(book_id=bible, language_id=ko)
h=BookTranslation(book_id=bible, language_id=la)

i=BookTranslation(book_id=bible, language_id=pt)
j=BookTranslation(book_id=bible, language_id=ru)
k=BookTranslation(book_id=bible, language_id=th)
l=BookTranslation(book_id=bible, language_id=uk)
m=BookTranslation(book_id=bible, language_id=zh)
n=BookTranslation(book_id=bible, language_id=en)

c.save()
d.save()
e.save()
f.save()
g.save()
h.save()
i.save()
j.save()
k.save()
l.save()
m.save()
n.save()



#koran langauges
ar=ar
es=es
en=en
ru=ru
zh=zh

bs=Languages.objects.get(abbr="BS")
de=Languages.objects.get(abbr="DE")
fr=Languages.objects.get(abbr="FR")
hr=Languages.objects.get(abbr="HR")
idi=Languages.objects.get(abbr="ID")
it=Languages.objects.get(abbr="IT")
ja=Languages.objects.get(abbr="JA")
ms=Languages.objects.get(abbr="MS")
pl=Languages.objects.get(abbr="PL")
sw=Languages.objects.get(abbr="SW")
tr=Languages.objects.get(abbr="TR")


b=BookTranslation(book_id=quran, language_id=ar)
c=BookTranslation(book_id=quran, language_id=es)
d=BookTranslation(book_id=quran, language_id=en)
e=BookTranslation(book_id=quran, language_id=ru)
f=BookTranslation(book_id=quran, language_id=zh)
g=BookTranslation(book_id=quran, language_id=bs)
h=BookTranslation(book_id=quran, language_id=de)
i=BookTranslation(book_id=quran, language_id=fr)
j=BookTranslation(book_id=quran, language_id=hr)
k=BookTranslation(book_id=quran, language_id=idi)
l=BookTranslation(book_id=quran, language_id=it)
m=BookTranslation(book_id=quran, language_id=ja)
n=BookTranslation(book_id=quran, language_id=ms)
o=BookTranslation(book_id=quran, language_id=pl)
p=BookTranslation(book_id=quran, language_id=sw)
q=BookTranslation(book_id=quran, language_id=tr)

b.save()
c.save()
d.save()
e.save()
f.save()
g.save()
h.save()
i.save()
j.save()
k.save()
l.save()
m.save()
n.save()
o.save()
p.save()
q.save()
