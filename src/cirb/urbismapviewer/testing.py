from plone.app.testing import PloneSandboxLayer
from plone.app.testing import applyProfile
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import IntegrationTesting
from plone.app.testing import FunctionalTesting

from plone.testing import z2

from zope.configuration import xmlconfig


class CirburbismapviewerLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load ZCML
        import cirb.urbismapviewer
        xmlconfig.file(
            'configure.zcml',
            cirb.urbismapviewer,
            context=configurationContext
        )

        # Install products that use an old-style initialize() function
        #z2.installProduct(app, 'Products.PloneFormGen')

#    def tearDownZope(self, app):
#        # Uninstall products installed above
#        z2.uninstallProduct(app, 'Products.PloneFormGen')

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'cirb.urbismapviewer:default')

CIRB_URBISMAPVIEWER_FIXTURE = CirburbismapviewerLayer()
CIRB_URBISMAPVIEWER_INTEGRATION_TESTING = IntegrationTesting(
    bases=(CIRB_URBISMAPVIEWER_FIXTURE,),
    name="CirburbismapviewerLayer:Integration"
)
CIRB_URBISMAPVIEWER_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(CIRB_URBISMAPVIEWER_FIXTURE, z2.ZSERVER_FIXTURE),
    name="CirburbismapviewerLayer:Functional"
)
