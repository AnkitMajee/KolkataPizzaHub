#!"C:/Users/Rahul1234/anaconda3/python.exe"
import cgi
import mysql.connector as conn
def htmlTop():
	print("""Content-type:text/html\n\n

<html lang="en">
<head>
<title>Kolkata Pizza Hub | Table Booking</title>
<link rel="shortcut icon" href="images/favicon.png" type="image/x-icon">
<!-- for-mobile-apps -->
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<meta name="keywords" content="Kolkata Pizza Hub" /><link href="css/bootstrap.css" rel="stylesheet" type="text/css" media="all" />
<link href="css/font-awesome.css" rel="stylesheet"> 
<link href="css/style.css" rel="stylesheet" type="text/css" media="all" />
<!--web-fonts-->
<link href="//fonts.googleapis.com/css?family=Montserrat:400,700" rel="stylesheet">
<link href="//fonts.googleapis.com/css?family=Lato:300,400,700" rel="stylesheet">
<link href="//fonts.googleapis.com/css?family=Tangerine:400,700" rel="stylesheet">
<!--//web-fonts-->
<style>
@keyframes glowing {
  0% { background-color: #B20000; box-shadow: 0 0 3px #B20000; }
  50% { background-color: #FF0000; box-shadow: 0 0 40px #FF0000; }
  100% { background-color: #B20000; box-shadow: 0 0 3px #B20000; }
}

.button {
  -webkit-animation: glowing 1500ms infinite;
  -moz-animation: glowing 1500ms infinite;
  -o-animation: glowing 1500ms infinite;
  animation: glowing 1500ms infinite;
}    
</style>
</head>
<body style="align-items: center;
             margin: 10em; border: 2px;
             border-bottom-color: blueviolet;
             border-bottom-style: groove;
             border-top-style: dashed;
             border-left-style: dashed;
             border-right-style: dashed;
             padding: 10px;
             max-width: 30em">""")
	
def htmlTail():
	print("""</body>
		</html>""")

def getData():
        formData = cgi.FieldStorage()
        name = formData.getvalue('customer_name')
        phno = formData.getvalue('phone_number')
        eid = formData.getvalue('email_address')
        address = formData.getvalue('address')
        return name,phno,eid,address

def connectDB():
        db = conn.connect(host='localhost',user='root',passwd='',db='kph')
        cursor = db.cursor()
        return db,cursor
        
def createUserList(name,phno,eid,address):
        user = []
        user.append([name,phno,eid,address])
        return user
def insertUser(db,cursor,user,orderid):
        for each in user:
                sql = "update orders SET name = '{0}', phno  = {1}, eid = '{2}', address = '{3}' WHERE orders.orderid = {4}".format(each[0],each[1],each[2],each[3],orderid)
                #print(sql)
                cursor.execute(sql)
        db.commit()

def getDetail(db,cursor):
    sql = "select orderid from orders order by orderid DESC LIMIT 1"
    cursor.execute(sql)
    orderid = str(cursor.fetchone()[0])
    return orderid
if __name__ == "__main__":
    try:
        htmlTop()
        db,cursor = connectDB()
        orderid = getDetail(db,cursor)
        name,phno,eid,address = getData()
        user = createUserList(name,phno,eid,address)
        insertUser(db,cursor,user,orderid)
        
        print('''<h1 class="btn btn-info">Thank You</h1><h2>Your Order has beed successfully placed</h2><div class="jumbotron" style="float:right"><h1 class="button btn btn-danger btn-sm">Your Order Id is: %s</h1></div>'''%(orderid))
        htmlTail()
    except:
        cgi.print_exception()

