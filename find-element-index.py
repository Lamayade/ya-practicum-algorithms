length = int(input())

unique_dict = dict.fromkeys(input().split(' '))

appendix = length - len(unique_dict)

result = ' '.join(unique_dict) + ' _' * appendix

print(result)
