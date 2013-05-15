# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from users.models import UserAccount
from languages.models import Languages

users = [
    #[USERNAME, PASSWORD, FIRST_NAME, LAST_NAME, EMAIL, NATIVE_LANG]
    ['testuser', 'testuser', 'fname', 'lname', 'email@domain.com', False, 'en'],
    ['hbergeron', 'hbergeron', 'Harrison', 'Bergeron', 'hbergon@example.com', False, 'fr'],
    ['esandy', 'esandy', 'Emiliana', 'Sandy', 'esandy@helloworld.com', False, 'en'],
    ['eentrena', 'eentrena', 'Estrella', 'Entrena', 'eentrena@somewhere.com', False, 'es'],
    ['rcheng', 'rcheng', 'Richard', 'Cheng', 'rcheng@blah.com', False, 'zh'],
    ['jswift', 'jswift', 'Jennifer', 'Swift', 'jswift@apple.com', False, 'es'],
    ['jpelz', 'jpelz', 'Jacob', 'Pelz', 'jpelz@myemail.com', False, 'he'],
    ['ochoudhury', 'ochoudhury', 'Owamic', 'Choudhury', 'ochoudhury@com.com', False, 'hi'],
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
            new_user = User.objects.create_user(username="%s" % user[0],
                                         email="%s" % user[4],
                                         password="%s" % user[1],
                                         first_name="%s" % user[2],
                                         last_name="%s" % user[3])
            lang = Languages.objects.get(abbr="%s" % user[6])
            extra_info = UserAccount(user_id=new_user.pk,
                                     is_contentmgr=user[5],
                                     native_lang=lang)
            extra_info.save()

main()
