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
        '''Return the player with the given username (or user ID).'''
        return Player(_api('players/%s', username))

    def shot(self, shotid):
        '''Return the shot with the given ID.'''
        return Shot(_api('shots/%d', shotid))

    def shots(self, typ='everyone'):
        '''Return shots.

        The ``typ`` argument can be ``'everyone'`` (the default), ``'popular'``,
        or ``'debuts'``, depending on the type of shots you want to retrieve.
        '''
        data = _api('shots/%s', typ)
        return [Shot(sd) for sd in data]


class Shot(object):
    '''A single shot.

    The following data is available::

        import dribbble
        d = dribbble.Dribbble()
        s = d.shot(12345)

        print s.id
        print s.title
        print s.url
        print s.image_url
        print s.width
        print s.height
    '''
    def __init__(self, data):
        for k, v in data.items():
            if k != u'player':
                setattr(self, k, v)
        self.player = Player(data[u'player'])

class Player(object):
    '''A single player.

    The following data is available::

        import dribbble
        d = dribbble.Dribbble()
        p = d.player(12345)

        print p.id
        print p.username
        print p.name
        print p.url
        print p.avatar_url
        print p.location
    '''
    def __init__(self, data, username=None):
        for k, v in data.items():
            setattr(self, k, v)

        # Srsly, Dribbble API?
        self.username = self.url.strip('/').rsplit('/', 1)[-1]

    def shots(self):
        '''Return shots from this player.'''
        data = _api('players/%s/shots', self.id)
        return [Shot(sd) for sd in data]

    def shots_following(self):
        '''Return shots from players this player is following.'''
        data = _api('players/%s/shots/following', self.id)
        return [Shot(sd) for sd in data]


