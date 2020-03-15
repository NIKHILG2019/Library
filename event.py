import loginPage
import DATABASE
def onClick():
    db = DATABASE.Database_connect
    db.Database_Connection(loginPage.Entry1.get(), loginPage.Entry2.get())
    loginPage.m.destroy()
    import dashboard
def onClick1() :
    import dashboard
    dashboard.d.destroy()
    import studentEntry
def onClick2() :
    print("hi")

def onClick3() :
    print("hi")

def onClick4() :
    print("hi")