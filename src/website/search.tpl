<!DOCTYPE html>
<html>
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
      <div class="container">
        <div class="page-header">
          <h1>Rechercher une installation</h1>
        </div>

        <form class="form-horizontal" action="/post" method="get">
          <fieldset>
            <legend>Rechercher</legend>
            <div class="form-group">
              <label for="select" class="col-lg-2 control-label">Activité</label>
              <div class="col-lg-10">
                <select class="form-control" id="activite">
                  <option>Football</option>
                  <option>Caca</option>
                  <option>3</option>
                  <option>4</option>
                  <option>5</option>
                </select>
              </div>
            </div>
            <div class="form-group">
              <div class="col-lg-10 col-lg-offset-2">
                <button type="submit" class="btn btn-primary">Submit</button>
              </div>
            </div>
          </fieldset>
        </form>
      </div>
   </body>
</html>