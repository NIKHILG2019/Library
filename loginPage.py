import tkinter as tk
import DATABASE
db = DATABASE.Database_connect
db.Database_Connection('', '')
m = tk.Tk()
m.title("Login Page")
lable1 = tk.Label(m, text="username ")
lable1.grid(row=0, column=0)
text1 = tk.Text(m, width="15", height="1")
text1.grid(row=0, column=1)
lable2 = tk.Label(m, text="Password ")
lable2.grid(row=1, column=0)
text2 = tk.Text(m, width="15", height="1")
text2.grid(row=1, column=1)
button1 = tk.Button(m, text="Login", command=m.destroy, width="10", height="1")
button1.grid(column=1, row=2)
m.mainloop()
