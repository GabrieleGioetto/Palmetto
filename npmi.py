import subprocess
import sys


# java -jar palmetto-0.1.0-jar-with-dependencies.jar <some-path>/wikipedia_bd <coherence> <topics-file>


# result = subprocess.getoutput(['java', '-jar', 'palmetto-0.1.0-jar-with-dependencies.jar','./wikipedia_bd', 'NPMI', 'topicsprova.txt'])
# result = subprocess.getoutput(['java -jar palmetto-0.1.0-jar-with-dependencies.jar ./wikipedia_bd NPMI topicsprova.txt'])

# print("fine")
# print(result.split(" "))
# print(result.split("\t"))

# print(result.split("\t")[1])

progetto = sys.argv[1]

fileOutput = open(f"./outputPalmetto{progetto}.txt", "a")



i = 1
sommaNPMI = 0.0
for i in range(1,51):
    result = subprocess.getoutput([f'java -jar palmetto-0.1.0-jar-with-dependencies.jar ./wikipedia_bd NPMI ./fileTopics{progetto}/topic{i}.txt'])
    npmi = float(result.split("\t")[1])
    print(npmi)
    fileOutput.write(str(npmi)+"\n")
    sommaNPMI += npmi

print(f"Average NPMI {progetto}: {sommaNPMI/50.0}")
fileOutput.write(f"Average NPMI {progetto}: {sommaNPMI/50.0}")
