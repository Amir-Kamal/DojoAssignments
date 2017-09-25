function whatsTheTime(HOUR, MINUTE, PERIOD){
    if (MINUTE < 30){
        if (PERIOD === "AM"){
            console.log("It's just after "+ HOUR +" in the "+"morning");
        }
        else if(PERIOD === "PM"){
            console.log("It's just after "+ HOUR +" in the "+"evening");
        }
    }
    else if (MINUTE >= 30);
        {
        if (PERIOD === "AM"){
            console.log("It's almost "+ HOUR +" in the "+"morning");
        }
        else if(PERIOD === "PM"){
            console.log("It's almost "+ HOUR +" in the "+"evening");
        }

    }
}

whatsTheTime(9, 3, "AM");