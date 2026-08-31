class Solution{
public:
    bool isPalindrome(long x) {
        if (x<0) return false;
        long original=x, reversed=0, digit;
        while(x>0){
            digit=x%10;
            reversed=reversed*10+digit;
            x/=10;
        }
        return original==reversed;
    }
};
