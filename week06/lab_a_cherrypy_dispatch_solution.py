import cherrypy
import json

class HelloWorld:
    @cherrypy.expose
    def index(self):
        yield 'Hello CherryPy world!'
        yield '<br/>'
        yield '<br/><a href="/link_a/">link a</a>'
        yield '<br/><a href="/link_b/">link b</a> - should work like link a'
        yield '<br/>'
        yield '<br/><a href="/positional/first/">/positional/first/</a>'
        yield '<br/><a href="/positional/first/second/">/positional/first/second/</a>'
        yield '<br/><a href="/positional/first/second/third/">/positional/first/second/third/</a>'
        yield '<br/><a href="/positional/first/second/third/fourth/">/positional/first/second/third/fourth/</a>'
        yield '<br/>'
        yield '<br/><a href="/named?a=spam">/named?a=spam</a>'
        yield '<br/><a href="/named?a=spam&b=eggs">/named?a=spam&b=eggs</a>'
        yield '<br/><a href="/named?a=spam&b=eggs&c=ham">/named?a=spam&b=eggs&c=ham</a>'
    @cherrypy.expose
    def link_a(self):
        yield 'hello from link a'

    # possible solution
    @cherrypy.expose
    def positional(self, a=None, b=None, c=None, d=None):
        yield 'look, arguments!<br/>'
        if a:
            yield a +'<br/>'
        if b:
            yield b +'<br/>'
        if c:
            yield c +'<br/>'
        if d:
            yield d +'<br/>'

    # possible solution
    @cherrypy.expose
    def positional(self, *args):
        yield 'look, arguments!<br/>'
        yield '<br/>'.join(args)

    # possible solution
    @cherrypy.expose
    def named(self, a=None, b=None, c=None, d=None):
        yield 'look, keyword arguments!<br/>'
        yield '<table border="1">'
        if a:
            yield '<tr><td>%s</td><td>%s</td></tr>' % ('a', a)
        if b:
            yield '<tr><td>%s</td><td>%s</td></tr>' % ('b', b)
        if c:
            yield '<tr><td>%s</td><td>%s</td></tr>' % ('c', c)
        if d:
            yield '<tr><td>%s</td><td>%s</td></tr>' % ('d', d)
        yield '</table>'

    # possible solution
    @cherrypy.expose
    def named(self, **kwargs):
        yield 'look, keyword arguments!<br/>'
        yield '<table border="1">'
        for key, value in kwargs.items():
            yield '<tr><td>%s</td><td>%s</td></tr>' % (key, value)
        yield '</table>'

    @cherrypy.expose
    def default(self, *args, **kwargs):
        data = {'args': args,
                'kwargs': kwargs}
        yield json.dumps(data)

cherrypy.quickstart(HelloWorld())

