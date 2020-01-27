# I am going to use two pointers starting at headA and headB. 
# Keep traversing while headA is not equal to headB. 
# If both pointers are None, break from the loop
# When either pointer reaches None / end of list, redirect it to the head of the other list and keep traversing.

# PSEUDOCODE

# def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
#   currA = headA
#   currB = headB
#   while currA != currB:
#     traverse currA and currB by one
#     break if currA and currB are both null
#     if currA is null:
#         point to headB
#     if currB is null:
#         point to headA
#   return currA

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:
            return None
        currA = headA
        currB = headB
        while currA is not currB:
            currA = currA.next
            currB = currB.next
            if not currA and not currB:
                break
            if not currA:
                currA = headB
            if not currB:
                currB = headA
        return currA