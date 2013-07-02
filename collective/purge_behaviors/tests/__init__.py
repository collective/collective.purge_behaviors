from plone.app.testing import PloneSandboxLayer
from plone.app.testing.layers import FunctionalTesting
from plone.app.testing.layers import IntegrationTesting
from zope.configuration import xmlconfig


class PurgeBehaviors(PloneSandboxLayer):

    def setUpZope(self, app, configurationContext):
        import collective.purge_behaviors
        xmlconfig.file('configure.zcml', collective.purge_behaviors, context=configurationContext)

    def setUpPloneSite(self, portal):
        from plone.app.testing import setRoles
        from plone.app.testing import TEST_USER_ID
        setRoles(portal, TEST_USER_ID, ['Manager'])
        

PURGE_FIXTURE = PurgeBehaviors()
PURGE_INTEGRATION_TESTING = IntegrationTesting(bases=(PURGE_FIXTURE,), name="collective.purge_behaviors:Integration")
PURGE_FUNCTIONAL_TESTING = FunctionalTesting(bases=(PURGE_FIXTURE,), name="collective.purge_behaviors:Functional")
