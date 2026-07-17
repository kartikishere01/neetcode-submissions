class ListNode:
    def __init__(self, key):
        # Store the value of the node
        self.key = key

        # Pointer to the next node
        self.next = None


class MyHashSet:

    def __init__(self):
        # Create 10,000 buckets.
        # Each bucket starts with a dummy node.
        self.set = [ListNode(-1) for _ in range(10000)]

    def add(self, key: int) -> None:

        # Find the bucket using the hash function
        cur = self.set[key % len(self.set)]

        # Traverse the linked list
        while cur.next:

            # If key already exists, do nothing
            if cur.next.key == key:
                return

            # Move to the next node
            cur = cur.next

        # Key not found, insert a new node at the end
        cur.next = ListNode(key)

    def remove(self, key: int) -> None:

        # Find the correct bucket
        cur = self.set[key % len(self.set)]

        # Traverse the linked list
        while cur.next:

            # If key is found
            if cur.next.key == key:

                # Remove the node by skipping it
                cur.next = cur.next.next
                return

            # Move forward
            cur = cur.next

    def contains(self, key: int) -> bool:

        # Find the correct bucket
        cur = self.set[key % len(self.set)]

        # Traverse the linked list
        while cur.next:

            # Key found
            if cur.next.key == key:
                return True

            # Move forward
            cur = cur.next

        # Reached the end, key doesn't exist
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)