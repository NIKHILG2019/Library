import loginPage
import DATABASE
def onClick():
    db = DATABASE.Database_connect
    db.Database_Connection(loginPage.Entry1.get(), loginPage.Entry2.get())
    loginPage.m.destroy()