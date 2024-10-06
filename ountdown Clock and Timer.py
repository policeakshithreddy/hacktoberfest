import tkinter as tk
from datetime import datetime, timedelta
import time

class TimerApp:
    def __init__(self, master):
        self.master = master
        master.title("Countdown Clock and Timer")

        self.current_time_label = tk.Label(master, font=('Arial', 24))
        self.current_time_label.pack(pady=20)

        self.timer_label = tk.Label(master, font=('Arial', 24))
        self.timer_label.pack(pady=20)

        self.time_entry = tk.Entry(master, font=('Arial', 16), width=5)
        self.time_entry.pack(pady=10)

        self.start_button = tk.Button(master, text="Start Timer", command=self.start_timer, font=('Arial', 16))
        self.start_button.pack(pady=5)

        self.reset_button = tk.Button(master, text="Reset Timer", command=self.reset_timer, font=('Arial', 16))
        self.reset_button.pack(pady=5)

        self.update_clock()
        self.remaining_time = None
        self.is_timer_running = False

    def update_clock(self):
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        self.current_time_label.config(text=current_time)
        self.master.after(1000, self.update_clock)  # Update the time every second

    def start_timer(self):
        if self.is_timer_running:
            return

        try:
            seconds = int(self.time_entry.get())
            self.remaining_time = timedelta(seconds=seconds)
            self.is_timer_running = True
            self.countdown()
        except ValueError:
            self.timer_label.config(text="Invalid input!")

    def countdown(self):
        if self.remaining_time.total_seconds() > 0:
            self.timer_label.config(text=str(self.remaining_time))
            self.remaining_time -= timedelta(seconds=1)
            self.master.after(1000, self.countdown)  # Update countdown every second
        else:
            self.timer_label.config(text="Time's up!")
            self.is_timer_running = False

    def reset_timer(self):
        self.remaining_time = None
        self.is_timer_running = False
        self.timer_label.config(text="")
        self.time_entry.delete(0, tk.END)  # Clear the entry field

if __name__ == "__main__":
    root = tk.Tk()
    timer_app = TimerApp(root)
    root.mainloop()
