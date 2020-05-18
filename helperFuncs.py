def getMaxDicKeyLen(dic):
    maxLen = 0
    for k in dic.keys():
        maxLen = max(len(k), maxLen)
    return maxLen
