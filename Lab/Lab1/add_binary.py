def add_binary(bin_num1, bin_num2):
    # Ensure both input strings have the same length by padding with '0's if needed.
    max_len = max(len(bin_num1), len(bin_num2))
    bin_num1 = bin_num1.zfill(max_len)
    bin_num2 = bin_num2.zfill(max_len)
    
    carry = 0  # Initialize the carry to 0.
    result = []  # Initialize an empty list to store the result in reverse order.

    for i in range(max_len - 1, -1, -1):
        bit1 = int(bin_num1[i])
        bit2 = int(bin_num2[i])
        # Calculate the sum of bits and the carry for the next iteration.
        total = bit1 + bit2 + carry
        result.append(str(total % 2))
        carry = total // 2

    if carry:
        result.append(str(carry))

    # Reverse the result list and join it to form the final binary string.
    return ''.join(result[::-1])

# Example usage:
bin_num1 = "1101"
bin_num2 = "1011"
sum_binary = add_binary(bin_num1, bin_num2)
print(sum_binary)  # Output should be "11000"
