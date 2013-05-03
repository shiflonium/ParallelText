from dajax.core import Dajax
from dajaxice.decorators import dajaxice_register
from django.utils import simplejson
from django.contrib.auth.models import User

@dajaxice_register
def multiply(request, a, b, word):
    dajax = Dajax()
    result = int(a) * int(b)
    dajax.assign('#result','value',str(result))
    
    
    #Check if the user is connected
    auth = request.user.is_authenticated()
    #print auth
    username = request.user

    #USERNAME
    if (auth):
		a = User.objects.get(username=username)
		print a.password
		return simplejson.dumps({'result':auth, 'word':word})