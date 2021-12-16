import sys
from jinja2 import Template

# try:
    
# except ImportError:
#     print("[-] Install required third-party module jinja2")
#     sys.exit(1)


DASH = Template("""<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8" />
    <link rel="icon" type="image/png" href="assets/img/favicon.ico">
    <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1" />

    <title>Light Bootstrap Dashboard</title>

    <meta content='width=device-width, initial-scale=1.0,
      maximum-scale=1.0, user-scalable=0' name='viewport' />
    <meta name="viewport" content="width=device-width" />


    <!-- Bootstrap core CSS     -->
    <link href="assets/css/bootstrap.min.css" rel="stylesheet" />

    <!-- Animation library for notifications   -->
    <link href="assets/css/animate.min.css" rel="stylesheet"/>

    <!--  Light Bootstrap Table core CSS    -->
    <link href="assets/css/light-bootstrap-dashboard.css" rel="stylesheet"/>


    <!--  CSS for Demo Purpose, don't include it in your project     -->
    <link href="assets/css/demo.css" rel="stylesheet" />


    <!--     Fonts and icons     -->
    <link href="
      http://maxcdn.bootstrapcdn.com/font-awesome/4.2.0/css/
      font-awesome.min.css" rel="stylesheet">
    <link href='http://fonts.googleapis.com/css?family=Roboto:400,700,300'
      rel='stylesheet' type='text/css'>
    <link href="assets/css/pe-icon-7-stroke.css" rel="stylesheet" />

</head>
<body>

<div class="wrapper">
    <div class="sidebar" data-color="purple"
      data-image="assets/img/sidebar-5.jpg">

    <!--
        Tip 1: you can change the color of the sidebar using:
          data-color="blue | azure | green | orange | red | purple"
        Tip 2: you can also add an image using data-image tag
    -->

        <div class="sidebar-wrapper">
            <div class="logo">
            </div>

            <ul class="nav">
                <li class="active">
                    <a href="dashboard.html">
                        <i class="pe-7s-graph"></i>
                        <p>Dashboard</p>
                    </a>
                </li>
                <li>
                    <a href="table.html">
                        <i class="pe-7s-note2"></i>
                        <p>Table List</p>
                    </a>
                </li>
            </ul>
        </div>
    </div>

    <div class="main-panel">
        <nav class="navbar navbar-default navbar-fixed">
            <div class="container-fluid">
                <div class="navbar-header">
                    <button type="button" class="navbar-toggle"
                      data-toggle="collapse"
                      data-target="#navigation-example-2">
                        <span class="sr-only">Toggle navigation</span>
                        <span class="icon-bar"></span>
                        <span class="icon-bar"></span>
                        <span class="icon-bar"></span>
                    </button>
                    <a class="navbar-brand" href="#">Dashboard Example</a>
                </div>
            </div>
        </nav>


        <div class="content">
            <div class="container-fluid">
                <div class="row">
                <div class="col-md-4">
                <h4>Custodians: <b>{{num_custodians}}</b></h4>
                </div>
                <div class="col-md-4">
                <h4>Devices Preserved: <b>{{num_devices}}</b></h4>
                </div>
                <div class="col-md-4">
                <h4>Total Data Preserved: <b>{{data}}</b></h4>
                </div>
                </div>
                <div class="row">
                    <div class="col-md-6">
                        <div class="card">
                            <div class="header">
                                <h4 class="title">Acquired Device Types</h4>
                                <p class="category">Breakdown of Device
                                  Type</p>
                            </div>
                            <div class="content">
                                <div id="chartPreferences"
                                  class="ct-chart ct-perfect-fourth"></div>

                                <div class="footer">
                                </div>
                            </div>
                        </div>
                    </div>

                <div class="col-md-6">
                    <div class="card">
                        <div class="header">
                            <h4 class="title">Custodian Devices</h4>
                            <p class="category">Breakdown of Devices per
                              Custodian</p>
                        </div>
                        <div class="content">
                            <div id="chartPreferences2" class="ct-chart"></div>

                            <div class="footer">
                            </div>
                        </div>
                    </div>
                </div>
            </div>


                <div class="row">
                    <div class="col-md-12">
                        <div class="card ">
                            <div class="header">
                                <h4 class="title">Preserved Data per
                                  Day</h4>
                                <p class="category">Acquired Data per
                                  Acquistion Date</p>
                            </div>
                            <div class="content">
                                <div id="chartActivity" class="ct-chart">
                                </div>

                                <div class="footer">
                                    <div class="legend">
                                        <i class="fa fa-circle
                                        text-info"></i> Size (GB)
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
    </div>

                                <div class="footer">
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>


</body>

    <!--   Core JS Files   -->
    <script src="assets/js/jquery-1.10.2.js" type="text/javascript">
    </script>
    <script src="assets/js/bootstrap.min.js" type="text/javascript">
    </script>

    <!--  Checkbox, Radio & Switch Plugins -->
    <script src="assets/js/bootstrap-checkbox-radio-switch.js"></script>

    <!--  Charts Plugin -->
    <script src="assets/js/chartist.min.js"></script>

    <!--  Notifications Plugin    -->
    <script src="assets/js/bootstrap-notify.js"></script>

    <!--  Google Maps Plugin    -->
    <script type="text/javascript"
    src="https://maps.googleapis.com/maps/api/js?sensor=false"></script>

    <!-- Light Bootstrap Table Core javascript and methods for
      Demo purpose -->
    <script src="assets/js/light-bootstrap-dashboard.js"></script>

    <!-- Light Bootstrap Table DEMO methods, don't include it in
      your project! -->
    <script src="assets/js/demo.js"></script>

    <script type="text/javascript">
        $(document).ready(function(){

            demo.initChartist();

        });
    </script>

</html>
""")