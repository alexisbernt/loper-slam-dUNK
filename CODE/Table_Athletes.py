class AthletesController:
    def __init__(self,cnxn):
        self.cnxn = cnxn
        self.cursor = self.cnxn.cursor()

    def printContent(self):
        # Go through each row in the currently selected data and print it out.
        # We can move to something Tkinter based quite easily from here.
        for row in self.cursor:
            print('row = %r' % (row,))


    def getAthletes(self):
        self.cursor = self.cnxn.cursor()
        self.cursor.execute('SELECT * FROM Athletes')
        return self.cursor

    def getAthlete(self, id):
        self.cursor = self.cnxn.cursor()
        self.cursor.execute("SELECT * FROM Athletes where AthleteID = '"+id+"'")
        return self.cursor

    # add team ID to this as it's required...
    def addAthlete(self, name, athlete):
        self.cursor = self.cnxn.cursor()
        try:
            self.cursor.execute("INSERT INTO Athletes (Name, AthleteID) VALUES ('"+name+"', '"+str(athlete)+"'); COMMIT;")
        except:
            return False
        else:
            return True
    def removeAthlete(self, id):
        self.cursor = self.cnxn.cursor()
        try:
            self.cursor.execute("DELETE FROM Athletes where AthleteID = '"+id+"'; COMMIT;")
        except:
            return False
        else:
            return True
        
    def updateAthlete(self, id, colNames = [], colVals = []):
        if len(colNames) != len(colVals):
            return "Column name / value mismatch. Ensure same # of values for both!"
        self.cursor = self.cnxn.cursor()
        try:
            updateString = "UPDATE Athletes "
            setString = ""
            whereString = " WHERE AthleteID = '"+id+"'"
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







