function bonjour(){
	var leprenom;
	var letext;
	leprenom = document.getElementById("prenom").value;
	letext = "coucou "+leprenom;
	document.getElementById("salut").value=letext;
	}
	
function fermer(){ 
close();
}

function explication(){
	alert("entrer votre prenom dans le formulaire puis cliquer sur bonjour");
}

function message(){
	alert("il se passe quelque chose");
}
	