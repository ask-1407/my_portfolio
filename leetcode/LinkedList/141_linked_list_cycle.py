class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        fast = head.next
        slow = head

        while not (fast is None or fast.next is None):
            if fast == slow:
                return True
            fast = fast.next.next
            slow = slow.next
        return False

# Hash Tableの解法
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        temp_node = head
        visited_node_tb = set()

        while temp_node:
            if temp_node in visited_node_tb:
                return True    
            visited_node_tb.add(temp_node)
            temp_node = temp_node.next
        return False