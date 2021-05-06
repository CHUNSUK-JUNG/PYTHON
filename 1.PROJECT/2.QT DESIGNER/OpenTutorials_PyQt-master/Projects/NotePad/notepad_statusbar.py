#!/usr/bin/env python
# coding: utf-8

from PyQt5.QtWidgets import QStatusBar
from PyQt5.QtGui import QTextCursor
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtPrintSupport import *


class StatusBar(QStatusBar):
    @pyqtSlot(QTextCursor)
    def __init__(self):
        QStatusBar.__init__(self)
        self.setVisible(False)


    def change_cursor_info(self, data:QTextCursor):
        ss = data.selectionStart()
        se = data.selectionEnd()
        selected_info = ""
        if se - ss:
            selected_info = "{0}{1} 선택됨.".format(se - ss, "문자" if (se-ss) == 1 else "문자열")
        self.showMessage("{0} {1}행:{2}열".format(selected_info, data.blockNumber()+1, data.columnNumber()))