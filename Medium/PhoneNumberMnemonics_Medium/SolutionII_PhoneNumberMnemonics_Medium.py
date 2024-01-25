mapping = ['0', '1', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']


# Algorithmic Beauty Bless You - O(n*4^n) time | O(n*4^n) space
def phoneNumberMnemonics(phoneNumber):
    phoneNumber, mnemonics = list(map(int, phoneNumber)), [[]]
    for digit in phoneNumber:
        new_mnemonics = []
        for letter in mapping[digit]:
            new_mnemonics.extend(_ + [letter] for _ in mnemonics)
        mnemonics = new_mnemonics
    for i in range(len(mnemonics)):
        mnemonics[i] = ''.join(mnemonics[i])
    return mnemonics
