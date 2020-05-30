from panda3d.core import PStatClient, Thread
from direct.directnotify import DirectNotifyGlobal
from direct.stdpy import threading
import atexit, subprocess, psutil, sys, os, wx, json

DEFAULT_TEXT = ''
DEFAULT_IMPORTS = '''from panda3d.core import *
from direct.actor.Actor import Actor
from direct.interval.IntervalGlobal import *
from direct.gui.DirectGui import *
'''
CLIENT = 0

class CustomDialog(wx.Dialog):

    def __init__(self, parent, caption, title, inputMethod):
        wx.Dialog.__init__(self, parent, -1, title)

        self.text = wx.StaticText(self, -1, caption)
        self.input = inputMethod(self)
        self.buttons = self.CreateButtonSizer(wx.OK | wx.CANCEL)
        self.sizer = wx.BoxSizer(wx.VERTICAL)

        self.sizer.Add(self.text, 0, wx.ALL, 5)
        self.sizer.Add(self.input, 1, wx.EXPAND | wx.ALL, 5)
        self.sizer.Add(self.buttons, 0, wx.EXPAND | wx.ALL, 5)
        self.SetSizerAndFit(self.sizer)
        self.input.SetFocus()
        self.Centre()

class ListDialog(CustomDialog):

    def __init__(self, parent, caption, title, choices):
        CustomDialog.__init__(self, parent, caption, title, lambda self: wx.ListBox(self, choices=sorted(choices)))

class InputDialog(CustomDialog):

    def __init__(self, parent, caption, title):
        CustomDialog.__init__(self, parent, caption, title, lambda self: wx.TextCtrl(self))

    def getInput(self):
        return self.input.GetValue()

class Injector(object):
    notify = DirectNotifyGlobal.directNotify.newCategory('Injector')

    def __init__(self):
        self.app = wx.App(redirect=False)
        self.frame = wx.Frame(None, title='Injector', size=(765, 325), style=wx.SYSTEM_MENU | wx.CAPTION | wx.MINIMIZE_BOX | wx.CLOSE_BOX | wx.RESIZE_BORDER)
        self.panel = wx.Panel(self.frame)

        self.buttonPanel = wx.Panel(self.panel)
        self.checkboxPanel = wx.Panel(self.panel)
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.buttonSizer = wx.BoxSizer(wx.HORIZONTAL)
        self.checkboxSizer = wx.BoxSizer(wx.HORIZONTAL)

        self.injectBox = wx.TextCtrl(parent=self.panel, style=wx.TE_MULTILINE | wx.TE_RICH2)
        self.injectButton = wx.Button(parent=self.buttonPanel, size=(100, 50), label='Inject')
        self.pstatsBox = wx.CheckBox(parent=self.checkboxPanel, label='PStats')

        self.injectBox.SetLabel(DEFAULT_TEXT)
        self.injectBox.Bind(wx.EVT_KEY_DOWN, self.__keyDown)
        self.injectButton.Bind(wx.EVT_BUTTON, lambda event: self.__inject(event, CLIENT))
        self.pstatsBox.Bind(wx.EVT_CHECKBOX, self.__pstats)

        self.addToSizer(self.buttonSizer, self.injectButton)
        self.addToSizer(self.checkboxSizer, self.pstatsBox)

        self.sizer.Add(self.checkboxPanel, 0, wx.ALIGN_CENTER)
        self.sizer.Add(self.injectBox, 1, wx.EXPAND)
        self.sizer.Add(self.buttonPanel, 0, wx.ALIGN_CENTER)

        self.buttonPanel.SetSizer(self.buttonSizer)
        self.panel.SetSizer(self.sizer)
        self.frame.SetMinSize((765, 325))
        self.frame.Show()

        atexit.register(self.__pstatCleanup)
        threading.Thread(target=self.app.MainLoop).start()

    def addToSizer(self, sizer, *args):
        for i, arg in enumerate(args):
            if i:
                sizer.AddSpacer(30)

            sizer.Add(arg)

    def info(self, parent, message, caption, icon=wx.ICON_INFORMATION, buttons=wx.OK):
        return wx.MessageDialog(parent, message, caption, buttons | icon).ShowModal() == wx.ID_YES

    def getPandaDirectory(self):
        return os.sep.join(sys.path[1].split(os.sep)[:-2])

    def getPStatsPath(self):
        return os.path.join(self.getPandaDirectory(), 'bin', 'pstats')

    def getProcesses(self, name):
        return [process for process in psutil.process_iter() if process.name().startswith(name)]

    def __keyDown(self, event):
        if event.GetKeyCode() == wx.WXK_TAB:
            self.injectBox.WriteText(' ' * 4)
        else:
            event.Skip()

    def __inject(self, event, type):
        injection = DEFAULT_IMPORTS + self.injectBox.GetValue()

        if type == CLIENT:
            exec(injection, globals())

    def __pstats(self, event):
        box = event.GetEventObject()
        box.Disable()

        if box.GetValue():
            if not self.getProcesses('pstats'):
                subprocess.Popen([self.getPStatsPath()])

            PStatClient.connect()
        else:
            PStatClient.disconnect()

            for process in self.getProcesses('pstats'):
                process.kill()

        taskMgr.doMethodLater(1, lambda task: box.Enable(), 'enableElement-%d' % id(box))

    def __pstatCleanup(self):
        if self.pstatsBox.GetValue():
            for process in self.getProcesses('pstats'):
                process.kill()
