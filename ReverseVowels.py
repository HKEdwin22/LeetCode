class Solution:
    def reverseVowels(self, seq: str) -> str:
        seq = list(seq)
        target = []
        ans = []
        for c in seq:
            if c in 'aeiouAEIOU':
                target.append(c)
                ans.append('_')
            else:
                ans.append(c)
        for i in range(len(ans)):
            if ans[i] == '_':
                ans[i] = target.pop()
        return ''.join(ans)

reverseVowels('leetcode')
