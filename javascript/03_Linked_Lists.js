/* 
Linked Lists
    Don't have index
    Are Non-Contiguous __ all over the place in memory
    Have a variable called HEAD and another called TAIL
    Each node (element) has reference to the next node
    The last item point to null

Linked List Operations ___ Big O
    ___Adding item at the end is O(1)
    ___Removing | Popping item from the end is O(n)
    ___Adding or Removing item at the beginning is O(1)
    ___Adding or Removing item at the middle or any index apart from the start and end is O(n)
    ___Finding by value or index is O(n)

NODE: Comprises of the value and the pointer. Is actually an object that has a value and a next key.
    {
        value: 4,
        next: null
    }

    Example
    {
        Head: {
            value: 11,
            next: {
                value: 22,
                next: {
                    value: 7,
                    next: {
                        value: 4,
        Tail----------> next: null,
                    }
                }
            }
        }
    }

    ___________________~~~~~~~~~~~~~~____________________
    #1
    class LinkedList {
        constructor(value) {....} // Create a new node

        __LinkedList Add Elements Operations__
        push(value) {....} // Create a new node and add node to end
        unShift(value) {....} // Create a new node and add to beginning
        insert(index, value) {.....} // Create a new node and add to any position
    }

    #2
    Class to create new node
    class Node {
        constructor(value) {
            this.value = value,
            this.next = null // because is not pointing to anything/node yet
        }
    }

    For example to create a node we write
    const newNode = new Node(4)  ===== newNode = {
                                                    value: 4,
                                                    next: null
                                                 }
    the new keyword is calling the constructor of the class Node

    class LinkedList {
        constructor(value) {
            const newNode = new Node(value) // Calls the Node class and create new node. The new keyword is calling the constructor of the Node class
            this.head = newNode
            this.tail = this.head  // tail is pointing to the same node the head is pointing
            this.length = 1  //Keeping track
        }

        Push method :: Create a new node
        push(value) {
            const newNode = new Node(value)
            if(!this.head) { // if linkedList head is empty then set
                this.head = newNode
                this.tail = newNode
            }
            else { // if !empty the set
                this.tail.next = newNode
                this.tail = newNode
            }
            this.length++ // increment linkedList length
            return this
        }

    }

    To create a linkedList
    let newLinkedList = new LinkedList(4)

*/

class Node {
    constructor(value) {
        this.value = value,
        this.next = null // because is not pointing to anything/node yet
    }
}

class LinkedList {
    constructor(value) {
        const newNode = new Node(value) // Calls the Node class and create new node. The new keyword is calling the constructor of the Node class
        this.head = newNode
        this.tail = this.head  // tail is pointing to the same node the head is pointing
        this.length = 1  //Keeping track
    }

    push(value) {
        const newNode = new Node(value)
        if (!this.head) {
            this.head = newNode
            this.tail = newNode
        }
        else {
            this.tail.next = newNode
            this.tail = newNode
        }
        this.length++
        return this
    }
}

let newLinkedList = new LinkedList(4)
newLinkedList.push(7)

console.log(newLinkedList);