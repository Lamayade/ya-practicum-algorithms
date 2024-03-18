def is_correct_bracket_seq(brackets: str) -> bool:
    if len(brackets) % 2 != 0:
        return False
    b = brackets
    for _ in range(len(brackets)//2 + 1):
        b_before = b
        b = b.replace('()', '').replace('[]', '').replace(r'{}', '')
        if len(b) == 0:
            return True
        if b == b_before:
            return False
    return False


print(is_correct_bracket_seq(input()))
