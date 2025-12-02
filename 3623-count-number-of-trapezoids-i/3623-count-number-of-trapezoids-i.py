class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        freq = Counter(p[1] for p in points)
        sum, c2 = 0, 0
        for f in freq.values():
            if f <= 1:
                continue
            c = f * (f-1)//2
            sum += c
            c2 += c*c 
        return (sum*sum-c2)//2 % (10**9+7)