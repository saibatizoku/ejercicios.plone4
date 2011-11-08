# -*- coding: utf-8 -*-

import unicodedata
from logging import getLogger

from five import grok
from zope import schema
from zope.component import getUtility

from plone.directives import form
from plone.registry.interfaces import IRegistry
from z3c.form.browser.checkbox import CheckBoxFieldWidget
from plone.registry.interfaces import IRecordModifiedEvent

log = getLogger('ejercicios.plone4')

from ejercicios.plone4 import _


class IEspecial(form.Schema):
    """Contenedor que permite relacionar contenido especial dentro del portal
    """


