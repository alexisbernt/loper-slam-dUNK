# This will be the calendar class
# Juan will begin coding the calendar
import calendar
import matplotlib.pyplot as plt

w_days = 'Sun Mon Tue Wed Thu Fri Sat'.split()
m_names = 'January February March April May June July August September October November December'.split()
#Ensure that the first day in the calendar is sunday
calendar.setfirstweekday(6)
class Calendar:
    def __init__(self, year, month):
        self._year = year
        self._month = month
        self.cal = calendar.monthcalendar(year, month)

        self.events = [[[] for day in week] for week in self.cal]

    def dayIndex(self, day):
    #index of the day in the list of lists
        for week_n, week in enumerate(self.cal):
            try:
                i = week.index(day)
                return week_n, i
            except ValueError:
                pass
        raise ValueError(f"There are not {day} days in the month")

    def show(self):
    #formatting calendar
        f, axs = plt.subplots(len(self.cal), 7, sharex=True, sharey=True)
        for week, ax_row in enumerate(axs):
            for week_day, ax in enumerate(ax_row):
                ax.set_xticks([])
                ax.set_yticks([])
                if self.cal[week][week_day] != 0:
                    ax.text(.02, .98,
                            str(self.cal[week][week_day]),
                            verticalalignment='top',
                            horizontalalignment='left')
                    contents = "\n".join(self.events[week][week_day])
                    ax.text(.03, .85, contents,
                            verticalalignment='top',
                            horizontalalignment='left',
                            fontsize=9)

        #using the titles of the weekdays(w_days) as first row
        for n, day in enumerate(w_days):
            axs[0][n].set_title(day)

        #
        f.subplots_adjust(hspace=0)
        f.subplots_adjust(wspace=0)
        f.suptitle(m_names[self._month] + '' + str(self._year),
                   fontsize=20, fontweight= 'bold')
        plt.show()

    #Function takes a string(event) and ensure that the date exist and adds to calendar
    def addEvent(self, day, event):
        week, w_day = self.dayIndex(day)
        self.events[week][w_day].append(event)
