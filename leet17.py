digits = "2345"
if not digits:
    result = []
digit2chars = {
    '2': 'abc',
    '3': 'def',
    '4': 'ghi',
    '5': 'jkl',
    '6': 'mno',
    '7': 'pqrs',
    '8': 'tuv',
    '9': 'wxyz'
}

res = [i for i in digit2chars[digits[0]]]
# print(res)
for i in digits[1:]:
    res = [m + n for m in res for n in digit2chars[i]]

print(res)