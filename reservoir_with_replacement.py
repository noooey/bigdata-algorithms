"""
국민대학교 소프트웨어학부
23-1학기 빅데이터최신기술 실습 코드
"""

import random
import matplotlib.pyplot as plt

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
                j = random.randrange(0, self.k)
                self.sampled[j] = x

# 시행 횟수
num_iterations = 10000

# 각 숫자가 추출된 횟수를 저장하는 리스트
count = [0] * 1000

# 시행 반복
for _ in range(num_iterations):
    reservoir = Reservoir(100)

    # 0부터 999까지의 숫자가 입력되는 스트림
    for i in range(1000):
        reservoir.add(i)

    # 추출된 값들의 분포를 count에 저장
    for value in reservoir.sampled:
        count[value] += 1

# 분포 시각화
plt.bar(range(1000), count)
plt.xlabel('Number')
plt.ylabel('Count')
plt.title('Distribution of sampled numbers')
plt.show()
