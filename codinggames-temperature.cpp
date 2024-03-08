#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <limits>

using namespace std;

/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/

int main()
{
    int n; // the number of temperatures to analyse
    cin >> n; cin.ignore();
    if(n==0){
        cout << 0 << endl;
        return 0;
    }
    int arr[1005];
    int min = numeric_limits<int>::max(); 
    for (int i = 0; i < n; i++) {
        int t; // a temperature expressed as an integer ranging from -273 to 5526
        cin >> t; cin.ignore();
        // cout<<t<<endl;
        arr[i] = t;
        
        if (abs(arr[i]) < abs(min) or (abs(arr[i]) == abs(min) and arr[i]>min))
            min = arr[i];
            //cout<< min <<endl;
    }

    // Write an answer using cout. DON'T FORGET THE "<< endl"
    // To debug: cerr << "Debug messages..." << endl;

    cout << min << endl;
    
}
