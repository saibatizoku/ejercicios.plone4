# -*- coding: utf-8 -*-

import unittest2 as unittest

from zope.component import createObject
from zope.component import queryUtility

from plone.app.testing import TEST_USER_ID
from plone.app.testing import setRoles
from plone.app.textfield.value import RichTextValue
from plone.dexterity.interfaces import IDexterityFTI

from ejercicios.plone4.candidato import ICandidato
from ejercicios.plone4.testing import INTEGRATION_TESTING


class EspecialIntegrationTest(unittest.TestCase):

    layer = INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.portal.invokeFactory('Folder', 'test-folder')
        #setRoles(self.portal, TEST_USER_ID, ['Member'])
        self.folder = self.portal['test-folder']

    def test_adding(self):
        self.folder.invokeFactory('ejercicios.plone4.candidato', 'can1')
        can1 = self.folder['can1']
        self.failUnless(ICandidato.providedBy(can1))

    def test_fti(self):
        fti = queryUtility(IDexterityFTI, name='ejercicios.plone4.candidato')
        self.assertNotEquals(None, fti)

    def test_schema(self):
        fti = queryUtility(IDexterityFTI, name='ejercicios.plone4.candidato')
        schema = fti.lookupSchema()
        self.assertEquals(ICandidato, schema)

    def test_factory(self):
        fti = queryUtility(IDexterityFTI, name='ejercicios.plone4.candidato')
        factory = fti.factory
        new_object = createObject(factory)
        self.failUnless(ICandidato.providedBy(new_object))


def test_suite():
    return unittest.defaultTestLoader.loadTestsFromName(__name__)
