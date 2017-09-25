function expoReward(){
    var days = 30
    var amt = .01
    while (days !== 0){
        amt += amt
        days--
    }  
    console.log("$"+amt)
}

function til10k(){
    var amt = .01;
    var days = 0;
    while (amt <= 10000){
        amt += amt
        days++
    }
    return console.log("It would take "+days+" days to reach $10,000")
}

function tilInfinity(){
    var amt = .01;
    var days = 0;
    while (amt != Infinity){
        amt += amt
        days++
    }
    return console.log("It would take "+days+" days to reach infinity")
};

expoReward();
til10k();
tilInfinity();

