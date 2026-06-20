#pragma GCC optimize("O3", "unroll-loops")
class Solution {
public:
    int numRescueBoats(vector<int>& people, int limit) {
        sort(people.begin(), people.end(), std::less<int>());       
        int x=0;
        int l = 0, r = people.size() - 1;
        while (l < r){
            x++;
            if (people[r--] + people[l] <= limit)
            {
                l++;          
            }
        }
        return x + (l == r);
    }
};