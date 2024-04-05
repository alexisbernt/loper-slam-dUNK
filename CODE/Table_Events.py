# Still need to set up an events table. Then we'll fill this thing in.
import pyodbc
class EventsController:
    def __init__(self):
        self.cnxn = pyodbc.connect(
            "Driver={SQL Server};"
            "Server=MSI;"
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
    def getEvents(self):
        self.cursor = self.cnxn.cursor()
        self.cursor.execute('SELECT * FROM Events')

        self.printContent()

    def addEvent(self, name, date):
        self.cursor = self.cnxn.cursor()
        self.cursor.execute("INSERT INTO Teams (Name, Date) VALUES ('" + name + "', '" + date + "'); COMMIT;")


events = EventsController()
events.addEvent("First meet of the season", "03/01/2004")

print("This shows all the rows of the Athletes table!:")
events.getEvents()