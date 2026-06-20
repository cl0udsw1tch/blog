class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        if (nums.empty())
        {
            return 0;
        }
        if (nums.size() == 1)
        {
            return nums[0] == val ? 0 : 1;
        }
        int slow = nums.size() - 1, fast = nums.size() -1;
        while (slow > -1 && nums[slow] == val)
        {
            slow--;
            fast--;
        }
        if (slow == -1)
        {
            return 0;
        }
        fast--;
        while (fast > -1)
        {
            while (fast > -1 && nums[fast] != val)
            {
                fast--;
            }
            if (fast == -1)
            {
                break;
            }
            nums[fast--] = nums[slow--];
        }
        return slow + 1;
    }
};