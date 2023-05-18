<!DOCTYPE html>
<html> 
<head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title >Breeds Dogs</title>
    <link rel="stylesheet" type="text/css" href="/static/content/bootstrap.min.css" />
    <link rel="stylesheet" type="text/css" href="/static/content/site.css" />
    <script src="/static/scripts/modernizr-2.6.2.js"></script>    
</head>

<body>
     <div class="navbar navbar-inverse navbar-fixed-top" style="background-color:#000000;">
        <div class="container">
            <div class="navbar-header">
                <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse">
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                </button>
                <img src = "/static/image/paws.png" height = 40 margin = 10/>
            </div>
            
            <div class="navbar-collapse collapse">
            
                <ul class="nav navbar-nav">
                    <li><a style="color: #ffa812" href="/home">Breeds Dogs</a></li>
                    <li><a style="color: #ffa812" href="/article">More about dogs</a></li>
                    <li><a style="color: #ffa812" href="/feedbackR">Your feedback</a></li>
                </ul>
            </div>
        </div>
    </div>
    <div class="container body-content">
    <div class = "name">
    </div>
        {{!base}}
        <hr />
        <div class="row" style="background-color:#000000; border-color:DarkGray; color:white">
        <footer>
            <p>&copy; {{ year }} - Dogs Breeds</p>
            </div>
        </footer>
    </div>

    <script src="/static/scripts/jquery-1.10.2.js"></script>
    <script src="/static/scripts/bootstrap.js"></script>
    <script src="/static/scripts/respond.js"></script>

</body>

</html>