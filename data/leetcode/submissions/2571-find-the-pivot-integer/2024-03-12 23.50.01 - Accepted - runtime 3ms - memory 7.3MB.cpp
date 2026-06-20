class Solution {
public:
    int pivotInteger(int n) {
        if (n == 1)
        {
            return 1;
        }
        if (n == 2)
        {
            return -1;
        }
        int f_iter = 2;
        int r_iter = n - 1;
        int f_sum = 1;
        int r_sum = n;
        while (f_iter < r_iter)
        {
            if (r_sum + r_iter <= f_sum + f_iter)
            {
                r_sum += r_iter--;
            }
            else if (f_sum + f_iter <= r_sum + r_iter)
            {
                f_sum += f_iter++;
            }
            else
            {
                f_sum += f_iter++;
                r_sum -= r_iter--;
            }
        }
        return f_sum == r_sum ? r_iter : -1; // r_iter == f_iter 
    }
};