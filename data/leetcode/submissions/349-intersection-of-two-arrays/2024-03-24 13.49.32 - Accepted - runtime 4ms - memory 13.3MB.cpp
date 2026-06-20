class Solution {
public:
    static bool sorter(const int& num1, const int& num2)
    {
        return num1 < num2;
    }
    vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {
        
        if (nums1.size() == 0 || nums2.size() == 0)
        {
            return {};
        }
        int ptr1 = 0, ptr2 = 0;
        std::sort(nums1.begin(), nums1.end(), sorter);
        std::sort(nums2.begin(), nums2.end(), sorter);
        vector<int> res;
        while (ptr1 < nums1.size() && ptr2 < nums2.size())
        {
            if (nums1[ptr1] < nums2[ptr2])
            {
                ptr1++;
            }
            else if (nums1[ptr1] > nums2[ptr2])
            {
                ptr2++;
            }
            else if (nums1[ptr1] == nums2[ptr2])
            {
                int curr = nums1[ptr1] ;
                res.push_back(nums1[ptr1]);

                while(ptr1 < nums1.size() && nums1[ptr1] == curr)
                {
                    ptr1++;
                }
                while(ptr2 < nums2.size() && nums2[ptr2] == curr)
                {
                    ptr2++;
                }
            }
        }
        return res;
    }
};