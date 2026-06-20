class Solution {
public:

    char findKthBit(int n, int k) {
        
        if (n == 1)
        {
            return '0';
        }
        if (k < std::pow(2, n - 1))
        {
            return findKthBit(n - 1, k);
        }
        else if (k == std::pow(2, n - 1))
        {
            return '1';
        }
        else
        {
            return '1' == findKthBit(n - 1, std::pow(2, n) - k) ? '0' : '1';
        }
    }
};