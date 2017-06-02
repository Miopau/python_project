<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>SportsMap - Accueil</title>
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
    <div id="carousel-example" class="carousel slide" data-ride="carousel">
  <ol class="carousel-indicators">
    <li data-target="#carousel-example" data-slide-to="0" class="active"></li>
    <li data-target="#carousel-example" data-slide-to="1"></li>
    <li data-target="#carousel-example" data-slide-to="2"></li>
  </ol>

  <div class="carousel-inner">
    <div class="item active">
      <a href="#"><img src="website/img/paysloire.png" /></a>
      <div class="carousel-caption">
        <h3>Un service</h3>
        <p>basé sur les bases de données de la région.</p>
      </div>
    </div>
    <div class="item">
      <a href="#"><img src="http://placekitten.com/1600/600" /></a>
      <div class="carousel-caption">
        <h3>Meow</h3>
        <p>Just Kitten Around</p>
      </div>
    </div>
    <div class="item">
      <a href="#"><img src="http://placekitten.com/1600/600" /></a>
      <div class="carousel-caption">
        <h3>Meow</h3>
        <p>Just Kitten Around</p>
      </div>
    </div>
  </div>

  <a class="left carousel-control" href="#carousel-example" data-slide="prev">
    <span class="glyphicon glyphicon-chevron-left"></span>
  </a>
  <a class="right carousel-control" href="#carousel-example" data-slide="next">
    <span class="glyphicon glyphicon-chevron-right"></span>
  </a>
</div>

<hr/>

        <div class="row">
        		<div class="col-md-7">
        			<img style="max-width: 100%" src="website/img/gymnase.png"/>
        		</div>
        		<div class="col-md-5">
        			<h3>Effectuez votre première recherche en toute simplicité !</h3>
        			<p>SportsMap vous permet de trouvez des installations sportives de la manière la plus simple au monde. Il vous suffit de renseigner quelques informations et SportsMap vous offrira des solutions adaptés à vos besoins.</p>
        			<a href="/search"><button class="btn btn-block btn-primary">Effectuez votre première recherche !</button></a>
        		</div>
        	</div>


        <div class="home_title">
		Quelques fonctionnalités disponibles
	</div>
	<div class="row">
		<!-- PREMIERE COLONNE -->
		<div class="col-md-4">
			<div class="row">
				<div class="col-md-2">
					<span class="glyphicon glyphicon-ok glyphicon-bigicon"></span>
				</div>
				<div class="col-md-8">
					<h4>Un service efficace</h4>
					<p>Ce service fonctionne sur une base de données complète fournise par la région et régulièrement mise à jour.</p>
				</div>
			</div>
		</div>
		<!-- DEUXIEME COLONNE -->
		<div class="col-md-4">
			<div class="row">
				<div class="col-md-2">
					<span class="glyphicon glyphicon-map-marker glyphicon-bigicon"></span>
				</div>
				<div class="col-md-8">
					<h4>Affichage de l'emplacement</h4>
					<p>Affiche une carte Google Maps pour localiser facilement l'installation.</p>
				</div>
			</div>
		</div>
		<!-- TROISIEME COLONNE -->
		<div class="col-md-4">
			<div class="row">
				<div class="col-md-2">
					<span class="glyphicon glyphicon-search glyphicon-bigicon"></span>
				</div>
				<div class="col-md-8">
					<h4>Recherche avancée</h4>
					<p>Vous pouvez recherchez soit une activité, soit une installation, soit un équipement particulier.</p>
				</div>
			</div>
		</div>
	</div>
</div>

<div class="footer" style="clear: both;">
   <small>
      <center>
         <hr/>
         Le site utilise <a href="http://getbootstrap.com" target="_blank">Bootstrap</a> ainsi que le thème <a target="_blank" href="http://bootswatch.com/yeti/">Yeti</a>. 
         <br/>Développé par <a href ="https://www.linkedin.com/in/florian-vallet-593020120/" target="_blank">Florian Vallet</a> et <a href ="http://matthieubernard.me" target="_blank">Matthieu Bernard</a> !<br/>
   </small>
</div>


    <script src="https://code.jquery.com/jquery-1.10.2.min.js"></script>
    <script src="website/bootstrap/bootstrap.min.js"></script>
	<script src="website/bootstrap/usebootstrap.js"></script>
  </body>
</html>
