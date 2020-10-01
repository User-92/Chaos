from cryptography.fernet import Fernet
f = Fernet(open("dum.txt", "r").readlines()[2].encode())
sentence = "".join(" ".join(" ".join([f.decrypt(open("dum.txt", "r").readlines()[0].encode()).decode(), ]).split(" ")[::-1]).split("\n"))
word = f.decrypt(open("dum.txt", "r").readlines()[1].encode()).decode()
fword = ""
for letter in word:
    if (word.index(letter) + 1) / 4 == 1 or (word.index(letter) + 1) / 8 == 1 or (word.index(letter) + 1) / 12 == 1 or (word.index(letter) + 1) / 16 == 1:
        fword += letter
print(sentence[:sentence.index("*")] + fword + sentence[sentence.index("*")+1:], end="", sep="")