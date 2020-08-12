from LinkedList import (Node, LinkedList)
import random


def main():
    "Main entrypoint for the app"

    a = [Node(i) for i in range(0, 1000000)]

    ll = LinkedList(a[0])
    for node in a[1:]:
        ll.push(node)

    ll.insert(0, Node('start'))
    ll.insert(5, Node('mid'))
    ll.insert(len(ll), Node('end'))
    ll.insert(random.randint(0, 1000000), Node('Rand'))

    print(ll.find('Rand'))


main()
