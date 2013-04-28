# -*- coding: utf-8 -*-

from django.contrib.auth.models import User
from users.models import UserAccount
from languages.models import Languages

users = [
    #[USERNAME, PASSWORD, FIRST_NAME, LAST_NAME, EMAIL, NATIVE_LANG]
    ['testuser', 'testuser', 'fname', 'lname', 'email@domain.com', 'en'],
    ['hbergeron', 'hbergeron', 'Harrison', 'Bergeron', 'hbergon@example.com', 'fr'],
    ['esandy', 'esandy', 'Emiliana', 'Sandy', 'esandy@helloworld.com', 'en'],
    ['eentrena', 'eentrena', 'Estrella', 'Entrena', 'eentrena@somewhere.com', 'es'],
    ['rcheng', 'rcheng', 'Richard', 'Cheng', 'rcheng@blah.com', 'zh'],
    ['jswift', 'jswift', 'Jennifer', 'Swift', 'jswift@apple.com', 'es'],
    ['jpelz', 'jpelz', 'Jacob', 'Pelz', 'jpelz@myemail.com', 'he'],
    ['ochoudhury', 'ochoudhury', 'Owamic', 'Choudhury', 'ochoudhury@com.com', 'hi'],
]

def main():
    global users
    global User
    global UserAccount
    global Languages
    for user in users:
        if User.objects.filter(username="%s" % user[0]).count():
            #print "User \"" + user[0] + "\" exists in database. Skipping."
            pass
        else:
            u = User.objects.create_user(username="%s" % user[0],
                                         email="%s" % user[4],
                                         password="%s" % user[1],
                                         first_name="%s" % user[2],
                                         last_name="%s" % user[3])
            u = User.objects.get(id=u.pk)
            u.native_lang_id = "%s" % user[5]
            u.save()

main()
