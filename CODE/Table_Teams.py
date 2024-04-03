class TeamsController:
    def __init__(self,cnxn):
        self.cnxn = cnxn
        self.cursor = self.cnxn.cursor()

    def printContent(self):
        # Go through each row in the currently selected data and print it out.
        # We can move to something Tkinter based quite easily from here.
        for row in self.cursor:
            print('row = %r' % (row,))


    def getTeams(self):
        self.cursor = self.cnxn.cursor()
        self.cursor.execute('SELECT * FROM Teams')
        return self.cursor

    def getTeam(self, id):
        self.cursor = self.cnxn.cursor()
        self.cursor.execute("SELECT * FROM Teams where TeamID = '"+id+"'")
        return self.cursor

    def addTeam(self, name, team):
        self.cursor = self.cnxn.cursor()
        try:
            self.cursor.execute("INSERT INTO Teams (Name, TeamID) VALUES ('"+name+"', '"+str(team)+"'); COMMIT;")
        except:
            return False
        else:
            return True
    def removeTeam(self, id):
        self.cursor = self.cnxn.cursor()
        try:
            self.cursor.execute("DELETE FROM Teams where TeamID = '"+id+"'; COMMIT;")
        except:
            return False
        else:
            return True
        
    def updateTeam(self, id, colNames = [], colVals = []):
        if len(colNames) != len(colVals):
            return "Column name / value mismatch. Ensure same # of values for both!"
        self.cursor = self.cnxn.cursor()
        try:
            updateString = "UPDATE Teams "
            setString = ""
            whereString = " WHERE TeamID = '"+id+"'"
            x = 0
            setString += "SET "+colNames[0]+" = "+colVals[0]
            colVals.pop(0)
            colNames.pop(0)
            for col in colNames:
                setString += ", SET "+col+" = "+colVals[x]
                x+=1
            self.cursor.execute(updateString+setString+whereString)
        except:
            return False
        else:
            return True







