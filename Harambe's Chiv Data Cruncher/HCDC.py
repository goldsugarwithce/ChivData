'''
Created on Aug 12, 2016
'''
#Import libs
import gspread #Handles google sheet pulls
from oauth2client.service_account import ServiceAccountCredentials #handles google api credentials 
import time #for use in program timing
start_time = time.time()

'''
any changes
'''
class Player(object):
    '''
    Player Object which contains info specific to the player
    and methods to update and calculate player specific values
    '''
    def __init__(self, name):
        '''
        Sets Attributes
        '''
        #Static Values
        self.playerName = name
        #Dynamic Values
        self.kills = 0
        self.deaths = 0
        self.assists = 0
        self.isArcher = False
        self.kDRatio = 0
    def updateValues(self, kills, deaths, assists, isArcher):
        '''
        Updates dynamic values
        '''
        self.kills = self.kills + int(kills)
        self.deaths = self.deaths + int(deaths)
        self.assists = self.assists + int(assists)
        if isArcher == "TRUE":
            self.isArcher = True
        self.kDRatio = self.kills/self.deaths
class Team(object):
    '''
    Team object which contains info specific to the team
    and methods to update and calculate team specific values
    '''
    def __init__(self, teamName):
        '''
        Set Attributes
        '''
        #Static Values
        self.teamName = teamName #Identifier
        #player Values
        self.playerList = []
        #player directory
        self.playerDir = {} 
        #Dynamic Values
        self.teamWins = 0
        self.teamLoss = 0
    def ObjectCreator(self):
        '''
        Fills player directory with player objects
        '''
        for player in self.playerList:
            playerObj = Player(player)
            self.playerDir[player] = playerObj
    def Win(self):
        '''
        Handles Case were team wins
        '''
        self.teamWins += 1
    def Loss(self):
        '''
        Handles Case were team loses
        '''
        self.teamLoss += 1
