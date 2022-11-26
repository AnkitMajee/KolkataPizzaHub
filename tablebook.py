print('Content-type:text/html\n\n');

def htmlTop():
	print("""
	<!DOCTYPE html>
<html lang="en">
<head>
<title>Kolkata Pizza Hub | Table Booking</title>
<link rel="shortcut icon" href="images/favicon.png" type="image/x-icon">
<!-- for-mobile-apps -->
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<meta name="keywords" content="Kolkata Pizza Hub" />
<script type="application/x-javascript"> addEventListener("load", function() { setTimeout(hideURLbar, 0); }, false);
		function hideURLbar(){ window.scrollTo(0,1); } </script>
<!--clock-->
<script src="http://cdn.jsdelivr.net/timepicker.js/latest/timepicker.min.js"></script>
<link href="http://cdn.jsdelivr.net/timepicker.js/latest/timepicker.min.css" rel="stylesheet"/>
<!-- //for-mobile-apps -->
<link href="css/bootstrap.css" rel="stylesheet" type="text/css" media="all" />
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
             max-width: 30em"><h1 class="btn btn-info">Booking Successfully Done</h1>""")
import cgi
import mysql.connector as conn	
def htmlTail():
    print("""<div align="right"><a href=index.html class="button btn btn-danger btn-sm">GoTo Home</a></div></body>
		</html>""")
	
def connectDB():
    db = conn.connect(host='localhost',user='root',passwd='',db='kph')
    cursor = db.cursor()
    return db,cursor

def getData():
        formData = cgi.FieldStorage()
        time = formData.getvalue('time')
        date = formData.getvalue('date')
        people = formData.getvalue('people')
        return time,date,people
    
def insertUser(db,cursor,time,date,people):
        sql = "insert into booking(time,date,people) values('%s','%s','%s')"%(time,date,people)
        cursor.execute(sql)
        db.commit()
    
def selectUser(db,cursor):
		sql="select bookid from booking order by bookid desc limit 1"
		cursor.execute(sql)
		user=str(cursor.fetchone()[0])
		print("""<h3>Booking ID is: {0}</h3>""".format(user))

if __name__ == "__main__":
    try:
        htmlTop()
        db,cursor = connectDB()
        time,date,people = getData()
        insertUser(db,cursor,time,date,people)
        selectUser(db,cursor)
        htmlTail()
    except:
        cgi.print_exception()

