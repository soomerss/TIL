with open("files.txt", "r") as file:
    words = file.readline()
    for word in words.split():
        if "c" in word:
            print(word.replace(",", "").replace(".", ""))
