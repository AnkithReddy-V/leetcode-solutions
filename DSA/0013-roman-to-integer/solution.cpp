class Solution {
public:
    int romanToInt(string s) {
        int len = s.length();
        int num[15];
        int count = 0;
        int t = 0;
        for(int i = 0; i < len; i++){
            if(s[i] == 'I'){
                num[i] = 1;
            }
            else if(s[i] == 'V'){
                num[i] = 5;
            }
            else if(s[i] == 'X'){
                num[i] = 10;
            }
            else if(s[i] == 'L'){
                num[i] = 50;
            }
            else if(s[i] == 'C'){
                num[i] = 100;
            }
            else if(s[i] == 'D'){
                num[i] = 500;
            }
            else if(s[i] == 'M'){
                num[i] = 1000;
            }
            else{
                cout<< s[i] <<  (" is invalid");
            }
        }
        for (int j = 0; j < len; j++) {
            if (j < len - 1 && num[j] < num[j + 1]) {
                count += (num[j + 1] - num[j]);
                j++; 
            } 
            else {
                count += num[j];
            }
        }
        return count;
    }
};
