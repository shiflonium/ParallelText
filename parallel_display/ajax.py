'''DAJAX'''
from dajaxice.decorators import dajaxice_register
from django.utils import simplejson
from django.contrib.auth.models import User
from languages.models import Translations
from languages.models import UserDictionary



@dajaxice_register
def insert_word(request, word):
    '''
    This function inserting a word into the UserDictionary.
    The user has to be logged in in order to use this feature
    '''    

    #Check if the user is connected
    auth = request.user.is_authenticated()
	#print "AUTH:" + str(auth)
    word = word.replace(' ', '')
	#print "ORIGINAL WORD: '" + word +"'"


	#USERNAME
    if(auth):
        username = request.user
        current_user = User.objects.get(username=username)
        uniword = unicode(word)
		#print "UNIWORD:" + uniword
        current_word = Translations.objects.get(original = uniword)
		#print "USERNAME:" + str(username)
		#print "currentUser:" + str(currentUser)
		#print 'currentWord:' + str(currentWord)
        
        #Check if word exists in the user table
        existence_check = UserDictionary.objects.filter(userID=current_user.id, definitionID=current_word.definitionID)

        if (existence_check.count() == 0):
            saved_definition = UserDictionary(
            	userID=current_user.id, definitionID=current_word.definitionID)
            saved_definition.save()

            return simplejson.dumps({'result':auth, 'word':word})

        else:
            return simplejson.dumps({'result':auth, 'word':'|||'})

        
    else:
        return simplejson.dumps({'result':auth})