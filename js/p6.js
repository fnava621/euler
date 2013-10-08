var uu = require('underscore')


function sum (ary){
    return uu.reduce(ary, function (x, y) { return x + y;});
}


function sum_of_squares(x){
    var list_numbers = uu.range(1,x+1);
    return sum(uu.map(list_numbers, function(y){ return Math.pow(y, 2);}));
}
    

function square_of_sum(x){
    return Math.pow(sum(uu.range(1,x+1)), 2);
}

function sum_of_square_diff(x){
    return square_of_sum(x) - sum_of_squares(x);
}

console.log(sum_of_square_diff(100))
