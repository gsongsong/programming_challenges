def print_formatted(number):
    # your code goes here
    max_bin_len = len(bin(number)[2:])
    for n in range(1, number + 1):
        print(str(n).rjust(max_bin_len),
              oct(n)[2:].rjust(max_bin_len),
              hex(n)[2:].upper().rjust(max_bin_len),
              bin(n)[2:].rjust(max_bin_len))
