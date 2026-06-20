class Solution {
public:
    vector<int> findDuplicates(vector<int>& nums) {
        if (nums.size() < 2)
        {
            return {};
        }
        if (nums.size() == 2)
        {
            if (nums[0] == nums[1])
            {
                return {nums[0]};
            }
            return {};
        }
        // int start = 0;
        // vector<int> res;
        // while (start < nums.size())
        // {
        //     int slow = start;
        //     int fast = start;
            
        //     if (nums[slow] == nums.size() || nums[slow] == slow)
        //     {
        //         goto next_iteration;
        //     }
        //     do 
        //     {
        //         slow = nums[slow];
        //         fast = nums[nums[fast]];
        //     } while 
        //     (
        //         slow < nums.size() && 
        //         fast < nums.size() && 
        //         nums[fast] < nums.size() && 
        //         nums[slow] != nums[fast]
        //     );

        //     if (!(slow < nums.size() && 
        //         fast < nums.size() && 
        //         nums[fast] < nums.size() ))
        //         {
        //             goto next_iteration;
        //         }

        //     slow = nums[start];
        //     while (slow != fast)
        //     {
        //         slow= nums[slow];
        //         fast= nums[fast];
        //     }

        //     res.push_back(slow);

        //     next_iteration:
        //         start = slow+1;
        // }
        // return res;

        vector<int> res;
        for (int i = 0; i < nums.size(); i++)
        {   
            if (std::abs(nums[i]) == nums.size())
            {
                if (nums[0] < 0)
                {
                    res.push_back(std::abs(nums[i]) );
                }
                else
                {
                    nums[0] = - nums[0];

                }
      
            }
            else if (nums[std::abs(nums[i])] > 0)
            {
                nums[std::abs(nums[i])] = -1 * nums[std::abs(nums[i])];
            }
            else
            {
                res.push_back(std::abs(nums[i]));
            }
        
        }
        return res;
    }
};

// 3 7 1  | 3 
// 7 3 1  | 3