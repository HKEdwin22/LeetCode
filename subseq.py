def test(s: str, t: str) -> bool:
    s_pos = []
    idx = 0
    for i,c in enumerate(s):
        if c not in t[idx:]:
            return False
        else:
            s_pos.append(t[idx:].index(c) + idx)
            idx = s_pos[-1] + 1
            if i != len(s) - 1 and idx >= len(t):
                return False
    return True
s = 'abc'
t = "ahbgdc"
test(s,t)
