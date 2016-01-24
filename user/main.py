import sys
from PySide import QtGui
from aside.facade import AsideFacade

from standalone import main as sa_main, components
from . import controller


class PluginFacade(AsideFacade):

    STARTUP = 'startup'
    PLUGIN_DIR = "plugins/user"

    def __init__(self, multitonKey):
        super(PluginFacade, self).__init__(multitonKey)

    def initializeFacade(self):
        super(PluginFacade, self).initializeFacade()
        self.initializeController()

    def initializeController(self):
        super(PluginFacade, self).initializeController()

        super(PluginFacade, self).registerCommand(PluginFacade.STARTUP, controller.StartupCommand)

MAIN_APP_KEY = 'mainAppKey'

if __name__ == '__main__':
    qtapp = QtGui.QApplication(sys.argv)

    standalone_app = sa_main.StandaloneAppFacade.getInstance(key=MAIN_APP_KEY)

    # NOTE: remember to disable webview QURL open
    main_window = components.QtMainWindow()
    main_window.show()

    standalone_app.sendNotification(sa_main.StandaloneAppFacade.STARTUP, main_window)
    #user_facade = PluginFacade.getInstance("user")
    #if user_facade:
    #    user_facade.PLUGIN_NAME = "user"
    #    user_facade.sendNotification(PluginFacade.STARTUP, main_window)

    sys.exit(qtapp.exec_())
