'''Ex. 394 Decode String'''
''' 
Pseudo code (Brain storm, ver 1.0)
1. read "[" - record last index
2. from that index, read the first "]", record the index
3. rephrase the input (e.g. 3[a2[c]] -> 3[acc])
4. repeat step 1

Pseudo code (Brain storm, ver 1.1)
1. read the first "]", record index
2. find the first "[" from the result above
3. rephrase as step 3 in ver 1.0
4. repeat step 1
'''

pair = 0
s0 = s = "3[a[2c]]"
target = []
bracket_idx = s0.index(']')
for i in range(bracket_idx,-1,-1):
    if s0[i].isalpha():
        target.insert(0, s0[i])
    elif s0[i].isnumeric():
        count = s0[i] - 1
        while count != 0:
            target.insert(0, target[0])
            count -= 1
