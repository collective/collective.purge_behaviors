from Products.CMFCore.interfaces import IFolderish
from z3c.caching.interfaces import IPurgePaths
from plone.app.caching.purge import ContentPurgePaths
from zope.interface import implements
from zope.component import adapts
from zope.site.hooks import getSite
from Acquisition import aq_parent
from interfaces import IPurgeParent, IPurgeSiblings, IPurgeContents, IPurgeSite
import logging


class PurgeParentPaths(object):
    """ Return purge paths for an objects parent
    """
    implements(IPurgePaths)
    adapts(IPurgeParent)

    def __init__(self, context):
        self.context = context

    def getRelativePaths(self):
        parent = aq_parent(self.context)
        if parent is not None:
            paths = [x for x in ContentPurgePaths(parent).getRelativePaths()]
            logging.debug("Purging parents of %s: %s" % (self.context.absolute_url(),
                                                         paths))
            return paths
        return []

    def getAbsolutePaths(self):
        return []


class PurgeSiblingPaths(object):
    """ Purge paths for an items siblings
    """
    implements(IPurgePaths)
    adapts(IPurgeSiblings)

    def __init__(self, context):
        self.context = context

    def getRelativePaths(self):        
        parent = aq_parent(self.context)
        paths = []
        if parent is not None:
            for id, child in parent.contentItems():
                if id == self.context.id:
                    # make sure to exclude self since its
                    # likely purged elsewhere
                    continue                
                paths += [x for x in ContentPurgePaths(child).getRelativePaths()]
                
        logging.debug("Purging siblings of %s: %s" % (self.context.absolute_url(),
                                                         paths))
        return paths

    def getAbsolutePaths(self):
        return []


class PurgeContentsPaths(object):
    """ Purge paths for an items contents
    """
    implements(IPurgePaths)
    adapts(IPurgeContents)

    def __init__(self, context):
        self.context = context

    def getRelativePaths(self):
        if not IFolderish.providedBy(self.context):
            return []
        
        paths = []
        for id, item in self.context.contentItems():
            paths += [x for x in ContentPurgePaths(item).getRelativePaths()]

        logging.debug("Purging children of %s: %s" % (self.context.absolute_url(),
                                                      paths))
        return paths

    def getAbsolutePaths(self):
        return []


class PurgeSitePaths(object):
    """ Purge site root on edit
    """
    implements(IPurgePaths)
    adapts(IPurgeSite)

    def __init__(self, context):
        self.context = context

    def getRelativePaths(self):
        site = getSite()
        paths = [x for x in ContentPurgePaths(site).getRelativePaths()]
        logging.debug("Purging site root from %s: %s" % (self.context.absolute_url(),
                                                         paths))
        return paths
        
    def getAbsolutePaths(self):
        return []

