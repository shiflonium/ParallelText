from books.models import BookInfo, BookTranslation
from ptext.models import AvailLangs

bible=BookInfo(title="Bible Genesis", author="Moses", numChaps=50)
quran=BookInfo(title="Quran", author="Muhammad", numChaps=113)
bible.save()
quran.save()

# genesis languages
es=AvailLangs.objects.get(abbr="ES")
ar=AvailLangs.objects.get(abbr="AR")
el=AvailLangs.objects.get(abbr="EL")
he=AvailLangs.objects.get(abbr="HE")
ko=AvailLangs.objects.get(abbr="KO")
la=AvailLangs.objects.get(abbr="LA")
pt=AvailLangs.objects.get(abbr="PT")
ru=AvailLangs.objects.get(abbr="RU")
th=AvailLangs.objects.get(abbr="TH")
uk=AvailLangs.objects.get(abbr="UK")
zh=AvailLangs.objects.get(abbr="ZH")
en=AvailLangs.objects.get(abbr="EN")


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

bs=AvailLangs.objects.get(abbr="BS")
de=AvailLangs.objects.get(abbr="DE")
fr=AvailLangs.objects.get(abbr="FR")
hr=AvailLangs.objects.get(abbr="HR")
idi=AvailLangs.objects.get(abbr="ID")
it=AvailLangs.objects.get(abbr="IT")
ja=AvailLangs.objects.get(abbr="JA")
ms=AvailLangs.objects.get(abbr="MS")
pl=AvailLangs.objects.get(abbr="PL")
sw=AvailLangs.objects.get(abbr="SW")
tr=AvailLangs.objects.get(abbr="TR")


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
