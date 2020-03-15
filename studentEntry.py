import tkinter as tk
import mysql.connector
def onClick() :
    db1 = mysql.connector.connect(host="localhost", user="nikhil", passwd="123", database="LIBRARY")
    c = db1.cursor()
    sql = "INSERT INTO STUDENT (idNo, name) VALUES (%s, %s)"
    id_no = Entry1.get()
    name = Entry2.get()
    val = (id_no, name)
    try:
        c.execute(sql, val)
        db1.commit()
        se.destroy()
        import dashboard
    except:
        print("Error in INSERTING")

se = tk.Tk()
se.title("Student Entry")
lable1 = tk.Label(se, text="ID")
lable1.grid(row=0, column=0)
lable2 = tk.Label(se, text="name")
lable2.grid(row=1, column=0)
Entry1 = tk.Entry(se, width="15")
Entry1.grid(row=0, column=1)
Entry2 = tk.Entry(se, width="15")
Entry2.grid(row=1, column=1)
button1 = tk.Button(se, text="Save", command=onClick, width="10", height="1")
button1.grid(column=1, row=2)
se.mainloop()