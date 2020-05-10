#["www.zframez.com", "www.wikipedia.org", "www.asp.net", "www.abcd.in"]
#Write a python program to print website suffixes (com , org , net ,in) from this list

urlList = ["www.zframez.com", "www.wikipedia.org", "www.asp.net", "www.abcd.in"]

suffixes = []

for url in urlList:
    currentSuffix = ""
    for symbol in reversed(url):
        if symbol == ".":
            suffixes.append(currentSuffix)
            currentSuffix = ""
            break
        else:
            currentSuffix = symbol+currentSuffix


print(",".join(suffixes))
