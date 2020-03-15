import tkinter as tk
import mysql.connector
class studententry :
    def onClick(self, id_no, name, se):
        id = id_no.get()
        name1 = name.get()
        db1 = mysql.connector.connect(host="localhost", user="nikhil", passwd="123", database="LIBRARY")
        c = db1.cursor()
        sql = "INSERT INTO STUDENT (idNo, name) VALUES (%s, %s)"
        val = (id, name1)
        try:
            c.execute(sql, val)
            db1.commit()
            se.destroy()
        except:
            print("Error in INSERTING")

    def ui(self):
        se = tk.Tk()
        Entry1 = tk.Entry(se, width="15")
        Entry1.grid(row=0, column=1)
        Entry2 = tk.Entry(se, width="15")
        Entry2.grid(row=1, column=1)
        se.title("Student Entry")
        lable1 = tk.Label(se, text="ID")
        lable1.grid(row=0, column=0)
        lable2 = tk.Label(se, text="name")
        lable2.grid(row=1, column=0)
        button1 = tk.Button(se, text="Save", command=lambda:studententry.onClick(self, Entry1, Entry2, se), width="10", height="1")
        button1.grid(column=2, row=2)
        se.mainloop()