from csv import reader
import time
import tracemalloc

FIND_SENTENCE = "find_words.txt"
FRENCH_DICTIONARY = "french_dictionary.csv"
T8 = "t8.shakespeare.txt"

def fnsToDict(file:str) -> dict:
    dictionary = dict()
    with open(file, "r") as csvFile:
        csvData = reader(csvFile)
        for row in csvData:
           # print(row)
            dictionary[row[0]] = row[1]
    return dictionary

def readFindSentence(file:str) -> list:
    findWordsList = list()
    with open(file, 'r') as findWordsFile:
        lines = findWordsFile.readlines()
        for line in lines:
            findWordsList.append(line.strip("\n"))
    return findWordsList

def replaceSentence(findWords:list, frenchDictionary:dict):
    with open(T8, 'r') as t8:
        fileData = t8.read()
    for a in findWords:
        fileData = fileData.replace(a, frenchDictionary[a])
    with open(T8, 'w') as t8:
        t8.write(fileData)

def main():
    replaceSentence(readFindSentence(FIND_SENTENCE), fnsToDict(FRENCH_DICTIONARY))

if __name__ == "__main__":
    try:
        start_time = time.time()
        tracemalloc.start()
        main()
        print("--- %s seconds ---" % (time.time() - start_time))
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        time1 = (time.time() - start_time)
        time2 = round(time1,2)
        memory = [f"Current memory usage is {current / 10**6}MB;"]
        lines = ["Time to process: %s seconds\n" % time2]
        with open('performance.txt', 'w') as f:
            f.writelines('\n'.join(lines))
            f.writelines('\n'.join(memory))
    except Exception as err:
        print(err)