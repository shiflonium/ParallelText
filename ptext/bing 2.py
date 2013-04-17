''' This method takes a list ant returned a translated list'''
def getListTranslate(text,frm,to, token):
    trns = list()
    for i in range (0, len(text)):
        trns.append('')
        trns[i] = translate(text[i],frm,to, token);

    return trns


''' This method translate a single word'''
def getToken():
    args = {
        'client_id': 'lshimro00',#your client id here
        'client_secret': '1otRBsji+lZ2gR0OWOwAchORE+H9ZUkASlfF9XAhH/g=',#your azure secret here
        'scope': 'http://api.microsofttranslator.com',
        'grant_type': 'client_credentials'
    }
    
    oauth_url = 'https://datamarket.accesscontrol.windows.net/v2/OAuth2-13'
    oauth_junk = json.loads(requests.post(oauth_url,data=urllib.urlencode(args)).content)

    return oauth_junk
    
def translate(myWord, frm, to, oauth_junk):
    translation_args = {
        'text': myWord,
        'to': to,
        'from': frm
    }

    headers={'Authorization': 'Bearer '+oauth_junk['access_token']}
    translation_url = 'http://api.microsofttranslator.com/V2/Ajax.svc/Translate?'
    translation_result = requests.get(translation_url+urllib.urlencode(translation_args),headers=headers)
    tword = translation_result.content
    return tword