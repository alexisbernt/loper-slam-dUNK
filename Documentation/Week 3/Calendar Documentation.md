# Purpose of the Calendar class
> The main purpose of the class is to give coaches a visual representation of the team's events for the current and upcoming months and allow them to create events for the future as well.
> It does this by using the following classes: Calendar, Tkinter, Matplotlib, and datetime to create, edit, and validate information in the Calendar class.

# Steps taken and challenges
> When first creating the Calendar class we first created the class constructor which included values to help represent each month's calendar and as well as other variables such as a calendar object to ensure that each date existed during the creating and editing tasks.
> Then the most difficult part in creating the calendar class was integrating the SQL server to add events from the events table when generating different calendars. There were multiple ways for implementing the SQL server to efficiently 
> add, delete, and generate events to the calendars but landed on our current implementation for interacting with the database which was querying the list of events depending on what month you are viewing. 

# Functionality
> The class functions by intializing the GUI using TKinter methods once the communication button is pressed on the main dashboard. Once intialized, the user will have two options depending on if they logged in as a coach or an athlete. If logged in as a coach, the user is given the option to send an announcement using a textbox and a send announcement button. They can also view recent announcements with a refresh announcements button. Once sent, the announcement is added to an announcement table in the SQL server. If logged in as an athlete, you can only receive announcements using the refresh button.

# How to use the functionality within the program
> To use the functionality, you have to do what was described in the prior paragraph. Depending on your login, you can either send AND receive announcements using the two buttons on the GUI, or you can only receive announcements using the refresh button.
