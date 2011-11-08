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


class ICandidato(form.Schema):
    votos = schema.Float(
                        title=_(u"Votos obtenidos"),
                        default=0.0,
                        min=0.0,
                        max=100.0,
                        required=True,
                        )
    nombre = schema.TextLine(
            title=_(u"Nombre(s) y apellido(s)"),
            required=True,
            default=u"",
            )


#@grok.subscribe(IEleccion, IRecordModifiedEvent)
#def detectPriceChange(settings, event):
#    if record.fieldName == 'entryPrice':
#        log.warning("Someone change the price from %d to %d" % (event.oldValue, event.newValue,))
