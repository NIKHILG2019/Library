import tkinter as tk
import event
d = tk.Tk()
d.title("DashBoard")
button1 = tk.Button(d, width="10", height="1", text="Student Entry", command=event.onClick1)
button1.grid(row=1, column=0)
button2 = tk.Button(d, width="10", height="1", text="Book Entry", command=event.onClick2)
button2.grid(row=1, column=1)
button3 = tk.Button(d, width="10", height="1", text="Book issue", command=event.onClick3)
button3.grid(row=1, column=2)
button4 = tk.Button(d, width="10", height="1", text="Book Return", command=event.onClick4)
button4.grid(row=1, column=3)
d.mainloop()