import math
import mmh3
import random

class BloomFilter:

    def __init__(self, m, fp): # m = |S|, fp = desired false positive rate
        self.m = m
        self.fp = fp
        self.n = int(- (m * math.log(fp)) / (math.log(2) ** 2))
        self.k = int((self.n / m) * math.log(2))
        self.B = [False] * self.n
        self.seeds = [random.randint(1, 100000) for _ in range(self.k)]

    def add(self, x):
        for i in range(self.k):
            x = str(x).encode()
            idx = mmh3.hash(x, self.seeds[i]) % self.n
            self.B[idx] = True

    def check(self, x):
        for i in range(self.k):
            x = str(x).encode()
            idx = mmh3.hash(x, self.seeds[i]) % self.n
            if not self.B[idx]:
                return False

        return True


# Bloom Filter의 false positive 비율을 확인하는 함수
def test_false_positive_rate(m, fp):
    bloom_filter = BloomFilter(m, fp)

    # 실제 요소 집합 생성
    elements = set(range(m))

    # Bloom Filter에 요소 추가
    for element in elements:
        bloom_filter.add(element)

    # false positive 테스트
    false_positives = 0
    test_size = 1000  # 테스트할 요소 수

    for i in range(test_size):
        # 알려지지 않은 요소를 무작위로 선택
        element = random.randint(m + 1, 2 * m)

        # Bloom Filter에 존재하지 않는데도 존재로 판단되면 false positive로 처리
        if bloom_filter.check(element) and element not in elements:
            false_positives += 1

    # false positive 비율 계산
    false_positive_rate = false_positives / test_size
    print(f"False Positive Rate: {false_positive_rate}")


# m과 fp 값을 적절히 설정하여 테스트
m = 10000
fp = 0.05

test_false_positive_rate(m, fp)
