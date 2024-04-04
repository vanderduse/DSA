# def rearrange_bits(N):
#   """
#   Rearranges bits in N to make set bits consecutive and minimizes the value.

#   Args:
#       N: An integer representing the number.

#   Returns:
#       An integer representing the minimum value after rearranging bits.
#   """
#   # Isolate set bits using bit manipulation
#   set_bits = N
#   while set_bits:
#     set_bits &= (set_bits - 1)

#   # Count set bits
#   count = 0
#   while set_bits:
#     count += 1
#     set_bits >>= 1

#   # Handle zero set bits case (no need to shift)
#   return (1 << (max(count - 1, 0))) - 1  # Use max to avoid negative shift

# # Example usage
# N = 10  # Binary: 1010
# min_value = rearrange_bits(N)
# print("Original:", N, "Binary:", bin(N)[2:])
# print("Minimum after rearranging:", min_value, "Binary:", bin(min_value)[2:])
def rearrange_bits(N):
    """
    Rearranges bits in N to make set bits consecutive and minimizes the value.

    Args:
        N: An integer representing the number.

    Returns:
        An integer representing the minimum value after rearranging bits.
    """
    # Count the number of set bits in N
    count = bin(N).count('1')

    # Create a new binary number with the same number of set bits but with all set bits placed at the least significant positions
    min_value = (1 << count) - 1

    return min_value

# Example usage
N = 10  # Binary: 1010
min_value = rearrange_bits(N)
print("Original:", N, "Binary:", bin(N)[2:])
print("Minimum after rearranging:", min_value, "Binary:", bin(min_value)[2:])
