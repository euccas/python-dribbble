import urllib2

try: import simplejson as json
except ImportError: import json


API_URL = 'http://api.dribbble.com/'


def _api(url, id):
    u = urllib2.urlopen(API_URL + url % id)
    return json.loads(u.read())

class Dribbble(object):
    def __init__(self):
        pass

    def player(self, username):
        return Player(_api('players/%s/', username))

    def shot(self, id):
        return Shot(_api('shots/%d/', id))



class Shot(object):
    def __init__(self, data):
        for k, v in data.items():
            if k != u'player':
                setattr(self, k, v)
        self.player = Player(data[u'player'])

class Player(object):
    def __init__(self, data, username=None):
        for k, v in data.items():
            setattr(self, k, v)

        # Srsly, Dribbble API?
        self.username = self.url.strip('/').rsplit('/', 1)[-1]

