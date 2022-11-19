/* Big O Notation :: Worst Case
    Concepts
        :-: Drop Constant : Give O(2n) -> O(n)
        :-: Different Terms For Inputs
                function logItems(a, b) {
                    for (let i = 0; i < a; i++) { // O(a)
                        console.log(i);
                    }
                    for (let j = 0; j < b; j++) { // O(b)
                        console.log(j);
                    }
                }

                logItems(3) O(a + b)

                function logItems(a, b) {
                    for (let i = 0; i < a; i++) { // O(a)
                        for (let j = 0; j < b; j++) { // O(b)
                            console.log(i, j);
                        }
                    }
                    
                }

                logItems3(3) O(a * b)
            
        :-: Drop Non-Dominants
                function logItems(a, b) {
                    for (let i = 0; i < n; i++) { // O(n)
                        for (let j = 0; j < n; j++) { // O(n)
                            console.log(i, j);
                        }
                    }
                    for (let k = 0; k < n; k++) { // O(n)
                        console.log(k);
                    }
                    
                }
                logItems3(3) O(n * n + n) -> O(n^2 + n) n is the non-dominant term so we drop it -> O(n^2)

:_: Linear Time O(n) :: The number of operations is proportional to the number of input(n)
    Example
    function logItems1(n) {
        for (let i = 0; i < n; i++) { // O(n)
            console.log(i);
        }
    
    }

    logItems2(3) O(n) Time complexity

    Drop constant concept
    function logItems2(n) {
        for (let i = 0; i < n; i++) { // O(n)
            console.log(i);
        }
        for (let j = 0; j < n; j++) { // O(n)
            console.log(j);
        }
    }

    logItems2(3) O(n + n) = // O(2n) drop constant | now O(n) Time complexity


:_: Quadratic Time O(n^2) : The number of operations is square the number of inputs(n)

    function logItems3(n) {
        for (let i = 0; i < n; i++) { // O(n)
            for (let j = 0; j < n; j++) { // O(n)
                console.log(i, j);
            }
        }
        
    }

    logItems3(3) O(n^2)

    function logItems4(n) {
        for (let i = 0; i < n; i++) { // O(n)
            for (let j = 0; j < n; j++) { // O(n)
                    for (let k = 0; k < n; k++) { // O(n)
                    console.log(i, j, k);
                }
            }
        }
        
    }

    logItems4(3) O(n * n * n) -> O(n^3) -> O(n^2)

:_: Constant Time O(1) : The number of operation does not change as n changes
        function addItems(n) {
            return n + n;
        }

        addItems(3) O(1)

:_: Logarithmic Time O(log n) : Works on sorted data. Divide and conquer technique
*/
