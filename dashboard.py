import tkinter as tk
import studentEntry as s
import bookEntry as b
import bookIssue as i
import bookReturn as r
import globalVar

class dashboard:
    def onClick1(self, d):
        d.destroy()
        objs = s.studententry
        objs.ui(s.studententry)
        objd = dashboard
        objd.ui(dashboard)

    def onClick2(self, d):
        d.destroy()
        b.bookentry.ui(b.bookentry)
        objd = dashboard
        objd.ui(dashboard)

    def onClick3 ( self, d) :
        d.destroy()
        i.bookissue.ui(i.bookissue)
        objd = dashboard
        objd.ui(dashboard)


    def onClick4(self, d):
        d.destroy()
        r.bookreturn.ui(r.bookreturn)
        objd = dashboard
        objd.ui(dashboard)

    def onClick5(self, d):
        globalVar.db1.close()
        d.destroy()

    def ui(self):
        d = tk.Tk()
        d.geometry('500x150+550+300')
        d.title("DashBoard")
        button1 = tk.Button(d, width="10", height="1", text="Student Entry",command=lambda: dashboard.onClick1(self, d))
        button1.grid(row=1, column=0)
        button2 = tk.Button(d, width="10", height="1", text="Book Entry", command=lambda: dashboard.onClick2(self, d))
        button2.grid(row=1, column=1)
        button3 = tk.Button(d, width="10", height="1", text="Book issue", command=lambda: dashboard.onClick3(self, d))
        button3.grid(row=1, column=2)
        button4 = tk.Button(d, width="10", height="1", text="Book Return", command=lambda: dashboard.onClick4(self, d))
        button4.grid(row=1, column=3)
        button5 = tk.Button(d, width="10", height="1", text="Logout", command=lambda: dashboard.onClick5(self, d))
        button5.grid(row=2, column=4)
        d.mainloop()
