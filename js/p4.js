

function largest_palin () {
    var count = 0;

    for (var a = 100; a < 1000; a++){
        for (var b= 100; b < 1000; b++){
            var ab_str = (a*b).toString();
            if (ab_str === ab_str.split('').reverse().join('')){
                if (a*b > count){
                    count = a*b;
                }
            }
        }
    }

    return count;
};


console.log(largest_palin())
            
