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
	word = word.replace(' ','')
	print "ORIGINAL WORD: '" + word +"'"


	#USERNAME
	if(auth):
		username = request.user
		currentUser = User.objects.get(username=username)
		uniword = unicode(word)
		print "UNIWORD:" + uniword
		currentWord = Translations.objects.get(original = uniword)
		print "USERNAME:" + str(username)
		print "currentUser:" + str(currentUser)
		print 'currentWord:' + str(currentWord)
		savedDefinition = UserDictionary(userID=currentUser.id, definitionID=currentWord.definitionID)
		savedDefinition.save();
		return simplejson.dumps({'result':auth, 'word':word})
	else:
		return simplejson.dumps({'result':auth})