import mysql.connector
class Database_connect:
    def Database_Connection(str1, str2):
        username = str1
        password = str2
        try:
            db = mysql.connector.connect(host="localhost", user=username, passwd=password, database="LIBRARY")
            c = db.cursor()
            try:
                c.execute("CREATE TABLE IF NOT EXISTS STUDENT(idNo varchar(8),name varchar(20))")
            except mysql.connector.errors as e:
                print("Error in creation of DATABASE.")
                print(e)
            choice = 0
            var = []
            while choice != 1000:
                print("Press 1 to INSERT ")
                print("Press 2 to DELETE ")
                print("Press 3 to VIEW ")
                print("Press 4 to EXIT")
                print("Press 5 to drop TABLE")
                choice = int(input("Enter your choice : "))
                if choice == 1:
                    sql = "INSERT INTO STUDENT (idNo, name) VALUES (%s, %s)"
                    n = int(input("Enter the number of entries : "))
                    for i in range(n):
                        id_no = input("Enter the id : ")
                        name = input("Enter the name : ")
                        val = (id_no, name)
                        try:
                            c.execute(sql, val)
                            db.commit()
                        except mysql.connector.errors as e:
                            print("Error in INSERTING")
                            print(e)
                elif choice == 2:
                    sql = "DELETE FROM STUDENT WHERE idNo = %s"
                    idNo = input("Enter the id you want to delete : ")
                    val = (idNo,)
                    try:
                        c.execute(sql, val)
                        db.commit()
                    except mysql.connector.errors as e:
                        print("Error in deleting")
                        print(e)
                elif choice == 3:
                    c.execute("SELECT * FROM student")
                    result = c.fetchall()
                    for i in result:
                        print(i)
                elif choice == 4:
                    choice = 1000
                    db.close()
                elif choice == 5:
                    c.execute("DROP TABLE STUDENT")
                    choice = 1000
                else:
                    print("Wrong input.")
        except mysql.connector.errors as e:
            print("Error in Connection")
            print(e)