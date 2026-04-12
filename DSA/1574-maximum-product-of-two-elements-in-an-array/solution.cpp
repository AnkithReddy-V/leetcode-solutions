class Solution {
public:
    int maxProduct(vector<int>& nums) {
        int p = 0;
        sort(nums.begin(), nums.end());
        reverse(nums.begin(), nums.end());
        p = ((nums[0] - 1) * (nums[1] - 1));
        return p;
    }
};
