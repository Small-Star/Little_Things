# -*- coding: utf-8 -*-
"""
Created on Sat Nov 19 10:43:27 2016

"""
import sys
from PyQt4 import QtGui

class PR_GUI(QtGui.QMainWindow):
    
    def __init__(self):
        super(PR_GUI, self).__init__()
        
        self.initUI()
        
    def initUI(self):               
        
        #self.showFullScreen()
        self.resize(700,400)        
        self.center()
        self.statusBar().showMessage('Test')   
        self.setWindowTitle('TLT')   
        
        act_exit = QtGui.QAction(QtGui.QIcon('exit.png'), '&Exit', self)        
        act_exit.setShortcut('Ctrl+Q')
        act_exit.setStatusTip('Exit application')
        act_exit.triggered.connect(QtGui.qApp.quit)
        
        act_new_thing = QtGui.QAction('Add New Thing', self)
        act_new_thing.setStatusTip('Add a new thing to the rotation')
        
        act_profile_settings = QtGui.QAction('Profile Settings', self)
        act_profile_settings.setStatusTip('Setup a new user profile')
        
        act_show_history = QtGui.QAction('Show History', self)
        act_show_history.setStatusTip('View all of the principles in the rotation, along with statistics')

        act_play = QtGui.QAction(QtGui.QIcon('play.png'), 'Pla&Y', self)
        act_play.setShortcut('Ctrl+Y')
        act_play.setStatusTip('Play')
        
        act_pause = QtGui.QAction(QtGui.QIcon('pause.png'), '&Pause', self)
        act_pause.setShortcut('Ctrl+P')
        act_pause.setStatusTip('Pause')
        
        act_resume = QtGui.QAction(QtGui.QIcon('play.png'), '&Resume', self)
        act_resume.setShortcut('Ctrl+R')
        act_resume.setStatusTip('Resume where you left off')

        menubar = self.menuBar()
        mnu_file = menubar.addMenu('&File')
        mnu_settings = menubar.addMenu('&Settings')
        mnu_history = menubar.addMenu('&History')
        mnu_action = menubar.addMenu('&Action')
        
        mnu_file.addAction(act_exit)
        mnu_settings.addAction(act_new_thing)
        mnu_settings.addAction(act_profile_settings)
        mnu_history.addAction(act_show_history)
        mnu_action.addAction(act_play)   
        mnu_action.addAction(act_pause)        
        mnu_action.addAction(act_resume) 

        vbox = QtGui.QVBoxLayout()        
        hbox = QtGui.QHBoxLayout()
        
        vbox.addLayout(hbox)
        self.setLayout(vbox)  
        
        self.show()
        
    def center(self):
        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        
        
def main(): 
    app = QtGui.QApplication(sys.argv)
    win = PR_GUI()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()     