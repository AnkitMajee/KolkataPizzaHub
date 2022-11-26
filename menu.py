import cgi
import mysql.connector as conn
print("""Content-type:text/html\n\n
    <html lang="en">
    <head>
        <title>Kolkata Pizza Hub | Order Menu</title>
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
    </head>
    <body style="background-image: url(images/bg.png);
                 background-repeat: repeat;
                 background-size: 20%;
                 background-color: rgba(184, 219, 38, 0.24); 
                 background-blend-mode: multiply">
        <style>
            .btn span.glyphicon {    			
               opacity: 0;				
            }
            .btn.active span.glyphicon {				
               opacity: 1;				
            }
            .scrollbar
            {
                margin-left: 30px;
                float: left;
                height: 300px;
                //width: 65px;
                background: #F5F5F5;
                overflow-y: scroll;
            }

            .force-overflow
            {
                min-height: 300px;
            }
            #style-1::-webkit-scrollbar-track
            {
                -webkit-box-shadow: inset 0 0 6px rgba(0,0,0,0.3);
                border-radius: 10px;
                background-color: #F5F5F5;
            }

            #style-1::-webkit-scrollbar
            {
                width: 12px;
                background-color: #F5F5F5;
            }

            #style-1::-webkit-scrollbar-thumb
            {
                border-radius: 10px;
                -webkit-box-shadow: inset 0 0 6px rgba(0,0,0,.3);
                background-color: #DB7C26;
            }
        </style>
        <div class="container ">
            <caption>
                <h1 style="color: red;font-size: 72px;text-shadow: 1px 2px #000; text-align: center">Pizza</h1>
            </caption>
            <div class="table-responsive">
                <table class="table table-hover" style="background-color: #F7B538">
                    <form action="print.py" method="get" name="pizza" multiple="multiple" id="form1">
                        <thead>
                            <tr>
                                <th></th>
                                <th></th>
                                <th></th>
                                <th></th>
                            </tr>
                        </thead>""")
						
try:
    db = conn.connect(host='localhost',user='root',passwd='',db='kph')
    cursor = db.cursor()
    sql = "select * from pizza"
    cursor.execute(sql)
    pizzaNameList = cursor.fetchall()
    sql = "select * from topping"
    cursor.execute(sql)
    toppingList = cursor.fetchall()
    for each in pizzaNameList:
        print("""       <tbody>
                            <tr style="text-align: center">
                                <td style="vertical-align:middle">
                                    <div><strong style="color: black">{0}</strong></div>
                                    <img src="images\pizza_menu\{1}" hight="150px" width="150px">
                                </td>
                                <td style="vertical-align:middle">
                                    <table><tr>
                                <td style="vertical-align:middle">
                                    <div class="btn-group" data-toggle="buttons">
                                        <label class="btn btn-warning">
                                            <input type="checkbox" name="pizzaid" value="{2}"  autocomplete="off">
                                            <span class="glyphicon glyphicon-ok"></span> Add To Menu
                                        </label>
                                    </div>
                                </td>
                                <td style="vertical-align:middle"><fieldset id="size{3}">
                                    <div class="btn-group" data-toggle="buttons">
                                        
                                        <label class="radio-inline btn btn-info">
                                            <input type="radio" name="size{3}" value="l" autocomplete="off">
                                            <span class="glyphicon glyphicon-ok"></span> Large
                                        </label>
                                        <label class="radio-inline btn btn-info">
                                            <input type="radio" name="size{3}" value="m" autocomplete="off">
                                            <span class="glyphicon glyphicon-ok"></span> Medium
                                        </label>
                                        <label class="radio-inline btn btn-info">
                                            <input type="radio" name="size{3}" value="r" autocomplete="off">
                                            <span class="glyphicon glyphicon-ok"></span> Regular
                                        </label> 
                                            </fieldset>
                                    </div>
                                </td></tr>
                                <tr ><td colspan="2">&#8377; {4}/-</td></tr>
                                </table></td>
                                    """.format(each[0],each[1],each[2],each[3],each[4]))
        print("""               <td hight="300">
                                    <div class="scrollbar" id="style-1">
                                        <div class="force-overflow btn-group">
                                            <table style="background-color: azure">""")
        for i in toppingList:
            print("""                           <tr>
                                                    <td style="vertical-align:middle ">
                                                        <img src="images/pizza_top/{0}" hight="60px" width="60px">
                                                    </td>
                                                    <td style="text-align: left">
                                                        <div class="btn-group" data-toggle="buttons">
                                                            <label class="btn btn-danger">
                                                                <input type="checkbox" value="{1}" name="topid{3}" autocomplete="off">
                                                                <span class="glyphicon glyphicon-ok"></span> {2}
                                                            </label>
                                                        </div>
                                                    </td>
                                                </tr>""".format(i[0],i[1],i[2],each[3]))
        print("""                           </table>
                                        </div>
                                    </div>
                                </td>
                            </tr>""")
    print("""               <tr>
                                <td colspan="4" align="center">
                                    <div><input type="submit" class="btn btn-success" name="Proceed"></div>
                                </td>
                            </tr>
                        </tbody> 
                    </form>
                </table>
            </div>
        </div>
    </body>
    </html>""")
except:
    cgi.print_exception()
