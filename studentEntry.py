import tkinter as tk
import globalVar
class studententry:
    def onClick(self, id_no, name, se, lable3):
        if id_no.get()=='' or name.get()=='':
            lable3.configure(text = "Entries Cannot be Empty ")
        else :
            id = id_no.get()
            name1 = name.get()
            c = globalVar.db1.cursor()
            sql = "INSERT INTO STUDENT (idNo, name) VALUES (%s, %s)"
            val = (id, name1)
            try:
                c.execute(sql, val)
                globalVar.db1.commit()
                se.destroy()
            except:
                print("Error in INSERTING")
                print(c)
    def ui(self):
        se = tk.Tk()
        se.geometry('600x150+550+300')
        Entry1 = tk.Entry(se, width="15")
        Entry1.grid(row=0, column=1)
        Entry2 = tk.Entry(se, width="15")
        Entry2.grid(row=1, column=1)
        se.title("Student Entry")
        lable1 = tk.Label(se, text="ID")
        lable1.grid(row=0, column=0)
        lable2 = tk.Label(se, text="name")
        lable2.grid(row=1, column=0)
        button1 = tk.Button(se, text="Save", command=lambda:studententry.onClick(self, Entry1, Entry2, se, lable3), width="10", height="1")
        button1.grid(column=0, row=2)
        lable3 = tk.Label(se, text="")
        lable3.grid(row=4, column=2)
        se.mainloop()