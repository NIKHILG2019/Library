import tkinter as tk
class bookentry :
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
        button1 = tk.Button(se, text="Save", command=lambda : studententry.onClick(self, Entry2, be, lable3), width="10",
                            height="1")
        button1.grid(column=0, row=2)
        lable3 = tk.Label(se, text="")
        lable3.grid(row=4, column=2)
        be.mainloop()
