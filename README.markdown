python-dribbble is a simple Python library for interacting with [Dribbble][].
It's [MIT/X11 licensed][license]. It requires [Python][] 2.6+ or 2.5 and
[simplejson][].

Install it with [pip][]:

    pip install -e hg+http://bitbucket.org/sjl/python-dribbble#egg=dribbble

    ... or ...

    pip install -e git+http://github.org/sjl/python-dribbble#egg=dribbble

Use it:

    import dribbble
    d = dribbble.Dribbble()

    print 'Shots from everyone'
    for shot in d.shots():
        print shot.title, shot.url

    print 'Popular shots'
    for shot in d.shots('popular'):
        print shot.title, shot.url

    steve = d.player('stevelosh')

    print 'Shots from %s (%s):' % (steve.name, steve.location)
    for shot in steve.shots():
        print '    ', shot.title, shot.url

    print 'Shots from players %s is following:' % steve.name
    for shot in steve.shots_following():
        print '    ', shot.title, shot.url

    simplebits = d.player('simplebits')

    print 'All shots from @simplebits:'
    for shot in simplebits.ishots():
        print '%8d: %s' % (shot.id, shot.title)

Documentation
=============

Here's some quick documentation. Want more? Read the source. It's less than
a hundred and fifty lines.

Dribbble
--------

You'll use `dribbble.Dribble` to make most of your API calls.

    import dribbble
    d = dribbble.Dribbble()

* `player(username)`: Get the player with the given username. You can pass
  in the user's numeric ID instead if you feel like it.
* `shot(shot_id)`: Get the shot with the given ID.
* `shots(type)`: Get a list of the latest shots of the give type. The type
  can be `'everyone'`, `'popular'`, or `'debuts'`. If you don't pass in a type
  you'll get `'everyone'` shots.

Player
------

You can get a Player object by calling `d.player()`. Shots also have a `player`
attribute.

* `id`: The (numeric) user id of the player.
* `username`: The username of the player.
* `name`: The full name of the player.
* `url`: The URL of the player's profile.
* `avatar_url`: The URL of the player's avatar image.
* `location`: The location of the player, if they've listed one.
* `shots()`: A list containing the player's latest shots. You can pass `page`
  and/or `per_page` to control pagination.
* `shots_following()`: A list containing the latest Shots of the players this
  player is following. You can pass `page` and/or `per_page` to control
  pagination.
* `ishots()`: A generator that yields shots from this player, newest to oldest.
  It will hit Dribbble's API whenever it needs more shots, so be careful not to
  get rate limited (i.e. don't try to take more than ~1,000 shots per minute).
  You can pass `start_page` to start at a certain page.
* `ishots_following()`: A generator that yields shots from players this player
  is following, newest to oldest.  It will hit Dribbble's API whenever it needs
  more shots, so be careful not to get rate limited (i.e. don't try to take
  more than ~1,000 shots per minute). You can pass `start_page` to start at
  a certain page.

Shot
----

You can get Shot objects from `d.shot()`, `d.shots()`, or from a Player object.

* `id`: The (numeric) shot id of the shot.
* `title`: The title of the shot.
* `url`: The URL of the shot's page.
* `image_url`: The URL of the actual image of the shot.
* `width`: The width of the shot image.
* `height`: The height of the shot image.
* `player`: The Player that made this shot.


Contributing
============

Fork the [Mercurial repository][bb] (preferred) or the [git repository][gh],
add your feature, send a pull request. Stick to the coding style and add a test
for your feature.

Make sure you look at the existing tests before writing your own -- they do
ugly "clever" things to avoid getting banned by Dribbble's API.

[Dribbble]: http://dribbble.com/
[license]: http://en.wikipedia.org/wiki/MIT_License
[Python]: http://python.org/
[simplejson]: http://simplejson.googlecode.com/svn/tags/simplejson-2.1.1/docs/index.html
[pip]: http://pip.openplans.org/
[bb]: http://bitbucket.org/sjl/python-dribbble/
[gh]: http://github.com/sjl/python-dribbble/
