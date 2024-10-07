def test(s: str, k: int) -> int:
    max_count = 0
    s = [alpha in 'aeiou' for alpha in s]
    count = sum(s[:k])

    for i in range(k, len(s)):
        count += s[i] - s[i - k]
        if count > max_count:
            max_count = count

    return max_count

test("ibpbhixfiouhdljnjfflpapptrxgcomvnb", 33)
#test('abciiidef', 3)
