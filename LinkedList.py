class Node:
    """A single Node in a Linked List

    :return: a single Node in a Linked List
    :rtype: Node
    """

    data = None
    next = None

    def __init__(self, data=None):
        """Constructor for Node

        :param data: Node value, defaults to None
        :type data: Any, optional
        """

        self.data = data
        self.next = None

    def __repr__(self) -> str:
        """The string representation of the Node

        :return: The string representation of the Node
        :rtype: str
        """
        return f"[{self.data}]"


class LinkedList:
    """A Linked List

    :raises IndexError: For positions outside of the list's scope
    :raises TypeError: For any inserted values that are not Node
    :return: Linked List class
    :rtype: LinkedList
    """

    head = None
    length = 0

    def __init__(self, node: Node):
        """Constructor for the LinkedList

        :param node: The Node to be added
        :type node: Node
        """

        self._checkType(node)
        self.head = node
        self.length += 1

    def push(self, node: Node):
        """Push a Node to the end of the list

        :param node: The Node to be added
        :type node: Node
        """

        self._checkType(node)

        if not self.head:
            self.head = node
            return

        currNode = self._getLastNode()

        currNode.next = node
        self.length += 1

    def insert(self, position: int, node: Node):
        """Insert a Node at given location, or at the end if out of scope

        :param position: The position to be inserted at
        :type position: int
        :param node: The Node to be added
        :type node: Node
        :raises IndexError: For any positions outside of the list scope
        """

        self._checkType(node)
        if position < 0:
            raise IndexError("Position must be 0 or larger")

        if self.length == 0 or position >= self.length:
            self.push(node)
        else:
            prevNode = None
            currNode = self.head
            currIndex = 0

            while currNode.next is not None:
                if position == currIndex:
                    if not prevNode:
                        self.head = node
                    else:
                        prevNode.next = node
                    node.next = currNode
                    break

                prevNode = currNode
                currNode = currNode.next
                currIndex += 1

    def pop(self) -> Node:
        """Remove the last Node in the list

        :return: The last Node in the list
        :rtype: Node
        """

        currNode = self.head
        while currNode.next.next:
            currNode = currNode.next

        retNode = currNode.next
        currNode.next = None
        self.length -= 1

        retNode.next = None
        return retNode

    def remove(self, position: int) -> Node:
        """Remove a Node at a given position

        :param position: The position from which to remove the Node
        :type position: int
        :raises IndexError: For any positions outside of the List scope
        :return: The Node at the given location
        :rtype: Node
        """

        if position < 0 or position >= self.length:
            raise IndexError(f"Position must not be < 0 or >= {self.length}")

        retNode = None
        prevNode = None
        currNode = self.head
        currIndex = 0

        while currNode is not None:
            if position == currIndex:
                retNode = currNode
                if not prevNode:
                    self.head = currNode.next
                else:
                    prevNode.next = currNode.next

            prevNode = currNode
            currNode = currNode.next
            currIndex += 1

        retNode.next = None
        return retNode

    def find(self, searchTerm: any) -> Node:
        """Search the Linked List for a Node with a given value

        :param searchTerm: Value to search by
        :type searchTerm: any
        :return: The Node with the given value OR None
        :rtype: Node
        """

        currNode = self.head
        currIndex = 0

        while currNode:
            if currNode.data == searchTerm:
                return (currIndex, currNode)
            currNode = currNode.next
            currIndex += 1

        return currNode  # None

    def _getLastNode(self) -> Node:
        """Get the last Node in the list

        :return: The last Node in the list
        :rtype: Node
        """

        currNode = self.head
        while currNode.next:
            currNode = currNode.next
        return currNode

    def _checkType(self, node: Node):
        """Check the node type. If not Node raise Exception

        :param node: The Node to be tested
        :type node: Node
        :raises TypeError: For any Nodes that are not of Node type
        """

        if type(node) != Node:
            raise TypeError(f"Input must be a Node - {type(node)} != Node")

    def __repr__(self) -> str:
        """The string representation of the LinkedList

        :return: The string representation of the LinkedList
        :rtype: str
        """

        currNode = self.head

        res = ""

        while currNode is not None:
            res += f"[{str(currNode.data)}] -> "
            currNode = currNode.next
        res += "None"
        return res

    def __len__(self) -> int:
        """The length of the list

        :return: The length of the list
        :rtype: int
        """
        return self.length
