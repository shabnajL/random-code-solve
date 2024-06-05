// leetcode#1768. Merge Strings Alternately
class Solution {
public:
    string mergeAlternately(string word1, string word2) {
        int i, j, len1, len2;
        string word = ""; 
        len1 = word1.length();
        //cout<<len1;
        len2 = word2.length();
        //cout<<len2;
        i = 0; j = 0;
        while(i<len1 || j<len2){
            if(i<len1){
                //cout<<"here";
                word.push_back(word1[i++]);
            }
            if(j<len2){
                word.push_back(word2[j++]);
            }
            //cout<<word;
        }
        return word;
    }
};
