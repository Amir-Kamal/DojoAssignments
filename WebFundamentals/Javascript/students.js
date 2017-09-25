function studentsAndInstructors(obj){
    for (var x = 0; x < obj.length; x++){

        console.log(obj[x]["first_name"] +" "+obj[x]["last_name"])
    }
}

let obj = [{first_name: "Victor", last_name: "Agbasi"},
            {first_name: "Amir", last_name: "Last"}]




studentsAndInstructors(obj);

function optional(obj){
    var num = 1;
    for (var x = 0; x < obj.length; x++){
    var count = (obj[x]["first_name"] +" "+obj[x]["last_name"]).length
        
    console.log( num +" - "+(obj[x]["first_name"] +" "+obj[x]["last_name"])+" - "+count)
    num++
    }
}

optional(obj);