class Solution {
public:
    string makeGood(string s) {
        string q = s;
        string t;
        while (true)
        {
            int nreds = 0;
            int i = 0;
            while (i < q.size())
            {
                if (i == q.size() - 1){
                    t+=q[i]; break;
                }
                if ((abs((int)q[i] - (int)q[i+1]) == 32))
                {
                    i+=2;
                    nreds++;
                }
                else
                {
                    t+=q[i];
                    i++;
                }
            }
            q = t;
            t = {};
            if (!nreds)
            {
                break;
            }
        }
        return q;
    }
};