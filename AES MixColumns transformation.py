import numpy as np

# AES Fixed Matrix for MixColumns
FIXED_MATRIX = np.array([
    [0x02, 0x03, 0x01, 0x01],
    [0x01, 0x02, 0x03, 0x01],
    [0x01, 0x01, 0x02, 0x03],
    [0x03, 0x01, 0x01, 0x02]
], dtype=int)

# Galois Field Multiplication
def galois_multiplication(a, b):
    p = 0
    for _ in range(8):
        if b & 1:
            p ^= a
        hi_bit_set = a & 0x80
        a <<= 1
        if hi_bit_set:
            a ^= 0x1b
        b >>= 1
    return p % 256

# MixColumns Function
def mix_columns(state):
    result = np.zeros((4, 4), dtype=int)
    for col in range(4):
        column = state[:, col]
        for row in range(4):
            result[row, col] = galois_multiplication(FIXED_MATRIX[row, 0], column[0]) ^ \
                              galois_multiplication(FIXED_MATRIX[row, 1], column[1]) ^ \
                              galois_multiplication(FIXED_MATRIX[row, 2], column[2]) ^ \
                              galois_multiplication(FIXED_MATRIX[row, 3], column[3])
    return result

# Example State Matrix
state = np.array([
    [0xD5, 0x79, 0x6E, 0x61],
    [0x65, 0x61, 0x6D, 0x65],
    [0x61, 0x77, 0x61, 0x69],
    [0x00, 0x00, 0x00, 0x73]
], dtype=int)

print("Original State:")
print(state)

mixed_state = mix_columns(state)
print("\nAfter MixColumns:")
print(mixed_state)
