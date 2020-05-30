# https://github.com/LittleNed/ToontownStride/blob/master/toontown/toonbase/ToontownTimer.py
# https://www.panda3d.org/manual/?title=DirectGUI
from direct.gui.DirectGui import DirectFrame, DGG
from direct.showbase.PythonUtil import bound
from direct.task import Task
from direct.task.TaskManagerGlobal import taskMgr
from pandac.PandaModules import Vec4

from src.gamebase import GameGlobals


class GameTimer(DirectFrame):
    ClockImage = None
    TimerId = 0

    def __init__(self, useImage = True, highlightNearEnd = True):
        if useImage:
            image = self.getImage()
        else:
            image = None
        DirectFrame.__init__(self, state=DGG.DISABLED, relief=None, scale=0.45, image=image, image_pos=(0, 0, 0), text='0', text_fg=(0, 0, 0, 1), text_font=GameGlobals.InterfaceFont, text_pos=(-0.01, -0.15), text_scale=0.35)
        self.timerId = GameTimer.TimerId
        GameTimer.TimerId += 1
        self.highlightNearEnd = highlightNearEnd
        self.countdownTask = None
        self.currentTime = 0
        self.taskTime = 0.0
        self.setFontColor(Vec4(0, 0, 0, 1))
        return

    def setFontColor(self, vColor):
        self.vFontColor = vColor

    def getImage(self):
        if GameTimer.ClockImage == None:
            model = loader.loadModel('phase_3.5/models/gui/clock_gui.bam')
            GameTimer.ClockImage = model.find('**/alarm_clock')
            model.removeNode()
        return GameTimer.ClockImage

    def posInTopRightCorner(self):
        self.reparentTo(base.a2dTopRight)
        self.setPos(-0.173, 0, -0.17)

    def setTime(self, time):
        time = bound(time, 0, 999)
        if time == self.currentTime:
            return

        self.currentTime = time
        timeStr = str(time)
        timeStrLen = len(timeStr)
        if timeStrLen == 1:
            if time <= 5 and self.highlightNearEnd:
                self.setTimeStr(timeStr, 0.34, (-0.025, -0.125), Vec4(1, 0, 0, 1))
            else:
                self.setTimeStr(timeStr, 0.34, (-0.025, -0.125))
        elif timeStrLen == 2:
            self.setTimeStr(timeStr, 0.27, (-0.025, -0.1))
        elif timeStrLen == 3:
            self.setTimeStr(timeStr, 0.2, (-0.01, -0.08))

    def setTimeStr(self, timeStr, scale = 0.2, pos = (-0.01, -0.08), fg = None):
        #self['text'] = ''
        self['text_fg'] = fg or self.vFontColor
        self['text_scale'] = scale
        self['text_pos'] = pos
        #self['text'] = timeStr

    def getElapsedTime(self):
        return self.taskTime

    def _timerTask(self, task):
        countdownTime = int(task.duration - task.time)
        self.setTime(countdownTime)
        self.taskTime = task.time
        if task.time >= task.duration:
            self.timerExpired()
            if task.callback:
                task.callback(*task.extraArgs)
            return Task.done
        else:
            return Task.cont

    def countdown(self, duration, callback = None):
        self.countdownTask = Task.Task(self._timerTask)
        self.countdownTask.duration = duration
        self.countdownTask.callback = callback
        taskMgr.remove('timerTask%s' % self.TimerId)
        return taskMgr.add(self.countdownTask, 'timerTask%s' % self.TimerId)

    def timerExpired(self):
        pass

    def stop(self):
        if self.countdownTask:
            taskMgr.remove(self.countdownTask)

    def reset(self):
        self.stop()
        self.setTime(0)
        taskMgr.remove('timerTask%s' % self.TimerId)
        self.taskTime = 0.0

    def destroy(self):
        self.reset()
        self.countdownTask = None
        DirectFrame.destroy(self)
        return

    def cleanup(self):
        self.destroy()
        self.notify.warning('Call destroy, not cleanup')
