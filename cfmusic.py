```python
import spotipy
sp = spotipy.Spotify()

results = sp.search(q='weezer', limit=20)
for i, t in enumerate(results['tracks']['items']):
    print ' ', i, t['name']
```
spotify = spotipy.Spotify()
results = spotify.search(q='artist:' + name, type='artist')
print results

util.prompt_for_user_token(username,scope,client_id='2c4153be84884261821a6b0f95eefe42',client_secret='b63cb1b221a241aebffaf8cb34ec382d',redirect_uri='http://localhost/')

class spotipy.client.Spotify(auth=None, requests_session=True, client_credentials_manager=None, proxies=None, requests_timeout=None)

audio_analysis(id)

# Change country and locale
#country - An ISO 3166-1 alpha-2 country code.
#locale - The desired language, consisting of an ISO 639 language code and an ISO 3166-1 alpha-2 country code, joined by an underscore.
#limit - The maximum number of items to return. Default: 20. Minimum: 1. Maximum: 50
#offset - The index of the first item to return. Default: 0 (the first object). Use with limit to get the next set of items.#

categories(country=None, locale=None, limit=1, offset=0)
