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

[Dribbble]: http://dribbble.com/
[license]: http://en.wikipedia.org/wiki/MIT_License
[Python]: http://python.org/
[pip]: http://pip.openplans.org/
