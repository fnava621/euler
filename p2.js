

var fib = function(n){

    if (n === 0){
        return 1;
    }else if (n == 1){
        return 2;
    }else{
        return fib(n-1) + fib(n-2);
    }
    
};        


var fib1 = function(n){
    var memo = [1,2];
    var rec = function(n){
        var result = memo[n];
        if (typeof result !== 'number'){
            result = rec(n-1) + rec(n-2);
            memo[n] = result;
        }
        return result;
    };

    rec(n);
    return memo;
};


var fib2 = function(n){
    var x = [];
    function fib_iter (a, b, c){
        if (1 === c){
            x.push(b)
            return b;
        }else{
            return fib_iter((a+b), a, (c - 1));
        }
    };
    fib_iter(2, 1, n);
    return x
}
            
            
    


console.log(fib2(10))
