import random
import numpy as np
import matplotlib.pyplot as plt

class Block:
    def __init__(self, size, t_start, t_end, sum_val):
        self.size = size
        self.t_start = t_start
        self.t_end = t_end
        self.sum_val = sum_val

    def __repr__(self):
        return f"{self.size, self.t_start, self.t_end, self.sum_val}"

class DGIM:
    def __init__(self):
        self.ts = 0
        self.dgim = [[]]

    def add(self, num):
        if num == 0:
            pass
        else:  # num > 0
            self.dgim[0].append(Block(1, self.ts, self.ts, num))

            bi = 0
            while len(self.dgim[bi]) > 2:
                b1 = self.dgim[bi].pop(0)
                b2 = self.dgim[bi].pop(0)
                new_block_size = b1.size + b2.size
                new_block_sum = b1.sum_val + b2.sum_val
                new_block = Block(new_block_size, b1.t_start, b2.t_end, new_block_sum)
                if len(self.dgim) < bi + 2:
                    self.dgim.append([])

                self.dgim[bi + 1].append(new_block)

                bi += 1

            self.adjust_blocks()

        self.ts += 1

    def adjust_blocks(self):
        bi = 0
        while bi < len(self.dgim):
            if len(self.dgim[bi]) > 2:
                b1 = self.dgim[bi].pop(0)
                b2 = self.dgim[bi].pop(0)
                b3 = self.dgim[bi].pop(0)

                new_block_size = b2.size + b3.size
                new_block_sum = b2.sum_val + b3.sum_val
                new_block = Block(new_block_size, b2.t_start, b3.t_end, new_block_sum)
                self.dgim[bi].insert(0, new_block)
                self.dgim[bi + 1].append(b1)

                bi += 1
            else:
                break

    def count_bits(self, k):
        target_ts = self.ts - k
        cnt = 0

        for blocks in self.dgim:
            for b in reversed(blocks):
                if target_ts <= b.t_start:
                    cnt += b.size
                elif target_ts <= b.t_end:
                    sum_val = b.sum_val
                    if sum_val > 2 ** b.size:
                        sum_val = 2 ** b.size
                    cnt += int((sum_val * (b.t_end - target_ts + 1)) / (b.t_end - b.t_start + 1))
                else:
                    break
            else:
                continue

            break

        return cnt

# Generate random integer stream
stream = [random.randint(0, 15) for _ in range(10000)]

# Initialize DGIM
dgim = DGIM()

# Calculate actual sums for different values of k
k_values = list(range(1, 2001))
actual_sums = []
for k in k_values:
    actual_sum = sum(stream[-k:])
    actual_sums.append(actual_sum)
    dgim.add(stream[-k])

# Calculate DGIM sums for different values of k
dgim_sums = [dgim.count_bits(k) for k in k_values]

# Plotting
plt.plot(k_values, actual_sums, label='Actual Sum')
plt.plot(k_values, dgim_sums, label='DGIM Sum')
plt.xlabel('k')
plt.ylabel('Sum')
plt.legend()
plt.show()
