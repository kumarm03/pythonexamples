#author:kumar
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA == None or headB == None:
            return None
        
        pa, pb = headA, headB
        while pa!=pb:
            if pa == None:
                pa = headB
            else:
                pa = pa.next
            
            if pb == None:
                pb = headA
            else:
                pb = pb.next
        
        return pa

				
class Solution:
    # @param two ListNodes
    # @return the intersected ListNode
    def getIntersectionNode(self, headA, headB):
        curA, curB = headA, headB
        begin, tailA, tailB = None, None, None
        
        while curA and curB:
            if curA == curB:
                begin = curA
                break
                
            if curA.next:
                curA = curA.next
            elif tailA is None:
                tailA = curA
                curA = headB
            else:
                break
            
            if curB.next:
                curB = curB.next
            elif tailB is None:
                tailB = curB
                curB = headA
            else:
                break
        
        return begin