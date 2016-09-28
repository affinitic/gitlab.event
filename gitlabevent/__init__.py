from pyramid.config import Configurator
from gitlabevent.resources import Root


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(root_factory=Root, settings=settings)
    includegitlabevent(config)
    return config.make_wsgi_app()


def includegitlabevent(config):
    config.add_route('gitlabevent', '/gitlabevent')
    config.scan('gitlabevent.views')
