from dajax.core import Dajax
from dajaxice.decorators import dajaxice_register
from django.utils import simplejson
from django.contrib.auth.models import User
from languages.models import Translations
from languages.models import UserDictionary

@dajaxice_register
def insertWord(request, word):
	print "HI"

	#Check if the user is connected
	auth = request.user.is_authenticated()
	print "AUTH:" + str(auth)

	#USERNAME
	if(auth):
		username = request.user
		currentUser = User.objects.get(username=username)
		uniword = word.decode('utf8')
		print "WORD:" + uniword
		currentWord = Translations.objects.get(fromLang = uniword)
		print "USERNAME:" + username
		print "currentUser:" + currentUser
		print 'currentWord:' + currentWord
		savedDefinition = UserDictionary(userID=currentUser.id, definitionID=currentWord.definitionID)
		savedDefinition.save();
		return simplejson.dumps({'result':auth, 'word':word})
	else:
		return simplejson.dumps({'result':auth})