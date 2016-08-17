'''
Created on Aug 15, 2016

@author: Jacob
'''
from PyQt4 import QtCore, QtGui
from GuiMethods import GuiMethods
class Ui_MainWindow():
    def __init__(self, Directory):
        self.methods = GuiMethods(Directory)
        self.methods.printShit()
    def setupUi(self, MainWindow):
        '''
        Set up gui window
        '''
        font = QtGui.QFont()
        font.setFamily("Arial")
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowTitle("Harambe\'s Chivalry Data Cruncher")
        MainWindow.resize(1084, 813)
        MainWindow.setFont(font)
        self.centralwidget = QtGui.QWidget(MainWindow)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        MainWindow.setStatusBar(self.statusbar)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        #=======================================================================
        # Handles Creation of 3 sub sections and adds them to a grid layout
        #=======================================================================
        self.MatchInputs()
        self.DataVisualization()
        self.Tabs()
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)        
        self.gridLayout.addWidget(self.DataVisualizationGroupBox, 1, 0, 1, 1)        
        self.gridLayout.addWidget(self.ContainerBottom, 2, 0, 1, 1, QtCore.Qt.AlignBottom)        
        self.gridLayout.addWidget(self.MatchInputsGroupBox, 0, 0, 1, 1)
    def MatchInputs(self):
        '''
        Fills Top Subsection with necessary objects
        '''
        #Match Inputs Group Box
        self.MatchInputsGroupBox = QtGui.QGroupBox(self.centralwidget)
        self.MatchInputsGroupBox.setFont(self.font(12, True, 75))
        self.MatchInputsGroupBox.setTitle("Match Inputs")
        #Label 'Match Count'
        self.MatchNumberLabel = QtGui.QLabel(self.MatchInputsGroupBox)
        self.MatchNumberLabel.setFont(self.font(10, False, 50))
        self.MatchNumberLabel.setText("Match Count")
        #Match SpinBox
        self.matchNumberSpinBox = QtGui.QSpinBox(self.MatchInputsGroupBox)
        self.matchNumberSpinBox.setFont(self.font(10, False, 50))
        #Create Match Push Button
        self.CreateMatchPushBtn = QtGui.QPushButton(self.MatchInputsGroupBox)
        self.CreateMatchPushBtn.setFont(self.font(10, False, 50))
        self.CreateMatchPushBtn.setText("Create Match")
        #Reload Push Button
        self.ReloadDataPushBtn = QtGui.QPushButton(self.MatchInputsGroupBox)
        self.ReloadDataPushBtn.setFont(self.font(10, False, 50))
        self.ReloadDataPushBtn.setText("Reload Data")
        #Progress Bar
        self.progressBar = QtGui.QProgressBar(self.MatchInputsGroupBox)
        self.progressBar.setFont(self.font(10, False, 50))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setTextVisible(False)
        #Error Line Text Line
        self.ErrorTextLine = QtGui.QLineEdit(self.MatchInputsGroupBox)
        self.ErrorTextLine.setFont(self.font(10, False, 50))
        self.ErrorTextLine.setText("Error 1.242342")
        #Layout
        self.horizontalLayoutTop = QtGui.QHBoxLayout(self.MatchInputsGroupBox)
        self.horizontalLayoutTop.addWidget(self.MatchNumberLabel)
        self.horizontalLayoutTop.addWidget(self.matchNumberSpinBox)
        self.horizontalLayoutTop.addWidget(self.CreateMatchPushBtn)
        self.horizontalLayoutTop.addWidget(self.ReloadDataPushBtn)
        self.horizontalLayoutTop.addWidget(self.progressBar)
        self.horizontalLayoutTop.addWidget(self.ErrorTextLine)
    def DataVisualization(self):
        '''
        Fills middle section with necessary objects
        '''
        #Data Visualization Group Box
        self.DataVisualizationGroupBox = QtGui.QGroupBox(self.centralwidget)
        self.DataVisualizationGroupBox.setFont(self.font(12, True, 75))
        self.DataVisualizationGroupBox.setTitle("Data Visualization")
        #Graphic View Left
        self.graphicsViewLeft = QtGui.QGraphicsView(self.DataVisualizationGroupBox)
        #Graphic View Right
        self.graphicsViewRight = QtGui.QGraphicsView(self.DataVisualizationGroupBox)
        #Layout
        self.horizontalLayout = QtGui.QHBoxLayout(self.DataVisualizationGroupBox)
        self.horizontalLayout.addWidget(self.graphicsViewLeft)
        self.horizontalLayout.addWidget(self.graphicsViewRight)
    def Tabs(self):
        self.ContainerBottom = QtGui.QWidget(self.centralwidget)
        def TabsLeft():
            def dataTabLeft():
                def DataSelectionGroupBoxLeft():
                    #Data Selection Group Box
                    self.DataSelectionGroupBoxLeft = QtGui.QGroupBox(self.dataTabLeft)
                    self.DataSelectionGroupBoxLeft.setFont(self.font(12, True, 75))
                    self.DataSelectionGroupBoxLeft.setTitle("Data Selection")
                    #Label "Match"
                    self.matchLabelLeft = QtGui.QLabel(self.DataSelectionGroupBoxLeft)
                    self.matchLabelLeft.setFont(self.font(10, False, 50))
                    self.matchLabelLeft.setText("Match")
                    #Match Combo Box
                    self.matchComboBoxLeft = QtGui.QComboBox(self.DataSelectionGroupBoxLeft)
                    self.matchComboBoxLeft.setFont(self.font(10, False, 50))
                    self.matchComboBoxLeft.addItem("")
                    self.matchComboBoxLeft.setItemText(0, "")
                    self.matchComboBoxLeft.addItem("")
                    self.matchComboBoxLeft.addItem("")
                    self.matchComboBoxLeft.setItemText(1, "Number One")
                    self.matchComboBoxLeft.setItemText(2, "Number Two")                    
                    #Label "Half"
                    self.halfLabelLeft = QtGui.QLabel(self.DataSelectionGroupBoxLeft)
                    self.halfLabelLeft.setFont(self.font(10, False, 50))
                    self.halfLabelLeft.setText("Half")
                    #Half Combo Box
                    self.halfComboBoxLeft = QtGui.QComboBox(self.DataSelectionGroupBoxLeft)
                    self.halfComboBoxLeft.setFont(self.font(10, False, 50))
                    self.halfComboBoxLeft.addItem("")
                    self.halfComboBoxLeft.setItemText(0, "")
                    self.halfComboBoxLeft.addItem("")
                    self.halfComboBoxLeft.addItem("")
                    self.halfComboBoxLeft.setItemText(1, "Number One")
                    self.halfComboBoxLeft.setItemText(2, "Number Two")                    
                    #Label "Player"
                    self.playerLabelLeft = QtGui.QLabel(self.DataSelectionGroupBoxLeft)
                    self.playerLabelLeft.setFont(self.font(10, False, 50))
                    self.playerLabelLeft.setText("Player")
                    #Player Combo Box
                    self.playerComboBoxLeft = QtGui.QComboBox(self.DataSelectionGroupBoxLeft)
                    self.playerComboBoxLeft.setFont(self.font(10, False, 50))
                    self.playerComboBoxLeft.addItem("")
                    self.playerComboBoxLeft.setItemText(0, "")
                    self.playerComboBoxLeft.addItem("")
                    self.playerComboBoxLeft.setItemText(1,"Crimson King")
                    #Label "Team"
                    self.teamLabelLeft = QtGui.QLabel(self.DataSelectionGroupBoxLeft)
                    self.teamLabelLeft.setFont(self.font(10, False, 50))
                    self.teamLabelLeft.setText("Team")
                    #Team Combo Box
                    self.teamComboBoxLeft = QtGui.QComboBox(self.DataSelectionGroupBoxLeft)
                    self.teamComboBoxLeft.setFont(self.font(10, False, 50))
                    self.teamComboBoxLeft.addItem("")
                    self.teamComboBoxLeft.setItemText(0, "")
                    self.teamComboBoxLeft.addItem("")
                    self.teamComboBoxLeft.setItemText(1,"Harambe")
                    #Find Button
                    self.findBtnLeft = QtGui.QPushButton(self.DataSelectionGroupBoxLeft)
                    self.findBtnLeft.setFont(self.font(10, False, 50))
                    self.findBtnLeft.setText("Find")
                    #Clear Button
                    self.clearBtnLeft = QtGui.QPushButton(self.DataSelectionGroupBoxLeft)
                    self.clearBtnLeft.setFont(self.font(10, False, 50))
                    self.clearBtnLeft.setText("Clear")                    
                    #Layout
                    self.DataSelectionGroupBoxLeftGrid = QtGui.QGridLayout(self.DataSelectionGroupBoxLeft)
                    self.DataSelectionGroupBoxLeftGrid.addWidget(self.matchLabelLeft, 0, 0, 1, 1)
                    self.DataSelectionGroupBoxLeftGrid.addWidget(self.matchComboBoxLeft, 1, 0, 1, 1, QtCore.Qt.AlignBottom)
                    self.DataSelectionGroupBoxLeftGrid.addWidget(self.halfLabelLeft, 2, 0, 1, 1, QtCore.Qt.AlignBottom)
                    self.DataSelectionGroupBoxLeftGrid.addWidget(self.halfComboBoxLeft, 3, 0, 1, 1, QtCore.Qt.AlignBottom)
                    self.DataSelectionGroupBoxLeftGrid.addWidget(self.teamLabelLeft, 4, 0, 1, 1, QtCore.Qt.AlignBottom)
                    self.DataSelectionGroupBoxLeftGrid.addWidget(self.teamComboBoxLeft, 5, 0, 1, 1, QtCore.Qt.AlignBottom)
                    self.DataSelectionGroupBoxLeftGrid.addWidget(self.playerLabelLeft, 6, 0, 1, 1, QtCore.Qt.AlignBottom)
                    self.DataSelectionGroupBoxLeftGrid.addWidget(self.playerComboBoxLeft, 7, 0, 1, 1, QtCore.Qt.AlignBottom)
                    self.DataSelectionGroupBoxLeftGrid.addWidget(self.findBtnLeft, 8, 0, 1, 1, QtCore.Qt.AlignBottom)
                    self.DataSelectionGroupBoxLeftGrid.addWidget(self.clearBtnLeft, 9, 0, 1, 1, QtCore.Qt.AlignBottom)
                self.dataTabLeft = QtGui.QWidget()
                DataSelectionGroupBoxLeft()
                self.dataTabLeftGrid = QtGui.QGridLayout(self.dataTabLeft)            
                self.dataTabLeftGrid.addWidget(self.DataSelectionGroupBoxLeft, 0, 0, 1, 1)
                self.tabsLeft.addTab(self.dataTabLeft, "Data Selection")
            def teamTabLeft():
                def teamGroupBoxLeft():
                    #Team Group Box
                    self.teamGroupBoxLeft = QtGui.QGroupBox(self.teamTabLeft)
                    self.teamGroupBoxLeft.setFont(self.font(12, True, 75))
                    self.teamGroupBoxLeft.setTitle("Team")
                    #Team Label
                    self.teamNameLeft = QtGui.QLabel(self.teamGroupBoxLeft)
                    self.teamNameLeft.setFont(self.font(14, False, 50))
                    self.teamNameLeft.setText("Accolade")
                    #Line
                    self.lineLeft = QtGui.QFrame(self.teamGroupBoxLeft)
                    self.lineLeft.setFrameShape(QtGui.QFrame.HLine)
                    self.lineLeft.setFrameShadow(QtGui.QFrame.Sunken)
                    #Wins Label
                    self.winsLeft = QtGui.QLabel(self.teamGroupBoxLeft)
                    self.winsLeft.setFont(self.font(10, False, 50))
                    self.winsLeft.setText("Wins: ")
                    #Losses Label
                    self.lossesLeft = QtGui.QLabel(self.teamGroupBoxLeft)
                    self.lossesLeft.setFont(self.font(10, False, 50))
                    self.lossesLeft.setText("Losses:")
                    #Win Loss Ration Label
                    self.wLRatioLeft = QtGui.QLabel(self.teamGroupBoxLeft)
                    self.wLRatioLeft.setFont(self.font(10, False, 50))
                    self.wLRatioLeft.setText("Win Loss Ratio :")
                    #Other Label
                    self.otherLeft = QtGui.QLabel(self.teamGroupBoxLeft)
                    self.otherLeft.setFont(self.font(10, False, 50))
                    self.otherLeft.setText("Other :")
                    #Data Visualization Button
                    self.dataVizTeamLeft_1 = QtGui.QPushButton(self.teamGroupBoxLeft)
                    self.dataVizTeamLeft_1.setFont(self.font(10, False, 50))
                    self.dataVizTeamLeft_1.setText("Data Viz ")
                    #Data Visualization Button
                    self.dataVizTeamLeft_2 = QtGui.QPushButton(self.teamGroupBoxLeft)
                    self.dataVizTeamLeft_2.setFont(self.font(10, False, 50))
                    self.dataVizTeamLeft_2.setText("Data Viz ")
                    #Data Visualization Button
                    self.dataVizTeamLeft_3 = QtGui.QPushButton(self.teamGroupBoxLeft)
                    self.dataVizTeamLeft_3.setFont(self.font(10, False, 50))
                    self.dataVizTeamLeft_3.setText("Data Viz ")
                    #Data Visualization Button
                    self.dataVizTeamLeft_4 = QtGui.QPushButton(self.teamGroupBoxLeft)
                    self.dataVizTeamLeft_4.setFont(self.font(10, False, 50))
                    self.dataVizTeamLeft_4.setText("Data Viz ")
                    #Layout
                    self.teamGroupBoxLeftGrid = QtGui.QGridLayout(self.teamGroupBoxLeft)
                    self.teamGroupBoxLeftGrid.addWidget(self.teamNameLeft, 0, 0, 1, 1)
                    self.teamGroupBoxLeftGrid.addWidget(self.lineLeft, 1, 0, 1, 1)
                    self.teamGroupBoxLeftGrid.addWidget(self.winsLeft, 2, 0, 1, 1)
                    self.teamGroupBoxLeftGrid.addWidget(self.lossesLeft, 3, 0, 1, 1)
                    self.teamGroupBoxLeftGrid.addWidget(self.wLRatioLeft, 4, 0, 1, 1)
                    self.teamGroupBoxLeftGrid.addWidget(self.otherLeft, 5, 0, 1, 1)
                    self.teamGroupBoxLeftGrid.addWidget(self.dataVizTeamLeft_1, 6, 0, 1, 1)
                    self.teamGroupBoxLeftGrid.addWidget(self.dataVizTeamLeft_2, 7, 0, 1, 1)
                    self.teamGroupBoxLeftGrid.addWidget(self.dataVizTeamLeft_3, 8, 0, 1, 1)
                    self.teamGroupBoxLeftGrid.addWidget(self.dataVizTeamLeft_4, 9, 0, 1, 1)
                self.teamTabLeft = QtGui.QWidget()
                teamGroupBoxLeft()
                self.teamTabLeftGrid = QtGui.QGridLayout(self.teamTabLeft)
                self.teamTabLeftGrid.addWidget(self.teamGroupBoxLeft, 0, 0, 1, 1)
                self.tabsLeft.addTab(self.teamTabLeft, "Team")
            def playerTabLeft():
                def PlayerGroupBoxLeft():
                    #Player Group Box
                    self.PlayerGroupBoxLeft = QtGui.QGroupBox(self.playerTabLeft)
                    self.PlayerGroupBoxLeft.setFont(self.font(12, True, 75))
                    self.PlayerGroupBoxLeft.setTitle("Player")
                    #Player Label
                    self.playerNameLabelLeft = QtGui.QLabel(self.PlayerGroupBoxLeft)
                    self.playerNameLabelLeft.setFont(self.font(14, False, 50))
                    self.playerNameLabelLeft.setText("Crimson King")
                    #Line
                    self.lineLeft_2 = QtGui.QFrame(self.PlayerGroupBoxLeft)
                    self.lineLeft_2.setFrameShape(QtGui.QFrame.HLine)
                    self.lineLeft_2.setFrameShadow(QtGui.QFrame.Sunken)
                    #Kills Label
                    self.killsLeft = QtGui.QLabel(self.PlayerGroupBoxLeft)
                    self.killsLeft.setFont(self.font(10, False, 50))
                    self.killsLeft.setText("Kills:")
                    #Deaths Label
                    self.deathsLeft = QtGui.QLabel(self.PlayerGroupBoxLeft)
                    self.deathsLeft.setFont(self.font(10, False, 50))
                    self.deathsLeft.setText("Deaths:")
                    #Assists Label
                    self.assistsLeft = QtGui.QLabel(self.PlayerGroupBoxLeft)
                    self.assistsLeft.setFont(self.font(10, False, 50))
                    self.assistsLeft.setText("Assists:")
                    #Kill Death Ratio Label
                    self.kDRatioLeft = QtGui.QLabel(self.PlayerGroupBoxLeft)
                    self.kDRatioLeft.setFont(self.font(10, False, 50))
                    self.kDRatioLeft.setText("K/D Ratio:")
                    #Is Archer Label
                    self.isArcherLeft = QtGui.QLabel(self.PlayerGroupBoxLeft)
                    self.isArcherLeft.setFont(self.font(10, False, 50))
                    self.isArcherLeft.setText("Is Archer:")
                    #Data Visualization Button
                    self.dataVizPlayerLeft_1 = QtGui.QPushButton(self.PlayerGroupBoxLeft)
                    self.dataVizPlayerLeft_1.setFont(self.font(10, False, 50))
                    self.dataVizPlayerLeft_1.setText("Data Viz ")
                    #Data Visualization Button
                    self.dataVizPlayerLeft_2 = QtGui.QPushButton(self.PlayerGroupBoxLeft)
                    self.dataVizPlayerLeft_2.setFont(self.font(10, False, 50))
                    self.dataVizPlayerLeft_2.setText("Data Viz ")
                    #Data Visualization Button
                    self.dataVizPlayerLeft_3 = QtGui.QPushButton(self.PlayerGroupBoxLeft)
                    self.dataVizPlayerLeft_3.setFont(self.font(10, False, 50))
                    self.dataVizPlayerLeft_3.setText("Data Viz ")
                    #Data Visualization Button
                    self.dataVizPlayerLeft_4 = QtGui.QPushButton(self.PlayerGroupBoxLeft)
                    self.dataVizPlayerLeft_4.setFont(self.font(10, False, 50))
                    self.dataVizPlayerLeft_4.setText("Data Viz ")
                    #Layouts
                    self.PlayerGroupBoxLeftGrid = QtGui.QVBoxLayout(self.PlayerGroupBoxLeft)
                    self.PlayerGroupBoxLeftGrid.addWidget(self.playerNameLabelLeft)
                    self.PlayerGroupBoxLeftGrid.addWidget(self.lineLeft_2)
                    self.PlayerGroupBoxLeftGrid.addWidget(self.killsLeft, QtCore.Qt.AlignBottom)
                    self.PlayerGroupBoxLeftGrid.addWidget(self.deathsLeft, QtCore.Qt.AlignBottom)
                    self.PlayerGroupBoxLeftGrid.addWidget(self.assistsLeft, QtCore.Qt.AlignBottom)
                    self.PlayerGroupBoxLeftGrid.addWidget(self.kDRatioLeft, QtCore.Qt.AlignBottom)
                    self.PlayerGroupBoxLeftGrid.addWidget(self.isArcherLeft, QtCore.Qt.AlignBottom)
                    self.PlayerGroupBoxLeftGrid.addWidget(self.dataVizPlayerLeft_1)
                    self.PlayerGroupBoxLeftGrid.addWidget(self.dataVizPlayerLeft_2)
                    self.PlayerGroupBoxLeftGrid.addWidget(self.dataVizPlayerLeft_3)
                    self.PlayerGroupBoxLeftGrid.addWidget(self.dataVizPlayerLeft_4)
                self.playerTabLeft = QtGui.QWidget()
                PlayerGroupBoxLeft()
                self.playerTabLeftGrid = QtGui.QGridLayout(self.playerTabLeft)
                self.playerTabLeftGrid.addWidget(self.PlayerGroupBoxLeft, 0, 0, 1, 1, QtCore.Qt.AlignBottom)
                self.tabsLeft.addTab(self.playerTabLeft, "")
                self.tabsLeft.setTabText(self.tabsLeft.indexOf(self.playerTabLeft), "Player")
            def tournamentLeft():
                def TournamentGroupBoxLeft():
                    #Tournament Group Box
                    self.TournamentGroupBoxLeft = QtGui.QGroupBox(self.tournamentLeft)
                    self.TournamentGroupBoxLeft.setFont(self.font(12, True, 75)) 
                    self.TournamentGroupBoxLeft.setTitle("Tournament")
                    #Tournament Button
                    self.tournamentBtnLeft_1 = QtGui.QPushButton(self.TournamentGroupBoxLeft)
                    self.tournamentBtnLeft_1.setFont(self.font(10, False, 50)) 
                    self.tournamentBtnLeft_1.setText("tournamnetBtn1")      
                    #Tournament Button 
                    self.tournamentBtnLeft_2 = QtGui.QPushButton(self.TournamentGroupBoxLeft)
                    self.tournamentBtnLeft_2.setFont(self.font(10, False, 50)) 
                    self.tournamentBtnLeft_2.setText("tournamnetBtn2")  
                    #Tournament Button   
                    self.tournamentBtnLeft_3 = QtGui.QPushButton(self.TournamentGroupBoxLeft)
                    self.tournamentBtnLeft_3.setFont(self.font(10, False, 50))   
                    self.tournamentBtnLeft_3.setText("tournamnetBtn3") 
                    #Tournament Button
                    self.tournamentBtnLeft_4 = QtGui.QPushButton(self.TournamentGroupBoxLeft)
                    self.tournamentBtnLeft_4.setFont(self.font(10, False, 50)) 
                    self.tournamentBtnLeft_4.setText("tournamnetBtn4")   
                    #Tournament Button   
                    self.tournamentBtnLeft_5 = QtGui.QPushButton(self.TournamentGroupBoxLeft)
                    self.tournamentBtnLeft_5.setFont(self.font(10, False, 50))
                    self.tournamentBtnLeft_5.setText("tournamnetBtn5")  
                    #Layout
                    self.TournamentGroupBoxLeftGrid = QtGui.QGridLayout(self.TournamentGroupBoxLeft)
                    self.TournamentGroupBoxLeftGrid.addWidget(self.tournamentBtnLeft_1, 0, 0, 1, 1)
                    self.TournamentGroupBoxLeftGrid.addWidget(self.tournamentBtnLeft_2, 1, 0, 1, 1)
                    self.TournamentGroupBoxLeftGrid.addWidget(self.tournamentBtnLeft_3, 2, 0, 1, 1)
                    self.TournamentGroupBoxLeftGrid.addWidget(self.tournamentBtnLeft_4, 3, 0, 1, 1)
                    self.TournamentGroupBoxLeftGrid.addWidget(self.tournamentBtnLeft_5, 4, 0, 1, 1)
                self.tournamentLeft = QtGui.QWidget()
                TournamentGroupBoxLeft()
                self.tournamentLeftGrid = QtGui.QGridLayout(self.tournamentLeft)
                self.tournamentLeftGrid.addWidget(self.TournamentGroupBoxLeft, 0, 0, 1, 1)
                self.tabsLeft.addTab(self.tournamentLeft, "")
                self.tabsLeft.setTabText(self.tabsLeft.indexOf(self.tournamentLeft), "Tournament") 
            self.tabsLeft = QtGui.QTabWidget(self.ContainerBottom)
            dataTabLeft()
            teamTabLeft()
            playerTabLeft()
            tournamentLeft()
            self.tabsLeft.setCurrentIndex(0)
        def TabsRight():
            self.tabsRight = QtGui.QTabWidget(self.ContainerBottom) 
            def dataTabRight():
                def DataSelectionGroupBoxRight():
                    #Data Selection Group Box
                    self.DataSelectionGroupBoxRight = QtGui.QGroupBox(self.dataTabRight)
                    self.DataSelectionGroupBoxRight.setFont(self.font(12, True, 75))
                    self.DataSelectionGroupBoxRight.setTitle("Data Selection")
                    #Player Label
                    self.playerLabelRight = QtGui.QLabel(self.DataSelectionGroupBoxRight)
                    self.playerLabelRight.setFont(self.font(10, False, 50))
                    self.playerLabelRight.setText("Player")
                    #Half Combo Box
                    self.halfComboBoxRight = QtGui.QComboBox(self.DataSelectionGroupBoxRight)
                    self.halfComboBoxRight.setFont(self.font(10, False, 50))
                    self.halfComboBoxRight.addItem("")
                    self.halfComboBoxRight.setItemText(0, "")
                    self.halfComboBoxRight.addItem("")
                    self.halfComboBoxRight.addItem("")
                    self.halfComboBoxRight.setItemText(1, "Number One")
                    self.halfComboBoxRight.setItemText(2, "Number Two")
                    #Match Label
                    self.matchLabelRight = QtGui.QLabel(self.DataSelectionGroupBoxRight)
                    self.matchLabelRight.setFont(self.font(10, False, 50))
                    self.matchLabelRight.setText("Match")
                    #Match Combo Box
                    self.matchComboBoxRight = QtGui.QComboBox(self.DataSelectionGroupBoxRight)
                    self.matchComboBoxRight.setFont(self.font(10, False, 50))
                    self.matchComboBoxRight.addItem("")
                    self.matchComboBoxRight.setItemText(0, "")
                    self.matchComboBoxRight.addItem("")
                    self.matchComboBoxRight.addItem("")
                    self.matchComboBoxRight.setItemText(1, "Number One")
                    self.matchComboBoxRight.setItemText(2, "Number Two")
                    #Clear Button
                    self.clearBtnRight = QtGui.QPushButton(self.DataSelectionGroupBoxRight)
                    self.clearBtnRight.setFont(self.font(10, False, 50))
                    self.clearBtnRight.setText("Clear")
                    #Find Button
                    self.findBtnRight = QtGui.QPushButton(self.DataSelectionGroupBoxRight)
                    self.findBtnRight.setFont(self.font(10, False, 50))
                    self.findBtnRight.setText("Find")
                    #Half Label
                    self.halfLabelRight = QtGui.QLabel(self.DataSelectionGroupBoxRight)
                    self.halfLabelRight.setFont(self.font(10, False, 50))
                    self.halfLabelRight.setText("Half")
                    #Player Combo Box
                    self.playerComboBoxRight = QtGui.QComboBox(self.DataSelectionGroupBoxRight)
                    self.playerComboBoxRight.setFont(self.font(10, False, 50))
                    self.playerComboBoxRight.addItem("")
                    self.playerComboBoxRight.setItemText(0, "")
                    self.playerComboBoxRight.addItem("")
                    self.playerComboBoxRight.setItemText(1, "Crimson King")
                    #Team Label
                    self.teamLabelRight = QtGui.QLabel(self.DataSelectionGroupBoxRight)
                    self.teamLabelRight.setFont(self.font(10, False, 50))
                    self.teamLabelRight.setText("Team")
                    #Team Combo Box
                    self.teamComboBoxRight = QtGui.QComboBox(self.DataSelectionGroupBoxRight)
                    self.teamComboBoxRight.setFont(self.font(10, False, 50))
                    self.teamComboBoxRight.addItem("")
                    self.teamComboBoxRight.setItemText(0, "")
                    self.teamComboBoxRight.addItem("") 
                    self.teamComboBoxRight.setItemText(1, "Harambe")
                    #Layout
                    self.DataSelectionGroupBoxRightGrid = QtGui.QGridLayout(self.DataSelectionGroupBoxRight)
                    self.DataSelectionGroupBoxRightGrid.addWidget(self.playerLabelRight, 7, 0, 1, 1, QtCore.Qt.AlignBottom)
                    self.DataSelectionGroupBoxRightGrid.addWidget(self.halfComboBoxRight, 3, 0, 1, 1, QtCore.Qt.AlignBottom)
                    self.DataSelectionGroupBoxRightGrid.addWidget(self.matchLabelRight, 0, 0, 1, 1)
                    self.DataSelectionGroupBoxRightGrid.addWidget(self.matchComboBoxRight, 1, 0, 1, 1, QtCore.Qt.AlignBottom)
                    self.DataSelectionGroupBoxRightGrid.addWidget(self.clearBtnRight, 10, 0, 1, 1, QtCore.Qt.AlignBottom)
                    self.DataSelectionGroupBoxRightGrid.addWidget(self.findBtnRight, 9, 0, 1, 1, QtCore.Qt.AlignBottom)
                    self.DataSelectionGroupBoxRightGrid.addWidget(self.halfLabelRight, 2, 0, 1, 1, QtCore.Qt.AlignBottom)
                    self.DataSelectionGroupBoxRightGrid.addWidget(self.playerComboBoxRight, 8, 0, 1, 1, QtCore.Qt.AlignBottom)
                    self.DataSelectionGroupBoxRightGrid.addWidget(self.teamLabelRight, 4, 0, 1, 1, QtCore.Qt.AlignBottom)
                    self.DataSelectionGroupBoxRightGrid.addWidget(self.teamComboBoxRight, 5, 0, 1, 1)          
                self.dataTabRight = QtGui.QWidget()
                self.dataTabRightGrid = QtGui.QGridLayout(self.dataTabRight)
                DataSelectionGroupBoxRight()
                self.dataTabRightGrid.addWidget(self.DataSelectionGroupBoxRight, 0, 0, 1, 1) 
                self.tabsRight.addTab(self.dataTabRight, "Data Selection")
            def teamTabRight():
                def teamGroupBoxRight():
                    #Team Group Box
                    self.teamGroupBoxRight = QtGui.QGroupBox(self.teamTabRight)
                    self.teamGroupBoxRight.setFont(self.font(12, True, 75))
                    self.teamGroupBoxRight.setTitle("Team")
                    #Team Label
                    self.teamNameRight = QtGui.QLabel(self.teamGroupBoxRight)
                    self.teamNameRight.setFont(self.font(14, False, 50))
                    self.teamNameRight.setText("Accolade")
                    #Line
                    self.lineRight = QtGui.QFrame(self.teamGroupBoxRight)
                    self.lineRight.setFrameShape(QtGui.QFrame.HLine)
                    self.lineRight.setFrameShadow(QtGui.QFrame.Sunken)
                    #Win Label
                    self.winsRight = QtGui.QLabel(self.teamGroupBoxRight)
                    self.winsRight.setFont(self.font(10, False, 50))
                    self.winsRight.setText("Wins: ")
                    #Losses Label
                    self.lossesRight = QtGui.QLabel(self.teamGroupBoxRight)
                    self.lossesRight.setFont(self.font(10, False, 50))
                    self.lossesRight.setText("Losses:")
                    #Win Loss Ratio Label
                    self.wLRatioRight = QtGui.QLabel(self.teamGroupBoxRight)
                    self.wLRatioRight.setFont(self.font(10, False, 50))
                    self.wLRatioRight.setText("Win Loss Ratio :")
                    #Other Label
                    self.otherRight = QtGui.QLabel(self.teamGroupBoxRight)
                    self.otherRight.setFont(self.font(10, False, 50))
                    self.otherRight.setText("Other :")
                    #Data Visualization Button
                    self.dataVizTeamRight_1 = QtGui.QPushButton(self.teamGroupBoxRight)
                    self.dataVizTeamRight_1.setFont(self.font(10, False, 50))
                    self.dataVizTeamRight_1.setText("Data Viz ")    
                    #Data Visualization Button
                    self.dataVizTeamRight_2 = QtGui.QPushButton(self.teamGroupBoxRight)
                    self.dataVizTeamRight_2.setFont(self.font(10, False, 50))
                    self.dataVizTeamRight_2.setText("Data Viz ")  
                    #Data Visualization Button
                    self.dataVizTeamRight_3 = QtGui.QPushButton(self.teamGroupBoxRight)
                    self.dataVizTeamRight_3.setFont(self.font(10, False, 50))
                    self.dataVizTeamRight_3.setText("Data Viz ")
                    #Data Visualization Button
                    self.dataVizTeamRight_4 = QtGui.QPushButton(self.teamGroupBoxRight)
                    self.dataVizTeamRight_4.setFont(self.font(10, False, 50))
                    self.dataVizTeamRight_4.setText("Data Viz ")
                    #Layout
                    self.gridLayout_10 = QtGui.QGridLayout(self.teamGroupBoxRight)
                    self.gridLayout_10.addWidget(self.teamNameRight, 0, 0, 1, 1)
                    self.gridLayout_10.addWidget(self.lineRight, 1, 0, 1, 1)
                    self.gridLayout_10.addWidget(self.winsRight, 2, 0, 1, 1)
                    self.gridLayout_10.addWidget(self.lossesRight, 3, 0, 1, 1)
                    self.gridLayout_10.addWidget(self.wLRatioRight, 4, 0, 1, 1)
                    self.gridLayout_10.addWidget(self.otherRight, 5, 0, 1, 1)
                    self.gridLayout_10.addWidget(self.dataVizTeamRight_1, 6, 0, 1, 1)
                    self.gridLayout_10.addWidget(self.dataVizTeamRight_2, 7, 0, 1, 1)
                    self.gridLayout_10.addWidget(self.dataVizTeamRight_3, 8, 0, 1, 1)
                    self.gridLayout_10.addWidget(self.dataVizTeamRight_4, 9, 0, 1, 1)
                self.teamTabRight = QtGui.QWidget()
                self.teamTabRightGrid = QtGui.QGridLayout(self.teamTabRight)
                teamGroupBoxRight()
                self.teamTabRightGrid.addWidget(self.teamGroupBoxRight, 0, 0, 1, 1)
                self.tabsRight.addTab(self.teamTabRight, "")
                self.tabsRight.setTabText(self.tabsRight.indexOf(self.teamTabRight), "Team")
            def playerTabRight():
                def PlayerGroupBoxRight():
                    #Player Group Box
                    self.PlayerGroupBoxRight = QtGui.QGroupBox(self.playerTabRight)
                    self.PlayerGroupBoxRight.setFont(self.font(12, True, 75))
                    self.PlayerGroupBoxRight.setTitle("Player")
                    #Player Label
                    self.playerNameLabelRight = QtGui.QLabel(self.PlayerGroupBoxRight)
                    self.playerNameLabelRight.setFont(self.font(14, False, 50))
                    self.playerNameLabelRight.setText("Crimson King")
                    #Line 
                    self.lineRight_2 = QtGui.QFrame(self.PlayerGroupBoxRight)
                    self.lineRight_2.setFrameShape(QtGui.QFrame.HLine)
                    self.lineRight_2.setFrameShadow(QtGui.QFrame.Sunken)
                    #Kills label
                    self.killsRight = QtGui.QLabel(self.PlayerGroupBoxRight)
                    self.killsRight.setFont(self.font(10, False, 50))
                    self.killsRight.setText("Kills:")
                    #Deaths Label
                    self.deathsRight = QtGui.QLabel(self.PlayerGroupBoxRight)
                    self.deathsRight.setFont(self.font(10, False, 50))
                    self.deathsRight.setText("Deaths:")
                    #Assists Label
                    self.assistsRight = QtGui.QLabel(self.PlayerGroupBoxRight)
                    self.assistsRight.setFont(self.font(10, False, 50))
                    self.assistsRight.setText("Assists:")
                    #Kill Death Ratio Label
                    self.kDRatioRight = QtGui.QLabel(self.PlayerGroupBoxRight)
                    self.kDRatioRight.setFont(self.font(10, False, 50))
                    self.kDRatioRight.setText("K/D Ratio:")
                    #Is Archer Label
                    self.isArcherRight = QtGui.QLabel(self.PlayerGroupBoxRight)
                    self.isArcherRight.setFont(self.font(10, False, 50))
                    self.isArcherRight.setText("Is Archer:")
                    #Data Visualization Button
                    self.dataVizPlayerRight_1 = QtGui.QPushButton(self.PlayerGroupBoxRight)
                    self.dataVizPlayerRight_1.setFont(self.font(10, False, 50))
                    self.dataVizPlayerRight_1.setText("Data Viz ")
                    #Data Visualization Button
                    self.dataVizPlayerRight_2 = QtGui.QPushButton(self.PlayerGroupBoxRight)
                    self.dataVizPlayerRight_2.setFont(self.font(10, False, 50))
                    self.dataVizPlayerRight_2.setText("Data Viz ")
                    #Data Visualization Button
                    self.dataVizPlayerRight_3 = QtGui.QPushButton(self.PlayerGroupBoxRight)
                    self.dataVizPlayerRight_3.setFont(self.font(10, False, 50))
                    self.dataVizPlayerRight_3.setText("Data Viz ")
                    #Data Visualization Button
                    self.dataVizPlayerRight_4 = QtGui.QPushButton(self.PlayerGroupBoxRight)
                    self.dataVizPlayerRight_4.setFont(self.font(10, False, 50))
                    self.dataVizPlayerRight_4.setText("Data Viz ")
                    #Layout
                    self.PlayerGroupBoxRightGrid = QtGui.QVBoxLayout(self.PlayerGroupBoxRight)
                    self.PlayerGroupBoxRightGrid.addWidget(self.playerNameLabelRight)
                    self.PlayerGroupBoxRightGrid.addWidget(self.lineRight_2)
                    self.PlayerGroupBoxRightGrid.addWidget(self.killsRight, QtCore.Qt.AlignBottom)
                    self.PlayerGroupBoxRightGrid.addWidget(self.deathsRight, QtCore.Qt.AlignBottom)
                    self.PlayerGroupBoxRightGrid.addWidget(self.assistsRight, QtCore.Qt.AlignBottom)
                    self.PlayerGroupBoxRightGrid.addWidget(self.kDRatioRight, QtCore.Qt.AlignBottom)
                    self.PlayerGroupBoxRightGrid.addWidget(self.isArcherRight, QtCore.Qt.AlignBottom)
                    self.PlayerGroupBoxRightGrid.addWidget(self.dataVizPlayerRight_1)
                    self.PlayerGroupBoxRightGrid.addWidget(self.dataVizPlayerRight_2)
                    self.PlayerGroupBoxRightGrid.addWidget(self.dataVizPlayerRight_3)
                    self.PlayerGroupBoxRightGrid.addWidget(self.dataVizPlayerRight_4)
                self.playerTabRight = QtGui.QWidget()
                self.playerTabRightGrid = QtGui.QGridLayout(self.playerTabRight)
                PlayerGroupBoxRight()
                self.playerTabRightGrid.addWidget(self.PlayerGroupBoxRight, 0, 0, 1, 1)                   
                self.tabsRight.addTab(self.playerTabRight, "Player")
            def tournamentRight():
                def TournamentGroupBoxRight():
                    #Tournament Group Box
                    self.TournamentGroupBoxRight = QtGui.QGroupBox(self.tournamentRight)
                    self.TournamentGroupBoxRight.setFont(self.font(12, True, 75))   
                    self.TournamentGroupBoxRight.setTitle("Tournament") 
                    #Tournament Button            
                    self.tournamentBtnRight_1 = QtGui.QPushButton(self.TournamentGroupBoxRight)
                    self.tournamentBtnRight_1.setFont(self.font(10, False, 50))
                    self.tournamentBtnRight_1.setText("tournamnetBtn1")
                    #Tournament Button        
                    self.tournamentBtnRight_2 = QtGui.QPushButton(self.TournamentGroupBoxRight)
                    self.tournamentBtnRight_2.setFont(self.font(10, False, 50))
                    self.tournamentBtnRight_2.setText("tournamnetBtn2")                 
                    #Tournament Button 
                    self.tournamentBtnRight_3 = QtGui.QPushButton(self.TournamentGroupBoxRight)
                    self.tournamentBtnRight_3.setFont(self.font(10, False, 50))
                    self.tournamentBtnRight_3.setText("tournamnetBtn3")   
                    #Tournament Button 
                    self.tournamentBtnRight_4 = QtGui.QPushButton(self.TournamentGroupBoxRight)
                    self.tournamentBtnRight_4.setFont(self.font(10, False, 50))  
                    self.tournamentBtnRight_4.setText("tournamnetBtn4")  
                    #Tournament Button 
                    self.tournamentBtnRight_5 = QtGui.QPushButton(self.TournamentGroupBoxRight)
                    self.tournamentBtnRight_5.setFont(self.font(10, False, 50))   
                    self.tournamentBtnRight_5.setText("tournamnetBtn5") 
                    #Layout   
                    self.TournamentGroupBoxRightGrid = QtGui.QGridLayout(self.TournamentGroupBoxRight)
                    self.TournamentGroupBoxRightGrid.addWidget(self.tournamentBtnRight_1, 0, 0, 1, 1)
                    self.TournamentGroupBoxRightGrid.addWidget(self.tournamentBtnRight_2, 1, 0, 1, 1)
                    self.TournamentGroupBoxRightGrid.addWidget(self.tournamentBtnRight_3, 2, 0, 1, 1)
                    self.TournamentGroupBoxRightGrid.addWidget(self.tournamentBtnRight_4, 3, 0, 1, 1)        
                    self.TournamentGroupBoxRightGrid.addWidget(self.tournamentBtnRight_5, 4, 0, 1, 1)    
                self.tournamentRight = QtGui.QWidget()
                self.tournamentRightGrid = QtGui.QGridLayout(self.tournamentRight)
                TournamentGroupBoxRight()
                self.tournamentRightGrid.addWidget(self.TournamentGroupBoxRight, 0, 0, 1, 1)                       
                self.tabsRight.addTab(self.tournamentRight, "Tournament") 
            dataTabRight()
            teamTabRight()
            playerTabRight()
            tournamentRight()
            self.tabsRight.setCurrentIndex(0)
        TabsLeft()
        TabsRight()
        self.ContainerBottomGrid = QtGui.QHBoxLayout(self.ContainerBottom)
        self.ContainerBottomGrid.addWidget(self.tabsLeft)
        self.ContainerBottomGrid.addWidget(self.tabsRight)
    def font(self, fontSize, Bold, Weight):
        font = QtGui.QFont()
        font.setPointSize(fontSize)
        font.setBold(Bold)
        font.setWeight(Weight)
        return font
def run(Directory):
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow(Directory)
    ui.setupUi(MainWindow)
    MainWindow.show()
    app.exec_()

    