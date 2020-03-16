import tkinter as tk
import globalVar
class bookreturn :
    def onclick( self, Entry1, br, lable3):
        if Entry1.get() == '' :
            lable3.configure(text = "Entry cannot be empty .")
        else :
            idNo=Entry1.get()
            sql="SELECT * FROM issue WHERE idNo=%s"
            val=(idNo,)
            c = globalVar.db1.cursor()
            c.execute(sql, val)
            res = c.fetchall()
            l = len(res)
            for i in range(l) :

        print("Clicked")
    def ui( self ):
        br = tk.Tk()
        br.geometry('600x150+550+300')
        Entry1 = tk.Entry(br, width="15")
        Entry1.grid(row=0, column=1)
        br.title("Book Entry")
        lable1 = tk.Label(br, text="Student Id")
        lable1.grid(row=0, column=0)
        button1 = tk.Button(br, text="Search Student", command=lambda : bookreturn.onclick(bookreturn, Entry1, br, lable3), width="10", height="1")
        button1.grid(column=2, row=0)
        lable3 = tk.Label(br, text="")
        lable3.grid(row=4, column=2)
        br.mainloop()
bookreturn.ui(bookreturn)