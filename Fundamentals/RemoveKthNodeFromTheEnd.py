# Traverse the LinkedList once to get the size. 
# Traverse the LinkedList the second time watching 
# out for one before the kth node from the end (now that we know the size).
# Rewire pointer from one before kth node to one after kth node.

# PSEUDOCODE

# def removeKthNodeFromEnd(head, k):
#   curr = head
#	size = 0
# 	while curr:
# 		traverse curr by l 
# 		increment size  
# 	if size > 1: 
#   	curr = head
# 		i = 1
# 		while i < size - k:
#			increment i
# 			traverse curr by 1
# 		point currs pointer two nodes ahead
# 	else:
#		head = None


def removeKthNodeFromEnd(head, k):
	curr = head
	size = 0
	while curr:
		curr = curr.next 
		size+=1  
	if size > 1:
		curr = head
		i = 1
		while i < size - k:
			curr = curr.next
			i+=1
		curr.next = curr.next.next
	else:
		head = None
