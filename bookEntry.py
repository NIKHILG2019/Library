import globalVar
import tkinter as tk
class bookentry :
    def onclick ( self, Entry1, Entry2, be, lable3 ) :
        Quantity = Entry1.get()
        bookName = Entry2.get()
        c = globalVar.db1.cursor()
        sql = "INSERT INTO BOOKS (bookName,Quantity) VALUES(%s,%s)"
        val = (bookName, Quantity)
        try :
            c.execute(sql, val)
            globalVar.db1.commit()
            be.destroy()
        except :
            print("Error in Inserting.")
            lable3.configure(text="Error occured in Inserting.")

    def ui ( self ) :
        be = tk.Tk()
        be.geometry('600x150+550+300')
        Entry1 = tk.Entry(be, width="15")
        Entry1.grid(row=0, column=1)
        Entry2 = tk.Entry(be, width="15")
        Entry2.grid(row=1, column=1)
        be.title("Book Entry")
        lable2 = tk.Label(be, text="Book Name")
        lable2.grid(row=1, column=0)
        lable1 = tk.Label(be, text="Quantity")
        lable1.grid(row=0, column=0)
        button1 = tk.Button(be, text="Save", command=lambda : bookentry.onclick(bookentry, Entry1, Entry2, be, lable3),
                            width="10",
                            height="1")
        button1.grid(column=0, row=2)
        lable3 = tk.Label(be, text="")
        lable3.grid(row=4, column=2)
        be.mainloop()
