import tkinter as tk
import dashboard
import mysql.connector
class loginpage :
    def onClick(self, Entry1, Entry2, m,lable3):
        username = Entry1.get()
        password = Entry2.get()
        try:
            db = mysql.connector.connect(host="localhost", user=username, passwd=password, database="LIBRARY")
            if db.is_connected() :
                m.destroy()
                objd = dashboard
                objd.dashboard.ui(dashboard)
        except:
            lable3.configure(text="Not Connected with database")
    def ui(self):
        m = tk.Tk()
        m.title("Login Page")
        lable1 = tk.Label(m, text="username ")
        lable1.grid(row=0, column=0)
        Entry1 = tk.Entry(m, width="15")
        Entry1.grid(row=0, column=1)
        lable2 = tk.Label(m, text="Password ")
        lable2.grid(row=1, column=0)
        Entry2 = tk.Entry(m, width="15", show=' ')
        Entry2.grid(row=1, column=1)
        button1 = tk.Button(m, text="Login", command=lambda: loginpage.onClick(loginpage, Entry1, Entry2, m, lable3), width="10", height="1")
        button1.grid(column=1, row=2)
        lable3 = tk.Label(m, text="")
        lable3.grid(row=4, column=2)
        m.mainloop()
loginpage.ui(loginpage)