class Solution:
    def dividingStrings(self, seq1: str, seq2: str) -> str:
        '''
        seq1: the longer string
        seq2: the shorter string
        '''
        for i in range(len(seq2)):
            test_seq = seq2[:i + 1]
            ans = seq1.split(test_seq)
            if all(i == '' for i in ans):
                if len(seq2) % len(test_seq) == 0:
                    ans = seq1.split(test_seq * (len(seq2) // len(test_seq)))
                    if all(i == '' for i in ans):
                        return test_seq * (len(seq2) // len(test_seq))
                return test_seq
        return ''
 
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if len(str1) >= len(str2):
            return self.dividingStrings(str1, str2)
        return self.dividingStrings(str2, str1)


str1 = "ABAB"
str2 = "ABABABAB"
sol = Solution()
sol.gcdOfStrings(str1, str2)
