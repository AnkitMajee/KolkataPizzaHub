
import cgi
import mysql.connector as conn
def htmlTop():
	print("""Content-type:text/html\n\n
	<!DOCTYPE html>
	<html lang="en">
		<head>
			<meta charset="utf-8"/>
			<meta HTTP-EQUIV="REFRESH" content="3; url=index.html">
			<title>Form Submit</title>
		</head>
		<body>""")
	
def htmlTail():
	print("""</body>
		</html>""")

def getData():
        formData = cgi.FieldStorage()
        name = formData.getvalue('Name')
        eid = formData.getvalue('Email')
        msg = formData.getvalue('Message')
        return name,eid,msg

def connectDB():
        db = conn.connect(host='localhost',user='root',passwd='',db='kph')
        cursor = db.cursor()
        return db,cursor
        
def createUserList(name,eid,msg):
        user = []
        user.append([name,eid,msg])
        return user
def insertUser(db,cursor,user):
        for each in user:
                sql = "insert into contact(name,emailid,message) values('{0}','{1}','{2}')".format(each[0],each[1],each[2])
                cursor.execute(sql)
        db.commit()

if __name__ == "__main__":
    try:
        htmlTop()
        db,cursor = connectDB()
        name,eid,msg = getData()
        user = createUserList(name,eid,msg)
        insertUser(db,cursor,user)
        print("<h1>Thank You for Contacting Us</h1><h2>Redirecting You to Home Page...</h2>")
        htmlTail()
    except:
        cgi.print_exception()

