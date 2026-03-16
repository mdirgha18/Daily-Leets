class Fancy:
    def __init__(self):
        self.seq = []
        self.add = 0         # global additive offset
        self.mult = 1        # global multiplicative factor
        self.MOD = 10**9 + 7

    def append(self, val: int) -> None:
        # Neutralize current global state so future transforms apply correctly
        # raw * mult + add = val  →  raw = (val - add) * inv(mult)
        inv_mult = pow(self.mult, self.MOD - 2, self.MOD)
        raw = (val - self.add) * inv_mult % self.MOD
        self.seq.append(raw)
        # NO reset of add/mult — global state stays intact

    def addAll(self, inc: int) -> None:
        self.add += inc

    def multAll(self, m: int) -> None:
        self.add *= m % self.MOD
        self.mult *= m % self.MOD

    def getIndex(self, idx: int) -> int:
        return (self.seq[idx] * self.mult + self.add) % self.MOD if idx <= len(self.seq)-1 else -1