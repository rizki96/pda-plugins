import os
import sys

import puremvc.patterns.command
import puremvc.interfaces
import logging

from aside.facade import AsideFacade

from standalone import model

MAIN_APP_KEY = 'mainAppKey'


class StartupCommand(puremvc.patterns.command.SimpleCommand, puremvc.interfaces.ICommand):

    def execute(self, note):
        main_panel = note.getBody()

        self.facade.registerProxy(model.WebServerProxy(main_panel))

        main_panel.on_shutdown.signal.connect(StartupCommand._on_shutdown)

    @staticmethod
    def _on_shutdown(event):
        logging.info("standalone: shutdown")
        facade = AsideFacade.getInstance("mainAppKey")
        ws_obj = facade.retrieveProxy(model.WebServerProxy.NAME)
        if ws_obj:
            ws_obj.stop()
