class Solution:
    def findSubstring(self, s, words):
        if not s or not words: return []
        word_len, total_len = len(words[0]), len(words) * len(words[0])
        count, res = Counter(words), []
        for i in range(word_len):
            l, r, curr = i, i, Counter()
            while r + word_len <= len(s):
                w = s[r:r + word_len]
                r += word_len
                if w in count:
                    curr[w] += 1
                    while curr[w] > count[w]:
                        curr[s[l:l + word_len]] -= 1
                        l += word_len
                    if r - l == total_len:
                        res.append(l)
                else:
                    curr.clear()
                    l = r
        return res

