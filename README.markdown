python-dribbble is a simple Python library for interacting with [Dribbble][].
It's [MIT/X11 licensed][license]. It requires [Python][] 2.5+.

It was written in about half an hour, so don't expect miracles.

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

Documentation
=============

Here's some quick documentation. Want more? Read the source. It's less than
a hundred lines.

Dribbble
--------

You'll use `dribbble.Dribble` to make most of your API calls.

    import dribbble
    d = dribbble.Dribbble()

* **`player(username)`**: Get the player with the given username. You can pass
  in the user's numeric ID instead if you feel like it.
* **`shot(shot_id)`**: Get the shot with the given ID.
* **`shots(type)`**: Get a list of the latest shots of the give type. The type
  can be `'everyone'`, `'popular'`, or `'debuts'`. If you don't pass in a type
  you'll get `'everyone'` shots.

Player
------

You can get a Player object by calling `d.player()`. Shots also have a `player`
attribute.

* **`id`**: The (numeric) user id of the player.
* **`username`**: The username of the player.
* **`name`**: The full name of the player.
* **`url`**: The URL of the player's profile.
* **`avatar_url`**: The URL of the player's avatar image.
* **`location`**: The location of the player, if they've listed one.
* **`shots()`**: A list containing the player's latest shots.
* **`shots_following()`**: A list containing the latest shots of the players
  this player is following.


[Dribbble]: http://dribbble.com/
[license]: http://en.wikipedia.org/wiki/MIT_License
[Python]: http://python.org/
[pip]: http://pip.openplans.org/
