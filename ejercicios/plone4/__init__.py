# -*- coding: utf-8 -*-

try:
    from zope.i18nmessageid import MessageFactory

    _ = MessageFactory('ejercicios.plone4')
except ImportError:
    _ = unicode
