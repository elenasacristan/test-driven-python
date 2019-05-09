def count_upper_case(message):
    return sum([1 for c in message if c.isupper()])
    
assert count_upper_case("") == 0, "Empty"
assert count_upper_case("A") == 1, "One Capital"
assert count_upper_case("AB") == 2, "One Capital"
assert count_upper_case("a") == 0, "One lower"
assert count_upper_case("£%%^") == 0, "special Char"
assert count_upper_case("£%A%^") == 1, "special Char"


print("All test pass")