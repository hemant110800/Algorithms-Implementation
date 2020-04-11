'''
Consider two files having the following data:
File1: "ACA"      File2: "ADCE"

To find the difference between these two files:
Find the longest sequence of characters present in both the files.
This is a classic problem which can be solved using dynamic programming technique.
Longest common subsequence (LCS) is "AC"
Using the LCS, we can find out
The characters which are absent in the sequence and present in File1 (i.e. the deleted characters)
Deleted character(s): "A"
The characters which are absent in the sequence and present in File2 (i.e. the inserted characters)
Inserted characters: "DE"
Thus, in this case the difference between the two files are:
D A E
+ - +
where + indicates characters inserted in File2 and – indicates characters deleted from File1.
'''


def longest_common_subsequence(text1,text2):

    # find the length of the strings
    m = len(text1)
    n = len(text2)

    # declaring the list for storing the dynamic programming values
    LCS = [[None]*(n+1) for i in range(m+1)]

    """Following steps build LCS[m+1][n+1] in bottom up fashion using dynamic programming principle
    Note: LCS[i][j] contains length of Longest Common Subsequence of text1[0..i-1] and text2[0..j-1]"""
    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0 :
                LCS[i][j] = 0
            elif text1[i-1] == text2[j-1]:
                LCS[i][j] = LCS[i-1][j-1]+1
            else:
                LCS[i][j] = max(LCS[i-1][j] , LCS[i][j-1])
    #print(LCS[m][n])

    # Following code is used to find out the LCS string using the LCS list created above
    o = LCS[m][n]

    # Create a list to store the characters of LCS string
    lcs_chars = [""] * (o)

    i = m
    j = n
    while i > 0 and j > 0:
        # If current character in text1 and text2 are same, then
        # current character is part of LCS
        if text1[i-1] == text2[j-1]:
            lcs_chars[o-1] = text1[i-1]
            i-=1
            j-=1
            o-=1

        # If not same, then find the larger of two and
        # go in the direction of larger value
        elif LCS[i-1][j] > LCS[i][j-1]:
            i-=1
        else:
            j-=1

    #Concatenate the characters in the list to form the LCS string
    lcs_str=""
    for char in lcs_chars:
        lcs_str+=char

    return lcs_str


def diff(text1,text2):
    print("Text1:",text1)
    print("Text2:",text2)
    lcs_str=longest_common_subsequence(text1,text2)
    print("Common characters:",lcs_str)

    #Length of text1, text2 and LCS string
    m=len(text1)
    n=len(text2)
    o=len(lcs_str)

    del_chars=[]
    ins_chars=[]

    #Find the characters absent in LCS string and present in text1
    j=0
    for i in range(0,m):
        if(text1[i] in lcs_str[j:o]):
            j+=1
        else:
            del_chars.append(text1[i])
    print("Characters deleted from text1:", del_chars)

    #Find the characters absent in LCS string and present in text2
    j=0
    for i in range(0,n):
        if(text2[i] in lcs_str[j:o]):
            j+=1
        else:
            ins_chars.append(text2[i])
    print("Characters inserted in text2:",ins_chars)



diff("ACA", "ADCE")               

