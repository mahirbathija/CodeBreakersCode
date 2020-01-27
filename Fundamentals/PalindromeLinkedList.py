# Traverse through the list to find the size
# Traverse through the list and get to the node just after the halfway point
# Reverse the second half of the list.
# Traverse thorugh first half and newly reverse second half and keep checking if node vals are the same

# PSEUDOCODE

# def isPalindrome(self, head: ListNode) -> bool:
#   size = findSize()
#   currA = head
#   while i < size/2:
#       traverse currA
#   currB = currA.next or currA.next.next if size is odd
#   currA.next = None 
#   currA = head
#   reverse(currA)
#   while currA and currB and currA.val == currB.val:
#       traverse currA and currB
#   if currA and currB is None:
#       return true
#   else:
#       return false

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        size = self.findSize(head)
        if size <= 1:
            return True
        if size == 2:
            return head.val == head.next.val
        currA = head
        for i in range(1, size//2):
            currA = currA.next
        currB = None
        if size % 2 == 0:
            currB = currA.next
        else:
            currB = currA.next.next
        currA.next = None
        self.reverse(head)
        while currA and currB and currA.val == currB.val:
            currA = currA.next
            currB = currB.next
        if currA == None and currB == None:
            return True
        return False
    

# Reverse the linked list in-place
    def reverse(self, head):
        curr = head
        prev = None
        while curr.next:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        curr.next = prev
        return curr

# Finds and returns the size of the LinkedList
    def findSize(self, head):
        size = 0
        curr = head
        while curr:
            size+=1
            curr = curr.next
        return size