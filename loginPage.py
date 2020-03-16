import tkinter as tk
import mysql.connector
import globalVar
import dashboard
class loginpage :
    def onClick(self, Entry1, Entry2, m, lable3):
        if Entry1.get()=='' or Entry2.get()=='':
            lable3.configure(text="Username or Password cannot be empty")
        else:
            username = Entry1.get()
            password = Entry2.get()
            try:
                    globalVar.db1 = mysql.connector.connect(host="localhost", user=username, passwd=password, database="LIBRARY")
                    if globalVar.db1.is_connected():
                        m.destroy()
                        objd = dashboard
                        objd.dashboard.ui(dashboard)
            except :
                lable3.configure(text="Invalid Username or Password")
    def ui(self):
        m = tk.Tk()
        m.geometry('600x150+550+300')
        m.title("Login Page")
        lable1 = tk.Label(m, text="username ")
        lable1.grid(row=0, column=0)
        Entry1 = tk.Entry(m, width="15")
        Entry1.grid(row=0, column=1)
        lable2 = tk.Label(m, text="Password ")
        lable2.grid(row=1, column=0)
        Entry2 = tk.Entry(m, width="15", show='*')
        Entry2.grid(row=1, column=1)
        button1 = tk.Button(m, text="Login", command=lambda: loginpage.onClick(loginpage, Entry1, Entry2, m, lable3), width="10", height="1")
        button1.grid(column=1, row=2)
        lable3 = tk.Label(m, text="")
        lable3.grid(row=4, column=2)
        m.mainloop()
loginpage.ui(loginpage)