class Half(object):
    '''
    Half object which contains data specific to the Half
    and methods to update and return half specific values
    '''
    def __init__(self, row, half, matchWrs, teamList, playerListTeamOne, playerListTeamTwo):
        '''
        Set Attributes
        '''
        #Input Variables
        self.row = row + (half - 1)*8
        self.half = half
        self.matchWrs = matchWrs
        #Lists
        self.teamList = teamList
        self.playerListTeamOne = playerListTeamOne
        self.playerListTeamTwo = playerListTeamTwo
        self.playerList = self.playerListTeamOne + self.playerListTeamTwo
        #Directories
        self.teamDir = {}
        self.playerDir = {}
        #Main Sequence
        self.gatherData()
        self.objectCreator()
        self.ValueUpdater()
    def gatherData(self):
        '''
        Gather data specific to half
        '''
        self.attacking = self.matchWrs.getCellValue("C" + str(self.row))
        self.defending = self.matchWrs.getCellValue("E" + str(self.row))
        self.objectiveReached = self.matchWrs.getCellValue("G" + str(self.row))
        self.objectiveTime = self.matchWrs.getCellValue("I" + str(self.row))    
    def objectCreator(self):
        '''
        Creates Team objects and Player objects 
        '''
        def TeamObjectCreate(team, playerList):
            teamObj = Team(team) #generates a Team object
            teamObj.playerList = playerList #updates player list for team object
            teamObj.ObjectCreator() #creates player objects for the team object
            self.teamDir[team] = teamObj #adds to directory
        TeamObjectCreate(self.teamList[0], self.playerListTeamOne) #Team Object for team one
        TeamObjectCreate(self.teamList[1], self.playerListTeamTwo) #Team Object for team one
        #Creates and adds player objects to player directory
        for player in self.playerList:
            playerObj = Player(player) #generates a player object
            self.playerDir[player] = playerObj #adds to directory
    def ValueUpdater(self):
        '''
        Creates player object specific to half and places them into the playerDir 
        also fills out info for teams playerDir
        '''
        #=======================================================================
        # this block of code needs to be fixed for redundancy
        #=======================================================================
        x = time.time() - start_time
        for (i, player) in enumerate(self.playerList): #iterates over player list and creates a counter
            if self.half == 1: #if first half
                if i < 6: #column #1
                    row = str(self.row + i + 2) #determines the row the player data is on
                    #Gather data from spreadsheet
                    kills = self.matchWrs.getCellValue("C" + row) 
                    deaths = self.matchWrs.getCellValue("D" + row)
                    assists = self.matchWrs.getCellValue("E" + row)
                    isArcher = self.matchWrs.getCellValue("F" + row)
                    #Update player Values in team directory
                    self.teamDir[self.attacking].playerDir[player].updateValues(kills, deaths, assists, isArcher)
                else: #column #2
                    row = str(self.row + (i-5) + 1) #determines the row the player data is on
                    #Gather data from spreadsheet
                    kills = self.matchWrs.getCellValue("H" + row)
                    deaths = self.matchWrs.getCellValue("I" + row)
                    assists = self.matchWrs.getCellValue("J" + row)
                    isArcher = self.matchWrs.getCellValue("K" + row)
                    #Update player Values in team directory
                    self.teamDir[self.defending].playerDir[player].updateValues(kills, deaths, assists, isArcher)
                #Update player Values in player directory
                self.playerDir[player].updateValues(kills, deaths, assists, isArcher)
            else: #if second half
                if i < 6: #column #1
                    row = str(self.row + i + 2) #determines the row the player data is on
                    #Gather data from spreadsheet
                    kills = self.matchWrs.getCellValue("H" + row)
                    deaths = self.matchWrs.getCellValue("I" + row)
                    assists = self.matchWrs.getCellValue("J" + row)
                    isArcher = self.matchWrs.getCellValue("K" + row)
                    #Update player Values in team directory
                    self.teamDir[self.defending].playerDir[player].updateValues(kills, deaths, assists, isArcher)
                else: #column #2
                    row = str(self.row + (i-5) + 1) #determines the row the player data is on
                    #Gather data from spreadsheet
                    kills = self.matchWrs.getCellValue("C" + row)
                    deaths = self.matchWrs.getCellValue("D" + row)
                    assists = self.matchWrs.getCellValue("E" + row)
                    isArcher = self.matchWrs.getCellValue("F" + row)
                    #Update player Values in team directory
                    self.teamDir[self.attacking].playerDir[player].updateValues(kills, deaths, assists, isArcher)
                #Update player Values in player directory
                self.playerDir[player].updateValues(kills, deaths, assists, isArcher)
        print("time it took to do get data from half :{}".format(str((time.time() - start_time) - x)))
