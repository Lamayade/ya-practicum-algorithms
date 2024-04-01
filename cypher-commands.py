# Номер успешной посылки 111096851
import string


def decrypt_commands(crypted_str: str, inx: int = 0) -> str:
    result = ''
    multiplier = ''
    while inx < len(crypted_str):
        if crypted_str[inx] in string.digits:
            multiplier += crypted_str[inx]
        elif crypted_str[inx] == '[':
            unencrypted_str, inx = decrypt_commands(crypted_str, inx + 1)
            result += int(multiplier) * unencrypted_str
            multiplier = ''
        elif crypted_str[inx] == ']':
            return result, inx
        else:
            result += crypted_str[inx]
        inx += 1
    return result


if __name__ == '__main__':
    print(decrypt_commands(input()))
