# SETTING UP THE SQL PORTION OF OUR APPLICATION
Definition: According to Amazon Web Services, “Structured query language (SQL) is a programming language for storing and processing information in a relational database.” 
For loperslamdUNK, the Microsoft SQL Server Manager is used. Tables were created in the SQL database. In order to write to that SQL database, we have created .py files for those tables. 
Use SQL to interact with databases. Databases are a collection of tables. All major websites are powered by databases. 
To interface with a database we use a Relational Database Management System (RDMBS)
Microsoft SQL Management Studio is a type of RDMBS) 
SQL Server Management Studio: The SQL server is able to be interacted with. You can set a username and password using Blake’s example class in Python. 
Passwords and usernames are not visible within the SQL database because they get encoded 
You can put the key in along with all other information to get the display in the SQL database 
Go to athletes, edit the top 200 rows, don’t enter athlete ID (that enters itself), Then put in a name, then put in a team ID, then put in a username, then copy and paste the password (encoded) that was generated in the .py file. 
If you manually put the data in it works. You can add usernames and passwords within the .py files. That way our team was able to add usernames and passwords while programming. 


## Starting up SQL on Computer if you are a first-time loper slam dUNK user:
1. Download SQL Server Management Studio (SSMS)
2. If using windows, in search, type ODBC Data Sources. 
An ODBC User data source stores information about how to connect to the indicated data provider. A User data source is only visible to you and can only be used on the user's specific computer.
3. From ODBC Data Source, you can connect a Microsoft Access database to an external data source. In this case, use ODBC to connect to the Microsoft SQL Server.
4. Open up SQL Server Manager and connect to a server. The server type is a database engine. Then connect to your local machine using Windows Authentication (for Windows computers).
5. Once connected, the top is the server that you are connected to and beneath the server there are a number of objects in folders.
6. You can inspect columns and then see all the attributes in the columns. You can edit and submit commands to the database engine using the query window.
7. Go into Databases on the server, open databases, select or create the loperslamdUNK database. The cylinder is representative of a database. Once you open the database you can see Tables and the different tables. Tables help organize data and remove redundancies. Tables create relations and make sure there is less repeat in data (relational databases).
8. You can right click and select the top 1000 rows.
9. Depending on how many entries you’ve created, the entries will display. For example, in the Coaches Table, the CoachID, the Name, the Description, the Username, and the Password data will be visible.
10. Above the results panel is the query. A query can either be a request for data results from your database or for action on the data.

