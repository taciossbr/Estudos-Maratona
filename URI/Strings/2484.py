s = []
while True:
    try:
        word = input()
        tmp = []
        for i in range(len(word)):
            tmp.append(
                " " * i + " ".join([x for x in word][:len(word) - i]) + "\n")
        s.append("".join(tmp))
    except EOFError:
        # print(s)
        print("\n".join(s))
        break
