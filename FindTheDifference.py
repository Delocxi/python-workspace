t = "qazxsw"
s = "xawqs"
from collections import deque
for word in deque(t):
    if word not in deque(s):
        print(word)

def findTheDifference(s: str, t: str) -> str:
    cnt = [0] * 26
    for c in s:
        cnt[ord(c) - ord('a')] -= 1

    for c in t:
        if cnt[ord(c) - ord('a')] == 0: return c
        cnt[ord(c) - ord('a')] += 1

def findTheDifference(self, s: str, t: str) -> str:
    from collections import Counter
    cnt_s = Counter(s)
    cnt_t = Counter(t)
    return (cnt_t - cnt_s).most_common(1)[0][0]