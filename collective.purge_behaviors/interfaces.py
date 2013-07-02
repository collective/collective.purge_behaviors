from zope.interface import Interface


class IPurgeParent(Interface):
    """ Marker interface for purging an items parent
    """

class IPurgeSiblings(Interface):
    """ Marker interface for purging an items siblings
    """

class IPurgeContents(Interface):
    """ Marker interface for purging a containers contents
    """

class IPurgeSite(Interface):
    """ Marker interface for purging the home page
    """

