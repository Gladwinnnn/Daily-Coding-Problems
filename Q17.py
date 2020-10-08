# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.

# Input: l1 = [0], l2 = [0]
# Output: [0]

# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        placeHolder1 = l1.next
        placeHolder2 = l2.next
        temp1 = [l1.val]
        temp2 = [l2.val]
        
        while placeHolder1 != None:
            temp1.append(placeHolder1.val)
            placeHolder1 = placeHolder1.next
        while placeHolder2 != None:
            temp2.append(placeHolder2.val)
            placeHolder2 = placeHolder2.next
        
        temp1_reverse = []
        temp2_reverse = []
        
        for i in range(len(temp1)-1,-1,-1):
            temp1_reverse.append(temp1[i])
            
        for i in range(len(temp2)-1,-1,-1):
            temp2_reverse.append(temp2[i])
            
        number1 = ""
        number2 = ""
        
        for elements in temp1_reverse:
            number1 += str(elements)
        for elements in temp2_reverse:
            number2 += str(elements)
        
        total = str(int(number1) + int(number2))
        
        total_reverse = []
        
        for i in range(len(total)-1,-1,-1):
            total_reverse.append(int(total[i]))
        
        list_node = []
        for elements in total_reverse:
            result = ListNode(elements)
            list_node.append(result)
        
        a = list_node[0]
        
        for i in range(1,len(list_node)):
            list_node[i-1].next = list_node[i]
               
        return a 