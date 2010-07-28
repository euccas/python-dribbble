import time, urllib, urllib2

try: import simplejson as json
except ImportError: import json


API_URL = 'http://api.dribbble.com/'


_TRACK_CALLS = False
_calls = []

def _api(url, id, pagination=None):
    if _TRACK_CALLS:
        _calls.append(time.time())

    if pagination:
        query = '?' + urllib.urlencode(zip(('page', 'per_page'), pagination))
    else:
        query = ''

    u = urllib2.urlopen(API_URL + (url % id) + query)
    return json.loads(u.read())

def _i(f, start_page, **kwargs):
    i = start_page
    l = f(page=start_page, per_page=30, **kwargs)
    seen = set([item.id for item in l])

    while l:
        yield l.pop(0)
        if not l:
            i += 1
            items = f(page=i, per_page=30, **kwargs)
            ids = set([item.id for item in items])
            l.extend([item for item in items if item.id not in seen])
            seen.update(ids)


class Dribbble(object):
    def __init__(self, track_calls=False):
        # Hacky way to make sure the tests don't rate limit us.
        global _TRACK_CALLS
        if track_calls:
            _TRACK_CALLS = True


    def player(self, username):
        '''Return the player with the given username (or user ID).'''
        return Player(_api('players/%s', username))

    def shot(self, shotid):
        '''Return the shot with the given ID.'''
        return Shot(_api('shots/%d', shotid))

    def shots(self, typ='everyone', page=1, per_page=15):
        '''Return shots.

        The ``typ`` argument can be ``'everyone'`` (the default), ``'popular'``,
        or ``'debuts'``, depending on the type of shots you want to retrieve.
        '''
        data = _api('shots/%s', typ, (page, per_page))
        return [Shot(sd) for sd in data]


    def ishots(self, typ='everyone', start_page=1):
        return _i(self.shots, start_page, typ=typ)


    def calls(self):
        return _calls

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
        print s.player.name
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


    def shots(self, page=1, per_page=15):
        '''Return shots from this player.'''
        data = _api('players/%s/shots', self.id, (page, per_page))
        return [Shot(sd) for sd in data]

    def shots_following(self, page=1, per_page=15):
        '''Return shots from players this player is following.'''
        data = _api('players/%s/shots/following', self.id, (page, per_page))
        return [Shot(sd) for sd in data]


    def ishots(self, start_page=1):
        return _i(self.shots, start_page)

    def ishots_following(self, start_page=1):
        return _i(self.shots_following, start_page)


