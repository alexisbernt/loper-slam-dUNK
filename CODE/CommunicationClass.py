# This will be the communication class
# Dylan will begin coding the communication
import tkinter as tk
from tkinter import Label


class Communication:
    def __init__(self):
        self.window = tk.Tk()
        self.on_screen = []
        self.announcement_list = []
        self.window.title("Communication")
        self.window.geometry(f'{self.window.winfo_screenwidth() // 4}x{self.window.winfo_screenheight() // 3:.0f}')

    def reset_for_communicate(self):
        # Clear The Screen_________
        for item in self.on_screen:
            item.pack_forget()
        self.on_screen = []
        # Title____________________________________________________________
        communication_title = Label(self.window, text="COMMUNICATE", font=("litera", 25), pady=10)
        self.on_screen.append(communication_title)
        communication_title.pack()

        # Adds textbox to comm page, saves it to a list for now
        comm_textbox = tk.Entry(self.window, width=40)
        self.on_screen.append(comm_textbox)
        comm_textbox.pack()
        send_button = tk.Button(self.window, text="Send announcement",
                                command=lambda: self.send_announcement(comm_textbox))
        self.on_screen.append(send_button)
        send_button.pack()

    def send_announcement(self, comm_textbox):
        announce = comm_textbox.get()
        if announce:
            self.announcement_list.append(announce)
            comm_textbox.delete(0, tk.END)
            print("Announcement sent: ", announce)

# run_com_instance = Communication()
# run_com_instance.reset_for_communicate()
