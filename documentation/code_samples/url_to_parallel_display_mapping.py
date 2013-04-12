import re

request_string = "localhost/parallel_display/Bible_Genesis/ch_1/ENHE/"

m=re.match(r"(?P<hostname>\w+)/(?P<directory>\w+)/(?P<book>\w+)/(?P<chapter>\w+)/(?P<language1>\w\w)(?P<language2>\w\w)", request_string)
hostname=m.group('hostname')
directory=m.group('directory')
book=m.group('book')
chapter=m.group('chapter')
language1=m.group('language1')
language2=m.group('language2')

base_text_dir="localhost/texts"

right_text = base_text_dir + "/" + book + "/" + language1 + "/" + chapter + ".html"
left_text = base_text_dir + "/" + book + "/" + language1 + "/" + chapter + ".html"

print "request string: " + request_string
print "right text: " + right_text
print "left text: " + left_text
