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
        u = User.objects.create_user(user[0],
                                     user[4],
                                     user[1],
                                     first_name=user[2],
                                     last_name=user[3])

main()
