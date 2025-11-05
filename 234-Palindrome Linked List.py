# array:time:O(n), space:O(n)
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

        
class SolutionL:
    def isPalindrome(self, head:ListNode):
        nums = []

        while head:
            nums.append(head.val)
            head = head.next
            
        l, r =0, len(nums)-1
        while l <= r:
            if nums[l] != nums[r]:
                return False
            l += 1
            r -= 1
        return True


# Two pointer: Fast & Slow
# array:time:O(n), space:O(1)
class Solution:
    def isPalindrome(self, head:ListNode):
        fast = head
        slow = head

        # find middle(slow)
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # reverse second half
        prev = None
        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp

        # check palindrome
        left, right = head, prev
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True







