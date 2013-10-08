var divisible = function(x){
    if (x % 3 === 0 || x % 5 == 0){
        return true;
    }else { return false; }
};

var sum = function(ary){
    var total = 0;
    for (x in ary){
        total += ary[x]
    }
    return total;
};

var multiples = function(n){
    var values = [];
    for(var i = 0; i < n ; i++){
        if (divisible(i)){
            values.push(i)
        }
    }
    return sum(values);
};


// use underscore library below //

var uu= require('underscore')

console.log(multiples(1000))


