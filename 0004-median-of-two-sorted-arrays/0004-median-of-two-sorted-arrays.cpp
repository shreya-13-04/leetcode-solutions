#include <iostream>
#include <algorithm>
using namespace std;


class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        size_t n1=nums1.size();
        size_t n2=nums2.size();
        size_t m=n1+n2;

        vector<int> merged;
        merged.reserve(m);
        merged.insert(merged.end(), nums1.begin(), nums1.end());
        merged.insert(merged.end(), nums2.begin(), nums2.end());

        sort(merged.begin(), merged.end());
        

        if (m%2==0){
            return (merged[m/2-1] + merged[m/2])/2.0;
        }
        else{
            return (merged[m/2]);
        }



        
        
    }
};