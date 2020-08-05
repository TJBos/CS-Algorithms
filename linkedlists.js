//create a linked list 6-->2-->4-->3-->...

class Node {
    constructor(data) {
        this.data = data;
        this.next;
    }
}

const head = new Node(6);
const nodeB = new Node(2);
const nodeC = new Node(4);
const nodeD = new Node(3);

head.next = nodeB;
nodeB.next = nodeC;
nodeC.next = nodeD;

const findNodes = (head) => {
    let count = 1
    let current = head
    while (current.next) {
        current = current.next;
        count += 1;
    }
    return count
}
console.log(findNodes(head));