class Match(object):
    '''
    Match object which contains data specific to the match
    and methods to update and return half specific values
    '''
    def __init__(self, matchNum, matchWrs):
        '''
        Set Attributes
        '''
        #Match Create Variables
        self.matchNum = matchNum
        self.matchWrs = matchWrs
        #Determines Base Row
        self.row = ((self.matchNum - 1)*16 + 1)
        #Directories
        self.halfDir = {}
        self.teamDir = {}
        self.playerDir = {}
        #Lists
        self.halfList = [1, 2]
        #GatherData
        self.gatherData()
        self.objectCreator()
        self.ValueUpdater()
    def gatherData(self):
        '''
        Gather match specific data
        '''
        x = time.time() - start_time
        #Variables
        self.teamOne = self.matchWrs.getCellValue("A" + str(self.row + 4))
        self.teamTwo = self.matchWrs.getCellValue("A" + str(self.row + 6))
        self.map = self.matchWrs.getCellValue("A" + str(self.row + 8))
        self.winner = self.matchWrs.getCellValue("A" + str(self.row + 10))
        self.loser = self.matchWrs.getCellValue("A" + str(self.row + 12))
        #Lists
        self.teamList = [self.teamOne, self.teamTwo]
        self.playerListTeamOne = []
        self.playerListTeamTwo = []
        #fills player lists for each team
        for x in range(1, 7):
            row = str(self.row + 1 + x) #row calculation
            #get Values from spreadsheet
            self.playerListTeamOne.append(self.matchWrs.getCellValue("B" + row))
            self.playerListTeamTwo.append(self.matchWrs.getCellValue("G" + row))
        #gets a match specific list of players
        self.playerList = self.playerListTeamOne + self.playerListTeamTwo
        print("time it took to gather data from match :{}".format(str((time.time() - start_time) - x)))
    def objectCreator(self):
        '''
        Creates half, team, player objects and adds
        them to corresponding directories
        '''
        #=======================================================================
        # There has to be a way to remove redundancy here
        #=======================================================================
        #Half Object Creation
        for half in self.halfList:
            halfObj = Half(self.row, half, self.matchWrs, self.teamList, self.playerListTeamOne, self.playerListTeamTwo)
            self.halfDir[half] = halfObj
        #Team Object Creation
        for team in self.teamList:
            teamObj = Team(team)
            teamObj.playerList = self.halfDir[1].teamDir[team].playerList
            teamObj.ObjectCreator()
            self.teamDir[team] = teamObj
        #Player Object Creation
        for player in self.playerList:
            playerObj = Player(player)
            self.playerDir[player] = playerObj                
    def ValueUpdater(self):
        '''
        Updates match objects
        '''
        #Updates player objects
        for player in self.playerList:
            #calculates new values
            kills = self.halfDir[1].playerDir[player].kills + self.halfDir[2].playerDir[player].kills
            deaths = self.halfDir[1].playerDir[player].deaths + self.halfDir[2].playerDir[player].deaths
            assists = self.halfDir[1].playerDir[player].assists + self.halfDir[2].playerDir[player].assists
            #Updates team directory
            for team in self.teamList:
                try: #easier way to find player within team directory
                    self.teamDir[team].playerDir[player].updateValues(kills, deaths, assists, None)
                    break
                except:
                    pass
            self.playerDir[player].updateValues(kills, deaths, assists, None)
        #Updates team win/lose
        self.teamDir[self.winner].Win()
        self.teamDir[self.loser].Loss()
class SpreadSheet(object):
    '''
    Contains main spreadsheet object and methods required
    for error handling and data processing
    '''
    def __init__(self, url):
        '''
        '''
        scope = ['https://spreadsheets.google.com/feeds']
        credentials = ServiceAccountCredentials.from_json_keyfile_name('tutorial-b786124aec22.json', scope)
        gc = gspread.authorize(credentials)
        self.wks = gc.open_by_url(url)
        self.worksheet = self.wks.get_worksheet(0)
    def getCellValue(self, cellValue):
        '''
        get cell value based on alphanumerical cell position
        '''
        return self.worksheet.acell(cellValue).value
    def changeValue(self, label, newValue):
        '''
        changes cell value based on alphanumerical cell position
        '''
        self.worksheet.update_acell(label, newValue)
    def columnValues(self, column):
        '''
        gets all values from column
        '''
        return self.worksheet.col_values(column)
    def rowValues(self, row):
        '''
        gets all values from row
        '''
        return self.worksheet.row_values(row)
