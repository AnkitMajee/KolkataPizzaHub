#!"C:/Users/Rahul1234/anaconda3/python.exe"
import cgi
import mysql.connector as conn
db = conn.connect(host='localhost',user='root',passwd='',db='kph')
cursor = db.cursor()
print("""Content-type:text/html\n\n
<!DOCTYPE html>
<html lang="en">

<head>
    <title>Kolkata Pizza Hub | Coupons</title>
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
    <!-- //for-mobile-apps -->
    <link href="css/bootstrap.css" rel="stylesheet" type="text/css" media="all" />
    <link href="css/font-awesome.css" rel="stylesheet">
    <link href="css/style.css" rel="stylesheet" type="text/css" media="all" />
    <!--web-fonts-->
    <link href="//fonts.googleapis.com/css?family=Montserrat:400,700" rel="stylesheet">
    <link href="//fonts.googleapis.com/css?family=Lato:300,400,700" rel="stylesheet">
    <link href="//fonts.googleapis.com/css?family=Tangerine:400,700" rel="stylesheet">
    <link href="css/carousel.css" rel="stylesheet">
</head>
<!-- NAVBAR
================================================== -->

<body>
    <!-- banner -->
    <div class="banner inner-bg-w3" id="home">
        <!-- header -->
        <div class="banner-top">
            <div class="social-bnr-agileits">
                <ul>
                    <li><a href="#"><i class="fa fa-facebook" aria-hidden="true"></i></a></li>
                    <li><a href="#"><i class="fa fa-twitter" aria-hidden="true"></i></a></li>
                    <li><a href="#"><i class="fa fa-google-plus" aria-hidden="true"></i></a></li>
                    <li><a href="#"><i class="fa fa-linkedin" aria-hidden="true"></i></a></li>
                </ul>
            </div>
            <div class="contact-bnr-w3-agile">
                <ul>
                    <li><i class="fa fa-envelope" aria-hidden="true"></i><a href="mailto:sarthakpan@gmail.com">INFO@KPH.COM</a></li>
                    <li><i class="fa fa-phone" aria-hidden="true"></i>+91 (033)733-33-33</li>
                    <li>
                        <div class="search">
                            <input class="search_box" type="checkbox" id="search_box">
                            <label class="icon-search" for="search_box"><span class="glyphicon glyphicon-search" aria-hidden="true"></span></label>
                            <div class="search_form">
                                <form action="#" method="post">
                                    <input type="search" name="Search" placeholder="Search..." required="" />
                                    <input type="submit" value="Send" />
                                </form>
                            </div>
                        </div>
                    </li>
                </ul>
            </div>
            <div class="clearfix"></div>
        </div>
        <header>
            <div class="container">

                <!-- navigation -->
                <div class="w3_navigation">
                    <nav class="navbar navbar-default">
                        <div class="navbar-header navbar-left">
                            <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1">
						<span class="sr-only">Toggle navigation</span>
						<span class="icon-bar"></span>
						<span class="icon-bar"></span>
						<span class="icon-bar"></span>
					</button>
                            <div class="w3_navigation_pos">
                                <h1 style="text-align: center"><a href="index.html"><span>K</span>olkata <span>P</span>izza<br><span>H</span>ub</a></h1>
                            </div>
                        </div>
                        <!-- Collect the nav links, forms, and other content for toggling -->
                        <div class="collapse navbar-collapse navbar-right" id="bs-example-navbar-collapse-1">
                            <nav class="menu menu--miranda">
                                <ul class="nav navbar-nav menu__list">
                                    <li class="menu__item"><a href="index.html" class="menu__link">Home</a></li>
                                    <li class="menu__item"><a href="index.html#about" class=" menu__link">About</a></li>
                                    <li class="menu__item"><a href="index.html#particles-js" class=" menu__link">Services</a></li>
                                    <li class="menu__item menu__item--current"><a href="gallery.html" class=" menu__link">Gallery</a></li>
                                    <li class="dropdown menu__item">
                                        <a href="#" class="dropdown-toggle menu__link" data-toggle="dropdown" role="button" aria-haspopup="true" aria-expanded="false">Offer<span class="caret"></span></a>
                                        <ul class="dropdown-menu">
                                            <li><a href="coupon.py">Coupon Codes</a></li>
                                            <li><a href="coupon.py">Everyday Value</a></li>
                                        </ul>
                                    </li>
                                    <li class="menu__item"><a href="index.html#contact" class=" menu__link">Contact</a></li>
                                </ul>
                            </nav>
                        </div>
                    </nav>
                </div>
                <div class="clearfix"></div>
                <!-- //navigation -->
            </div>
        </header>
        <!-- //header -->
    </div>
    <!-- Carousel
    ================================================== -->
    <div class="introSection">
        <div class="container">
            <div class="row">
                <div class="col-lg-12">
                    <h1 class="cntr">We are launching complete online food order system for restaurent and takeaway Only at the rate <br>&#8377;195 </h1>
                </div>
            </div>
        </div>
    </div>
    <div class="container marketing">
        <h2 class="itemsTitle">Best Buy Coupons</h2>
        <div id="myCarousel1" class="carousel slide" data-ride="carousel">
            <!-- Indicators -->
            <div class="carousel-inner">
                <div class="item active">
                    <div class="row">""")
sql='select * from coupon LIMIT 3'
cursor.execute(sql)
coupon=cursor.fetchall()
for each in coupon:
    print("""               <div class="col-lg-4">
                            <img src="images/coupon.jpg" alt="Coupon Code" style="height: auto;width: 70%">
                            <h4>{0}</h4>
                            <p><a class="btn btn-default" href="#" rtitle="Copy the Code" data-toggle="popover" data-content="{1}">Copy &raquo;</a></p>
                            </div>""".format(each[0],each[1]))
print("""  </div></div>""")
sql='select * from coupon LIMIT 3,9'
cursor.execute(sql)
coupon=cursor.fetchall()
c = 0
for each in coupon:
    #print(str(each))
    if c%3==0:
        
        print("""<div class="item">
            <div class="row">""")
    print("""     <div class="col-lg-4">
                            <img src="images/coupon.jpg" alt="Coupon Code" style="height: auto;width: 70%">
                            <h4>{0}</h4>
                            <p><a class="btn btn-default" href="#" title="Copy the Code" data-toggle="popover" data-content="{1}">Copy &raquo;</a></p>
                        </div>""".format(each[0],each[1]))
    if c%3 ==2 :
        print("""</div></div>""")
    c+=1
    
print("""</div>
            <a class="left carousel-control" href="#myCarousel1" data-slide="prev"><span class="glyphicon glyphicon-chevron-left"></span></a>
            <a class="right carousel-control" href="#myCarousel1" data-slide="next"><span class="glyphicon glyphicon-chevron-right"></span></a>
        </div>
        <!-- /.carousel -->
    </div>
    <!-- FOOTER -->
    <footer>
        <div class="copyright-wthree">
            <p>&copy; 2017 Kolkata Pizza Hub . All Rights Reserved | Made with &hearts; in India</p>
        </div>
    </footer>



    <!-- Bootstrap core JavaScript
    ================================================== -->
    <!-- Placed at the end of the document so the pages load faster -->
    <script src="https://code.jquery.com/jquery-1.10.2.min.js"></script>
    <script src="js/bootstrap.min.js"></script>
    <script src="js/holder.js"></script>
    <script>
        $(document).ready(function() {
            $('[data-toggle="popover"]').popover();
        });
    </script>
</body>

</html>""")