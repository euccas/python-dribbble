import itertools, time
from .. import api

LIMIT = 25

class SafeDribbble(object):
    def __init__(self):
        self.d = api.Dribbble(track_calls=True)

    def call(self, fname, *args, **kwargs):
        f = getattr(self.d, fname)

        now = time.time()
        cs = filter(lambda i: i >= (now - 60), self.d.calls())
        if len(cs) > LIMIT:
            sleep = (cs[len(cs)/2] + 60) - now
            print '*** Waiting for %f seconds to avoid rate limiting' % sleep
            time.sleep(sleep)

        return f(*args, **kwargs)

    def pcall(self, player, fname, *args, **kwargs):
        f = getattr(player, fname)

        now = time.time()
        cs = filter(lambda i: i >= (now - 60), self.d.calls())
        if len(cs) > LIMIT:
            sleep = (cs[len(cs)/2] + 60) - now
            print '*** Waiting for %f seconds to avoid rate limiting' % sleep
            time.sleep(sleep)

        return f(*args, **kwargs)

d = SafeDribbble()


def _check_shot(sid):
    shot = d.call('shot', sid)
    assert str(shot.id) == str(sid)

def test_shot():
    for sid in xrange(1, 3):
        yield _check_shot, sid


def test_shots():
    shots = d.call('shots')
    assert len(shots) == 15

    assert all([shot.id for shot in shots])


def test_player():
    p = d.call('player', 'simplebits')
    assert p.username == u'simplebits'


def test_player_shots():
    p = d.call('player', 'simplebits')

    shots = d.pcall(p, 'shots')
    assert len(shots) == 15

    shots = d.pcall(p, 'shots', per_page=5)
    assert len(shots) == 5

    new_shots = d.pcall(p, 'shots', page=3, per_page=5)
    assert len(new_shots) == 5
    assert not any([ns.id in [s.id for s in shots] for ns in new_shots])


def test_player_shots_following():
    p = d.call('player', 'simplebits')

    shots = d.pcall(p, 'shots_following')
    assert len(shots) == 15

    shots = d.pcall(p, 'shots_following', per_page=5)
    assert len(shots) == 5

    new_shots = d.pcall(p, 'shots_following', page=4, per_page=5)
    assert len(new_shots) == 5
    assert not any([ns.id in [s.id for s in shots] for ns in new_shots])


def test_player_ishots():
    p = d.call('player', 'simplebits')

    ishots = d.pcall(p, 'ishots')
    shots = list(itertools.islice(ishots, 0, 45, 1))
    assert len(shots) == 45

    inew_shots = d.pcall(p, 'ishots', start_page=3)
    new_shots = list(itertools.islice(inew_shots, 0, 45, 1))
    assert len(new_shots) == 45
    assert not any([ns.id in [s.id for s in shots] for ns in new_shots])


def test_player_ishots_following():
    p = d.call('player', 'simplebits')

    ishots = d.pcall(p, 'ishots_following')
    shots = list(itertools.islice(ishots, 0, 45, 1))
    assert len(shots) == 45

    inew_shots = d.pcall(p, 'ishots_following', start_page=3)
    new_shots = list(itertools.islice(inew_shots, 0, 45, 1))
    assert len(new_shots) == 45
    assert not any([ns.id in [s.id for s in shots] for ns in new_shots])

