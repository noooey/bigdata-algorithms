"""
국민대학교 소프트웨어학부
23-1학기 빅데이터최신기술 실습 코드
"""

import random

class Reservoir:
    def __init__(self, k):
        self.k = k
        self.sampled = []
        self.size = 0

    def add(self, x):
        self.size += 1

        if self.size <= self.k:
            self.sampled.append(x)
        else:
            i = random.randrange(0, self.size)
            if i < self.k:
                self.sampled[i] = x

r = Reservoir(100)

for i in range(10000):
    r.add(i)
    print(i, r.sampled)
