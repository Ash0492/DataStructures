def missingPanagram(s):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    final=""
    for char in alphabet:
        if char not in s.lower():
            final+=char
        else:
            continue

    if len(final) == 0:
        return -1
    return final







s = "APFGMRZXIFPSXKOQDRRQJBBZ"
print(missingPanagram(s))