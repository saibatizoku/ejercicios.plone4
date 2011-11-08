# -*- coding: utf-8 -*-

import unittest2 as unittest

from zope.component import createObject
from zope.component import queryUtility

from plone.app.testing import TEST_USER_ID
from plone.app.testing import setRoles
from plone.app.textfield.value import RichTextValue
from plone.dexterity.interfaces import IDexterityFTI

from ejercicios.plone4.eleccion import IEleccion
from ejercicios.plone4.testing import INTEGRATION_TESTING


class EleccionIntegrationTest(unittest.TestCase):

    layer = INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.portal.invokeFactory('Folder', 'test-folder')
        #setRoles(self.portal, TEST_USER_ID, ['Member'])
        self.folder = self.portal['test-folder']

    def test_adding(self):
        self.folder.invokeFactory('ejercicios.plone4.eleccion', 'ele1')
        ele1 = self.folder['ele1']
        self.failUnless(IEleccion.providedBy(ele1))

    def test_fti(self):
        fti = queryUtility(IDexterityFTI, name='ejercicios.plone4.eleccion')
        self.assertNotEquals(None, fti)

    def test_schema(self):
        fti = queryUtility(IDexterityFTI, name='ejercicios.plone4.eleccion')
        schema = fti.lookupSchema()
        self.assertEquals(IEleccion, schema)

    def test_factory(self):
        fti = queryUtility(IDexterityFTI, name='ejercicios.plone4.eleccion')
        factory = fti.factory
        new_object = createObject(factory)
        self.failUnless(IEleccion.providedBy(new_object))


def test_suite():
    return unittest.defaultTestLoader.loadTestsFromName(__name__)
