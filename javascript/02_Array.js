// Array
let myArr = [11, 3, 23, 7]

// push() and pop() are both O(1) operations
// push()
myArr.push(17) // myArr = [11, 3, 23, 7, 17]

// pop()
myArr.pop() // myArr = [11, 3, 23, 7]

// shift() and unshift() are both O(n) operations. shifting or unshifting involve re-indexing the whole array
// shift()
myArr.shift() // [3, 23, 7 ] remove the first element in the array


// shift()
myArr.unshift(11) // [11, 3, 23, 7 ] add the element at position 0 in the array

// splice() is O(n) operations. splice() is used to add or remove item in an array. Adding or Removing item at the middle of an array is always O(n) because of re-indexing
myArr.splice(1, 0, 'new') // [ 11, 'new', 3, 23, 7 ] string 'new' added to the array


// Search by value is O(n) operations
// Search by index is O(1) operation
console.log(myArr);