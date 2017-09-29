$(document).ready(function(){
    for (var i = 1; i < 152; i++) {
        $("#pokeImg").append(`<img id="${i}" src="https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/${i}.png">`)   
    }
/*     $.get('https://pokeapi.co/api/v2/pokemon/2/', function(data){
        console.log(data);
    },'json'); */

    $('#pokeImg img').click(function(){
        var pokeNum = $(this).attr('id');
        $.get(`https://pokeapi.co/api/v2/pokemon/${pokeNum}/`, function(data){
            var name = data.name;
            var type = data.types;
            var height = data.height;
            var weight = data.weight;
            var pokeHtml = '';
            pokeHtml = `<h1 id='pokeTitle'>${name}</h1>`;
            pokeHtml += `<img src='https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/${pokeNum}.png'>`;
            pokeHtml += "<h4>Types</h4>";
            pokeHtml += "<ul>"

            for (var index = 0; index < type.length; index++) {
                console.log(type[index]);
                pokeHtml += `<li>${type[index].type.name}</li>`; 

            }  

            pokeHtml += "</ul>";
            pokeHtml += "<h4>Height</h4>";
            pokeHtml += `<p>${height}</p>`;
            pokeHtml += "<h4>Weight</h4>";
            pokeHtml += `<p>${weight}</p>`;            
            $("#pokedex").html(pokeHtml);
        }, 'json');
    })
    
})

<!-- <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Pokedex</title>
    <script src= 'http://ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js'></script>
    <link rel="stylesheet" href="pokedex.css">
    <script>
        $(document).ready(function(){
            for(var poke=1;poke<=151;poke++)
            {
                console.log(poke)
                $("#wrap").append(`<img src='https://pokeapi.co/media/img/${poke}.png' class='poke'>`)
            }
                console.log="https://pokeapi.co/api/v2/pokemon/7/"
            })
    </script>
</head>
<body>
    <div id="wrap">

    </div>
    
</body>
</html> -->
