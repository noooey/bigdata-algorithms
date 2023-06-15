"""
국민대학교 소프트웨어학부
23-1학기 빅데이터최신기술 실습 코드
"""

class Block:
    def __init__(self, size, t_start, t_end):
        self.size = size
        self.t_start = t_start
        self.t_end = t_end

    def __repr__(self):
        return f"{self.size, self.t_start, self.t_end}"

class DGIM:
    def __init__(self):
        self.ts = 0
        self.dgim = [[]]

    # b = 0 or 1
    def add(self, b):
        if b == 0:
            pass
        else: # b == 1
            self.dgim[0].append(Block(1, self.ts, self.ts))

            bi = 0
            while len(self.dgim[bi]) > 2:
                b1 = self.dgim[bi].pop(0)
                b2 = self.dgim[bi].pop(0)
                new_block = Block(b1.size + b2.size, b1.t_start, b2.t_end)
                if len(self.dgim) < bi + 2:
                    self.dgim.append([])

                self.dgim[bi + 1].append(new_block)

                bi += 1

        self.ts += 1

    def count_bits(self, k):
        target_ts = self.ts - k

        cnt = 0

        for blocks in self.dgim:
            for b in reversed(blocks):
                if target_ts <= b.t_start:
                    cnt += b.size
                elif target_ts <= b.t_end:
                    cnt += b.size * ((b.t_end - target_ts + 1) / (b.t_end - b.t_start + 1))
                else:
                    break
            else:
                continue

            break

        return cnt

dgim = DGIM()
bstream = [1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1]
for ts, b in enumerate(bstream):
    dgim.add(b)
    print(ts, b, dgim.dgim)

for k in range(1, 20):
    print(k, sum(bstream[-k:]), dgim.count_bits(k))
