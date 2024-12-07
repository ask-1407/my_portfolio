class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        node=head
        visited=set() 

        while node :
            if node in visited:
                return node
            visited.add(node)
            node = node.next
        return None

# フロイドの循環検知法
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        else:
            return None

        start_of_cycle = head
        collision_point = slow
        while start_of_cycle != collision_point:
            start_of_cycle = start_of_cycle.next
            collision_point = collision_point.next

        return collision_point