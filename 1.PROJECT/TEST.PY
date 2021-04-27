        # 툴바 만들기
        self.toolbar = self.addToolBar('Exit')
        self.toolbar.addAction(exitAction)
        self.toolbar.addAction(editAction)
        self.toolbar.addAction(printAction)
        self.toolbar.addAction(helpAction)
        
        # 버튼 만들기
        quitbtn = QPushButton('Quit', self) #6
        QToolTip.setFont(QFont('SansSerif', 10))
        quitbtn.setToolTip('<b>QuitButton</b>')
        quitbtn.move(350, 100)
        quitbtn.resize(50, 20) #quitbtn.resize(quitbtn.sizeHint())
        ex1 = Calculator()
        quitbtn.clicked.connect(Calculator) #7
