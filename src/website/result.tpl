<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/html">
<head>
    <meta charset="utf-8">
    <title>SportsMap - Recherche</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="website/theme/bootstrap.css" media="screen">
    <link rel="stylesheet" href="website/theme/usebootstrap.css">
</head>
<body>
<nav class="navbar navbar-default navbar-fixed-top" role="navigation">
    <div class="navbar-header">
        <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1">
            <span class="sr-only">Menu</span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
        </button>
        <a class="navbar-brand" href="/index"><span class="glyphicon glyphicon-map-marker"></span> SportsMap <small>beta</small></a>
    </div>
    <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
        <ul class="nav navbar-nav">
            <li><a href="/search">Rechercher</a></li>
            <li class="dropdown">
                <a href="#" class="dropdown-toggle" data-toggle="dropdown">A propos <b class="caret"></b></a>
                <ul class="dropdown-menu">
                    <li><a href="/team">L'équipe de SportsMap</a></li>
                </ul>
            </li>
        </ul>
    </div>
</nav>
<div class = container>

     <div class="page-header">
        <h1>Résultat de la recherche</h1>
    </div>



    <div class="panel panel-default">
      <div class="panel-body">
          <h3>Saint Nazaire</h3></br>
          <p>44560 15 rue du sport</p>
      </div>
    </div>

    %for elem in liste:
        <div class="panel panel-default">
            <div class="panel-body">
                <span class="pull-left glyphicon glyphicon-home"></span><h3>{{elem[O]}}</h3></br>
                <p>elem[1]</p>
            </div>
        </div>
    %end
</div>
</body>
</html>