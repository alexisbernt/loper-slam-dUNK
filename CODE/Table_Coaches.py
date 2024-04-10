from base64 import b64encode

class CoachesController:
    def __init__(self,cnxn):
        self.cnxn = cnxn
        self.cursor = self.cnxn.cursor()

    def checkLogin(self, username, password):
        self.cursor = self.cnxn.cursor()
        self.cursor.execute("SELECT * FROM Coaches WHERE Username = '"+str(username)+"'")
        field_names = [i[0] for i in self.cursor.description]
        userIdx = 0
        for field in field_names:
            if field == "Username":
                break
            userIdx+=1
        user = self.cursor.fetchall()[0]
        print(user)
        print(user[userIdx])
        token = b64encode(f"{username}:{password}".encode('utf-8')).decode("ascii")

        # returns if the login information is correct for the user.
        return token == user[userIdx]



    def printContent(self):
        # Go through each row in the currently selected data and print it out.
        # We can move to something Tkinter based quite easily from here.
        for row in self.cursor:
            print('row = %r' % (row,))


    def getCoaches(self):
        self.cursor = self.cnxn.cursor()
        self.cursor.execute('SELECT * FROM Coaches')
        return self.cursor.fetchall()

    def getCoach(self, id):
        self.cursor = self.cnxn.cursor()
        self.cursor.execute("SELECT * FROM Coaches where CoachID = '"+str(id)+"'")
        return self.cursor.fetchall()

    def addCoach(self, name, description, username, password):
        self.cursor = self.cnxn.cursor()
        # We use a token that uses both the username and password so it's harder for an attacker to decode the password.
        token = b64encode(f"{username}:{password}".encode('utf-8')).decode("ascii")
        try:
            self.cursor.execute("INSERT INTO Coaches (Name, Description, Username, Password) VALUES ('"+str(name)+"', '"+str(description)+"', '"+str(username)+"', '"+str(token)+"'); COMMIT;")
        except:
            return False
        else:
            return True

    def removeCoach(self, id):
        self.cursor = self.cnxn.cursor()
        try:
            self.cursor.execute("DELETE FROM Coaches where CoachID = '"+str(id)+"'; COMMIT;")
        except:
            return False
        else:
            return True
        
    def attachTeam(self, coach, team):
        self.cursor = self.cnxn.cursor()
        try:
            self.cursor.execute("INSERT INTO CoachesTeams (CoachID, TeamID) VALUES ('"+str(coach)+"', '"+str(team)+"'); COMMIT;")
        except:
            return False
        else:
            return True

    def detachTeam(self, coach, team):
        self.cursor = self.cnxn.cursor()
        try:
            self.cursor.execute("DELETE FROM CoachesTeams where CoachID = '"+str(coach)+"' and TeamID = '"+str(team)+"'; COMMIT;")
        except:
            return False
        else:
            return True
    
    def getTeams(self, coach):
        self.cursor = self.cnxn.cursor()
        self.cursor.execute("SELECT * FROM CoachesTeams where CoachID = '"+str(coach)+"'")
        return self.cursor.fetchall()
        
    def updateCoach(self, id, colNames = [], colVals = []):
        if len(colNames) != len(colVals):
            return "Column name / value mismatch. Ensure same # of values for both!"
        self.cursor = self.cnxn.cursor()
        try:
            updateString = "UPDATE Coaches "
            setString = ""
            whereString = " WHERE CoachID = '"+id+"'"
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