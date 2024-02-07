class Solution:
    def frequencySort(self, s: str) -> str:
        ans=""
        freq=collections.Counter(s).most_common()
        for letter,count in freq:
            # print(letter,count)
            for i in range(count):
                ans = ans + letter
        return ans