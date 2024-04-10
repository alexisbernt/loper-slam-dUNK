from base64 import b64encode

class AthletesController:
    def __init__(self,cnxn):
        self.cnxn = cnxn
        self.cursor = self.cnxn.cursor()

    def checkLogin(self, username, password):
        self.cursor = self.cnxn.cursor()
        self.cursor.execute("SELECT * FROM Athletes WHERE Username = '"+str(username)+"'")
        field_names = [i[0] for i in self.cursor.description]
        userIdx = 0
        for field in field_names:
            if field == "Username":
                break
            userIdx+=1
        user = (self.cursor.fetchall()[0]) or None
        if user == None:
            return False
        token = b64encode(f"{username}:{password}".encode('utf-8')).decode("ascii")

        # returns if the login information is correct for the user.
        return token == user[userIdx]

    def printContent(self):
        # Go through each row in the currently selected data and print it out.
        # We can move to something Tkinter based quite easily from here.
        for row in self.cursor:
            print('row = %r' % (row,))


    def getAthletes(self):
        self.cursor = self.cnxn.cursor()
        self.cursor.execute('SELECT * FROM Athletes')
        return self.cursor.fetchall()

    def getAthlete(self, id):
        self.cursor = self.cnxn.cursor()
        self.cursor.execute("SELECT * FROM Athletes where AthleteID = '"+str(id)+"'")
        return self.cursor.fetchall()

    def addAthlete(self, name, username, password, team = None):
        token = b64encode(f"{username}:{password}".encode('utf-8')).decode("ascii")

        self.cursor = self.cnxn.cursor()
        intoStr = "(Name, Username, Password, TeamID); COMMIT;"
        valuesStr = "VALUES ('"+name+", '"+str(username)+", '"+str(token)+", '"+str(team or "")+"'); COMMIT;"
        try:
            self.cursor.execute("INSERT INTO Athletes "+intoStr+" VALUES "+valuesStr+"; COMMIT;")
        except:
            return False
        else:
            return True

    def removeAthlete(self, id):
        self.cursor = self.cnxn.cursor()
        try:
            self.cursor.execute("DELETE FROM Athletes where AthleteID = '"+str(id)+"'; COMMIT;")
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