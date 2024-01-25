# Algorithmic Beauty Bless You - O(n) time | O(n) space
def caesarCipherEncryptor(string, key):
    v_min = ord('a')
    size = ord('z') - v_min + 1
    return ''.join(chr((ord(_) - v_min + key) % size + v_min) for _ in string)
