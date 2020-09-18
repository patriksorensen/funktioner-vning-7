
def HittaLangstaOrdet(arrayOfStrings):
    longestSoFar = arrayOfStrings[0]
    for one in arrayOfStrings:
        if len(one) > len(longestSoFar):
            longestSoFar = one
    return longestSoFar

listan = ["Djurgården", "AIK", "Hammarby", "Brommapojkarna"]
longestName = HittaLangstaOrdet(listan)
print(longestName)


spelare = {}
while true:
    print("1. Lista spelare")
    print("2.")