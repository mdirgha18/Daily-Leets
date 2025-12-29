class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        adj = defaultdict(list)
        for el in allowed:
            key = el[:2]
            val = el[-1]
            adj[key].append(val)

        def backtrack(base, next_level="", idx=0):
            # if we've built the complete next level
            if idx == len(base) - 1:
                if len(next_level) == 1:
                    return True
                return backtrack(next_level)

            # current adjacent pair we are examining
            key = base[idx:idx+2]
            # try each allowed character for this position
            for char in adj[key]:
                if backtrack(base, next_level + char, idx + 1):
                    return True
            return False
        return backtrack(bottom)