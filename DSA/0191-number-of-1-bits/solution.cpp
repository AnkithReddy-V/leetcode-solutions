class Solution {
public:
    int hammingWeight(int n) {
        int count = 0;
        int i = 0;
        while(n != 0){
            i = n%2;
            n = n/2;
            if(i == 1){
                count += 1;
            }
        }
        return count;
    }
};
