import unittest2 as unittest
from plone.app.testing import login
from plone.app.testing import TEST_USER_NAME
from plone.app.testing import TEST_USER_PASSWORD
from collective.purge_behaviors.tests import PURGE_INTEGRATION_TESTING
from collective.purge_behaviors.interfaces import IPurgeParent
from zope.interface import alsoProvides
from plone import api
from zope.event import notify
from zope.lifecycleevent import IObjectModifiedEvent


class TestProfile(unittest.TestCase):

    layer = PURGE_INTEGRATION_TESTING

    def test_purge_parent(self):
        # get the object, apply the behavior, trigger the edit event, catch it.
        portal = self.layer["portal"]
        #        login(portal, TEST_USER_NAME)
        folder_id = "base"
        base = api.content.create(
            type='Folder',
            id=folder_id,
            title='Base Folder',
            container=portal)
        obj = api.content.create(
            type='Document',
            title='New Obj',
            container=base)
        alsoProvides(obj, IPurgeParent)
        notify(IObjectModifiedEvent(obj))
       
        self.fail("working")

