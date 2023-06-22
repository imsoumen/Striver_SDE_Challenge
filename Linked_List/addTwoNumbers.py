class Node:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next


# Don't change the code above.


def addTwoNumbers(head1: Node, head2: Node) -> Node:
    # Write your code here.
    node1 = head1
    node2 = head2

    sumHead = None

    prev = None

    sum = carry = 0

    while node1 != None or node2 != None:
        sum = carry

        if(node1 != None):
            sum += node1.data

            node1 = node1.next

        if(node2 != None):
            sum += node2.data

            node2 = node2.next

        sumNode = Node(sum % 10)

        if (sumHead == None):
            sumHead = sumNode
        else:
            prev.next = sumNode

        prev = sumNode

        carry = sum // 10

    if(carry > 0):
        prev.next = Node(carry)

    return sumHead

