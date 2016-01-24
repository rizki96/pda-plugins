__author__ = 'rizki'

import os
import sys

import puremvc.interfaces
import puremvc.patterns.mediator

from . import main
#import vo
#import model
import utils

from aside import pages, events, components


class StandaloneViewMediator(puremvc.patterns.mediator.Mediator, puremvc.interfaces.IMediator):

    NAME = 'StandaloneViewMediator'

    def __init__(self, viewComponent):
        super(StandaloneViewMediator, self).__init__(StandaloneViewMediator.NAME, viewComponent)

    def listNotificationInterests(self):
        return [
            main.StandaloneAppFacade.DISPLAY_PAGE,
        ]

    def handleNotification(self, note):
        note_name = note.getName()

        if note_name == main.StandaloneAppFacade.DISPLAY_PAGE:
            params = dict(note.getBody())
            self.load_form(params)

    def handleHooks(self, **kwargs):
        if 'action' in kwargs:
            pass

    def load_form(self, params):
        current_path = utils.root_dir()
        if 'postfix_path' in params:
            current_path +=  params["postfix_path"]
        variables = params["vars"] if "vars" in params else {}
        content = pages.retrieve(params["name"], BASE_PATH=current_path, ASIDE_JS=None, TITLE=params["title"],
                                 **variables)
        self.viewComponent.webView.setHtml(*content)
