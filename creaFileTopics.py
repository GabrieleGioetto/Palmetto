import sys

progetto = sys.argv[1]

fileTopic = open("./topics.txt", "r")

i = 1
for line in fileTopic:
    words = line.split(" ")[:10]
    f = open(f"./fileTopics{progetto}/topic{i}.txt", "w")
    f.write(" ".join(words))
    f.close()
    i += 1
