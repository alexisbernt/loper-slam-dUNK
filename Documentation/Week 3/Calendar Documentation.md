# Purpose of the Calendar class
> The main purpose of the class is to give coaches a visual representation of the team's events for the current and upcoming months, and allow them to create events for the future as well.
> It does this by using the following classes: calendar, tkinter, matplotlib, and datetime to create, edit and validate information in the Calendar class.

# Steps taken and challenges
> To begin the class, we had to make the GUI for the user. This was not too challenging as using TKinter is fairly straight
> forward. After that was implemented we added functionality by allowing the user to "send" an announcment that was initially
> saved to a list. The most difficult part was integrating the SQL server to the announcement functionality. Rather than save
> it to a list, the last iteration saves the announcement to a table, which can then be fetched if needed by the athletes. Because of this, the communcation class ended up being quite large as there was a lot to implement.

# Functionality
> The class functions by intializing the GUI using TKinter methods once the communication button is pressed on the main dashboard. Once intialized, the user will have two options depending on if they logged in as a coach or an athlete. If logged in as a coach, the user is given the option to send an announcement using a textbox and a send announcement button. They can also view recent announcements with a refresh announcements button. Once sent, the announcement is added to an announcement table in the SQL server. If logged in as an athlete, you can only receive announcements using the refresh button.

# How to use the functionality within the program
> To use the functionality, you have to do what was described in the prior paragraph. Depending on your login, you can either send AND receive announcements using the two buttons on the GUI, or you can only receive announcements using the refresh button.
