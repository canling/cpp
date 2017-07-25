#include <iostream>
#include <vector>
#include  <algorithm>

using namespace std;

class Solution{
    public:
        int removeDuplicates(vector<int> &nums){
            return distance(nums.begin(),unique(nums.begin(),nums.end()));
        }
};
int main()
{
    cout << "Hello world!" << endl;
    return 0;
}
