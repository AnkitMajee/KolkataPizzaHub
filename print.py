#!"C:/Users/Rahul1234/anaconda3/python.exe"
import cgi
import mysql.connector as conn
from decimal import *
db = conn.connect(host='localhost',user='root',passwd='',db='kph')
a=[]
sizetemp=[]
cursor = db.cursor()
i = 0

def htmlTop():
	print("""Content-type:text/html\n\n
	<!DOCTYPE html>
    <html lang="en">
    <head>
        <title>Kolkata Pizza Hub | Cart</title>
        <link rel="shortcut icon" href="images/favicon.png" type="image/x-icon">
        <!-- for-mobile-apps -->
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
        <meta name="keywords" content="Kolkata Pizza Hub" />
        <script type="application/x-javascript">
            addEventListener("load", function() {
                setTimeout(hideURLbar, 0);
            }, false);
            function hideURLbar() {
                window.scrollTo(0, 1);
            }
        </script>
        <script type="text/javascript" src="js/jquery.min.js"></script>
        <script type="text/javascript" src="js/bootstrap.min.js"></script>
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
  0% { background-color: #5bc0de; box-shadow: 0 0 3px #5bc0de; }
  50% { background-color: #5bded9; box-shadow: 0 0 40px #5bded9; }
  100% { background-color: #5bc0de; box-shadow: 0 0 3px #5bc0de; }
}

.button {
  -webkit-animation: glowing 1500ms infinite;
  -moz-animation: glowing 1500ms infinite;
  -o-animation: glowing 1500ms infinite;
  animation: glowing 1500ms infinite;
}    
</style>
    </head>
        <body style="background-image: url(images/bg.png);
                 background-repeat: repeat;
                 background-size: 20%;
                 background-color: rgba(184, 219, 38, 0.24); 
                 background-blend-mode: multiply;
                 padding-bottom: 100px;
                min-height: 100vh">
            <div class="container"><div class="col-sm-12" style="background-color: rgba(0, 0, 0, 0.3); margin-top: 100px; padding-bottom: 50px">""")
	
def htmlTail():
                print("""</div></div></body>
		</html>""")

def connectDB():
    db = conn.connect(host='localhost',user='root',passwd='',db='kph')
    cursor = db.cursor()
    return db,cursor

def selectPizza(db,cursor,pizzacart):
        #print(pizzacart)
        for key in pizzacart:
                sql = "select pizza_name,price from pizza where id=%s"%(key)
                cursor.execute(sql)
                pizza = cursor.fetchall()
        """for key in pizzacart:
                sql = "select label from topping where value=%s"%(key)
                cursor.execute(sql)
                pizza = cursor.fetchall()"""
        #print(pizza) 
        disp(pizza)
        #return pizza

def disp(pizza):
        global i
        getcontext().prec = 5
        for each in pizza:
                print("""<div class="col-sm-8 text-left"  style="margin-bottom: 10px"><h3><label class="label label-success">You Have ordered {0}</label></h3></div>""".format(each[0]))
                if sizetemp[i] == 'r':
                    print('''<div class="col-sm-4 text-right"  style="margin-bottom: 10px"><h4><label class="label label-warning">Cost is &#8377; {0}</label></h4></div>'''.format(each[1]))
                    a.append(float(each[1]))
                elif sizetemp[i] == 'm':
                    print('''<div class="col-sm-4 text-right"  style="margin-bottom: 10px"><h4><label class="label label-warning">Cost is &#8377; {0}</label></h4></div>'''.format(each[1]*Decimal(1.913043)))
                    a.append(float(each[1]*Decimal(1.3)))
                elif sizetemp[i] == 'l':
                    print('''<div class="col-sm-4 text-right" style="margin-bottom: 10px"><h4><label class="label label-warning">Cost is &#8377; {0}</label></h4></div>'''.format(each[1]*Decimal(2.8478260)))
                    a.append(float(each[1]*Decimal(1.7)))
        #print(str(a))
        i+=1
        #for i in a:
            #x+=float(i)
            #x+=float(i)
        
                      
def getData():
        formData = cgi.FieldStorage()
        value = dict()
        
        ky = formData.keys()
        for each in ky:
                temp = formData.getlist(each)
                #print(each + " " + str(temp))
                value.update({each:temp})
                test=str(value)
        
        
        
        test=test.replace("'","")
        sql="insert into orders(orderid,details) values('null','%s')"%(test)
        cursor.execute(sql)
        return value

def processing(cart,cursor):
        c=0
        for each in cart['pizzaid']:
                c+=1
        print("""<button type="button" class="btn btn-danger col-sm-12 " style="margin-bottom: 10px"><h2>No of Pizza: <span class="badge"><h3>%s</h3></span></h2></button>"""%str(c))
        for i in range(1,25):
                if ('size'+str(i)) in cart:
                        size = cart[('size'+str(i))]
                        if size==['m']:
                                #print("Size is Medium")
                                sizetemp.append('m')
                        elif size==['l']:
                                #print("Size is Large")
                                sizetemp.append('l')
                        elif size==['r']:
                                #print("Size is Regular")
                                sizetemp.append('r')
        
        #print(sizetemp)
        for each in cart['pizzaid']:
                pizzacart = dict()
                pizzacart.update({each:[]})
                top = ''
                #print(each)
                if ('size'+str(each)) in cart:
                        name =cart[('size'+str(each))]
                        #print(name)
                if ('topid'+str(each)) in cart:
                        top=(cart[('topid'+str(each))])
                        #print(cart['topid'+str(each)])
                        sql = "insert into cart(pizzaid,size,topid) values('{0}','{1}','{2}')".format(each,name[0],' '.join(top))
                else:
                        top=' '
                        sql = "insert into cart(pizzaid,size,topid) values('{0}','{1}','{2}')".format(each,name[0],top[0])
                #print(top)
                #print(pizzacart)
                (selectPizza(db,cursor,pizzacart))
                
                #print(sql)
                cursor.execute(sql)
        db.commit()
        #return pizzacart

        
if __name__ == "__main__":
    try:
        cart = dict()
        htmlTop()
        cart = getData()
        #db,cursor = connectDB()
        cursor.execute("truncate cart")
        db.commit()
        pizzacart = processing(cart,cursor)
        #pizza = selectPizza(db,cursor,pizzacart)
        cursor.close()
        print('''<div class="col-sm-12 text-center"><h1><label class="label label-info button">Your Total Amount is: &#8377; %s0</label></h1></div>'''%(sum(a)))
        print('''<div class="col-sm-3 text-right"><h4><a href="menu.py"><label class="label label-primary">Back to Menu</label></a></h4></div>''')
        print('''<div class="col-sm-8 text-right"><h4><a href="purchase.html"><label class="label label-primary">Proceed to Pay</label></a></h4></div>''')
        htmlTail()
    except:
        cgi.print_exception()

