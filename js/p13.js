// Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.

var fs = require('fs'),
uu = require('underscore');

fs.readFile('./p13.txt', 'utf8', function(err, data) {
    if (err) {
        return console.log(err);
    }


    d = data.split('\n');
    var sum_array = uu.reduce(uu.map(d, function (y) { return Number(y);}),
                              function(x, y) { return x+y;})

    console.log(sum_array.toString().slice(0,10));
    // Bug answer comes out in scientific notation
});
