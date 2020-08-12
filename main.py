from LinkedList import (Node, LinkedList)
import random


def sep():
    print("===========================\n")


def main():
    "Main entrypoint for the app"

    # Create a list of Nodes
    nodeList = [Node(i) for i in range(0, 10)]

    # Create the Linked List and add Nodes to it
    linkedList = LinkedList(nodeList[0])
    for node in nodeList[1:]:
        linkedList.push(node)

    print(f"List: {linkedList}")
    sep()

    # Insert some Nodes
    linkedList.insert(0, Node('start'))
    linkedList.insert(5, Node('mid'))
    linkedList.insert(len(linkedList), Node('end'))
    linkedList.insert(random.randint(0, 10), Node('Rand'))

    print(f"List: {linkedList}")
    sep()

    # Pop some Nodes
    print(f"Pop(): {linkedList.pop()}")
    print(f"Remove(5): {linkedList.remove(5)}")

    print(f"List: {linkedList}")
    sep()

    # Find the random Node
    print(f"Find('Rand'): {linkedList.find('Rand')}")

    print(f"List: {linkedList}")
    sep()

    # Remove the random Node

    print(f"Remove(Rand): {linkedList.remove(linkedList.find('Rand')[0])}")

    print(f"List: {linkedList}")
    sep()


main()
