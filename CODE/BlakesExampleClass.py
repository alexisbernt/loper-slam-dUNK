from base64 import b64encode
import pyodbc
class ExampleClass:
    def __init__(self):
        # We can make this pull info from a .env file if we want to personalize it without overwriting each other's settings we need.
        # This is just a quick example though so I'll leave it for now. Feel free to modify on your end for testing and then undoing changes.
        self.cnxn = pyodbc.connect(
            "Driver={SQL Server};"
            "Server=LAPTOP-3JNM76RU;"
            "Database=LoperSlamdUNKDB;"
            "Trusted_Connection=yes;"
        )

        # Our main connection to the server. Use this variable to interact with it through queries.
        self.cursor = self.cnxn.cursor()

    def printContent(self):
        # Go through each row in the currently selected data and print it out.
        # We can move to something Tkinter based quite easily from here.
        for row in self.cursor:
            print('row = %r' % (row,))


    def getAthletes(self):
        self.cursor = self.cnxn.cursor()
        self.cursor.execute('SELECT * FROM Athletes')

        self.printContent()

    def getTeams(self):
        self.cursor = self.cnxn.cursor()
        self.cursor.execute('SELECT * FROM Teams')

        self.printContent()

    def getCoaches(self):
        self.cursor = self.cnxn.cursor()
        self.cursor.execute('SELECT * FROM Coaches')

        self.printContent()

    def getCoachesTeams(self):
        self.cursor = self.cnxn.cursor()
        self.cursor.execute('SELECT * FROM CoachesTeams')

        self.printContent()

    def getMessagesCtoT(self):
        self.cursor = self.cnxn.cursor()
        self.cursor.execute('SELECT * FROM MessagesCtoT')

        self.printContent()

    def getMessagesCtoA(self):
        self.cursor = self.cnxn.cursor()
        self.cursor.execute('SELECT * FROM MessagesCtoA')

        self.printContent()
    
    def getAdmins(self):
        self.cursor = self.cnxn.cursor()
        self.cursor.execute('SELECT * FROM Admins')

        self.printContent()

    def getUsers(self):
        self.cursor = self.cnxn.cursor()
        self.cursor.execute('SELECT * FROM Users')

        self.printContent()
    
    def getSignatures(self):
        self.cursor = self.cnxn.cursor()
        self.cursor.execute('SELECT * FROM Signatures')

        self.printContent()


    def printContent(self):
        # Go through each row in the currently selected data and print it out.
        # We can move to something Tkinter based quite easily from here.
        for row in self.cursor:
            print('row = %r' % (row,))


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

    def addTeam(self, name, desc): #ensure name and desc variables have no special characters in them... Otherwise injection might be possible.
        self.cursor = self.cnxn.cursor()
        self.cursor.execute("INSERT INTO Teams (Name, Description) VALUES ('"+name+"', '"+desc+"'); COMMIT;")

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

    def addMessageCtoT(self): #CHANGE BEHAVIOR
        self.cursor = self.cnxn.cursor()
        self.cursor.execute('SELECT * FROM MessagesCtoT')
        self.printContent()

    def addMessageCtoA(self): #CHANGE BEHAVIOR
        self.cursor = self.cnxn.cursor()
        self.cursor.execute('SELECT * FROM MessagesCtoA')
        self.printContent()



example = ExampleClass()
# example.addTeam("Team 1","We are team 1")
# example.addCoach("Coachy McCoacherson","coachman92","coachpass123",10)


print("This shows all the rows of the Athletes table!:")
example.getAthletes()
print("\n\nThis shows all the rows of the Teams table!:")
example.getTeams()
print("\n\nThis shows all the rows of the Coaches table!:")
example.getCoaches()
print("\n\nThis shows all the rows of the CoachesTeams table!:")
example.getCoachesTeams()
print("\n\nThis shows all the rows of the MessagesCtoT table!:")
example.getMessagesCtoT()
print("\n\nThis shows all the rows of the MessagesCtoA table!:")
example.getMessagesCtoA()

print("\n\nThis shows all the rows of the Admins table!:")
example.getAdmins()
print("\n\nThis shows all the rows of the Users table!:")
example.getUsers()
print("\n\nThis shows all the rows of the Signatures table!:")
example.getSignatures()

