class Directory():
    '''
    Main program object
    '''
    def __init__(self):
        '''
        Constructor
        '''
        #Directories
        self.playerDir = {}
        self.teamDir = {}
        self.matchDir = {}
        self.matchNumber = 1
        #Lists
        self.playerList = []
        self.teamList = []
        self.matchList = []
        #Spreadsheets
        self.teamWrs = SpreadSheet("https://docs.google.com/spreadsheets/d/1T6KWtWPa4UMvquZ_yuiaRN0PJBytHle7F8a4u3pzKtk/edit#gid=0")
        self.matchWrs = SpreadSheet("https://docs.google.com/spreadsheets/d/1ia8PwjHRf4newhe7Gl5DEvMCjVFs0VswXSkH57lYT78/edit#gid=0")
        #Main Sequence of program
        self.inputTeamWrs()
        self.playerCreate()
        self.matchCreate()
    def matchCreate(self):
        '''
        Create match object and add to match directory
        '''
        match = Match(self.matchNumber, self.matchWrs)
        self.matchDir[self.matchNumber] = match
        #Updates tournament wide values
        self.ValueUpdater(self.matchNumber)
        self.matchNumber += 1
    def playerCreate(self):
        '''
        Create player object and add to player directory
        '''
        for player in self.playerList:
            playerObj = Player(player)
            self.playerDir[player] = playerObj
    def inputTeamWrs(self):
        '''
        Gather data for and creates teamDir
        '''
        x = time.time() - start_time
        col = self.teamWrs.columnValues(1)
        #Gathers all the team names
        for x in range(1, len(col)):
            self.teamList.append(col[x])
        #Creates team objects for each
        for (i, team) in enumerate(self.teamList):
            self.teamDir[team] = Team(team)
            #finds all the players on a specific team
            playerList = self.teamWrs.rowValues(i + 2)
            for x in range(1,len(playerList)):
                #ensures blank cells are ignored
                if playerList[x] == '':
                    break
                else:
                    #updates team object player list 
                    self.teamDir[team].playerList.append(playerList[x])
                    #updates tournament object player list 
                    self.playerList.append(playerList[x])
            #creates player objects for each team
            self.teamDir[team].ObjectCreator()
        print("time it took to do gather data from Team spreadsheat :{}".format(str((time.time() - start_time) - x)))
    def ValueUpdater(self, matchNumber):
        '''
        Updates tournament wide values
        '''
        #Updates Player Values
        playerList = self.matchDir[matchNumber].playerList
        for player in playerList:
            #Gets player values from certain match
            kills = self.matchDir[matchNumber].playerDir[player].kills
            deaths = self.matchDir[matchNumber].playerDir[player].deaths
            assists = self.matchDir[matchNumber].playerDir[player].assists
            #Updates player object
            self.playerDir[player].updateValues(kills, deaths, assists, None)
            #Updates team object's player objects
            for team in self.matchDir[matchNumber].teamList:
                try:
                    self.teamDir[team].playerDir[player].updateValues(kills, deaths, assists, None)
                except:
                    pass
        #Updates Team Values
        self.teamDir[self.matchDir[matchNumber].winner].Win()
        self.teamDir[self.matchDir[matchNumber].loser].Loss()
    def dirPull(self, *arg):
        '''
        method to pull data from directory
        ensure args are placed in order of largest to smallest object
        '''
        argNum = len(arg)
        print(time.time() - start_time)
        if any(x in self.playerList for x in arg):
            if any(x in self.teamList for x in arg):
                if argNum == 4:
                    return self.matchDir[arg[0]].halfDir[arg[1]].teamDir[arg[2]].playerDir[arg[3]]
                elif argNum == 3:
                    return self.matchDir[arg[0]].teamDir[arg[1]].playerDir[arg[2]]
                else:
                    return self.matchDir[arg[0]].teamDir[arg[1]].playerDir[arg[2]]
            else:
                if argNum == 3:
                    return self.matchDir[arg[0]].halfDir[arg[1]].playerDir[arg[2]]
                if argNum == 2:
                    return self.matchDir[arg[0]].playerDir[arg[1]]
                if argNum == 1:
                    return self.playerDir[arg[0]]
        elif any(x in self.teamList for x in arg):
            if argNum == 3:
                return self.matchDir[arg[0]].halfDir[arg[1]].teamDir[arg[2]]
            if argNum == 2:
                return self.matchDir[arg[0]].teamDir[arg[1]]
            if argNum == 1:
                return self.teamDir[arg[1]]
        else:
            if argNum == 2:
                return self.matchDir[arg[0]].halfDir[arg[1]]
            elif argNum == 1:
                return self.matchDir[arg[0]]
            else:
                pass
HCDC = Directory()
print(HCDC.dirPull("Crimson King").kills)

