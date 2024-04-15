# Purpose of the Calendar class
> The main purpose of the class is to give coaches a visual representation of the team's events for the current and upcoming months and allow them to create events for the future as well.
> It does this by using the following classes: Calendar, Tkinter, Matplotlib, and datetime to create, edit, and validate information in the Calendar class.

# Steps taken and challenges
> When first creating the Calendar class we first created the class constructor which included values to help represent each month's calendar and as well as other variables such as a calendar object to ensure that each date existed during the creating and editing tasks.
> Then the most difficult part in creating the calendar class was integrating the SQL server to add events from the events table when generating different calendars. There were multiple ways for implementing the SQL server to efficiently 
> add, delete, and generate events to the calendars but landed on our current implementation for interacting with the database which was querying the list of events depending on what month you are viewing. 

# Functionality
> The class functions while the GUI is running which is then able to be generated on the main dashboard when selecting the calendar option. The calendar class will utilize matplotlib to format and generate a calendar for the current month using an array of subplots.
> The calendar class will also query the database when first created to process each event for that current month and add them to the calendar in a readable format.
> The only option currently available is the add events button which will then prompt the user for a name and a date in the format of MM/DD/YYYY to then be added to the events table while at the same time closing the calendar and regenerating it with the new event.

# How to use the functionality within the program
1. Open up application
2. Use login
3. From Dashboard, click on Calendar
4. Once calendar has generated then user is allowed to select add events
5. Enter an event name
6. Enter date of event (MUST be in format:MM/DD/YY)
7. Calendar then regenerate with new events
8. When closing the calendar user will return back to the Dashboard
