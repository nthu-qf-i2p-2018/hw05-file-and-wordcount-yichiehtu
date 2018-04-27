from collections import Counter
import string
import csv
import pickle
import json

def main(filename):
    txtfile = open(filename)
    lines = txtfile.readlines()

    all_words = []

    for line in lines:
        words = line.split()
        
        for word in words:
            word = word.strip().strip(string.punctuation)
            
            if word:
                word is not None
                all_words.append(word)
    counter=Counter(all_words)
    counter=counter.most_common()
    
    with open("wordcount.csv", "w", newline="") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['word', 'count'])
        for word, count in counter:
            writer.writerow([word, count])
    f=open("wordcount.json", "w")
    json.dump(counter, f)
    json.dump(counter, open("wordcount.json", "w"))
    pickle.dump(counter, open("wordcount.pkl", "wb"))
                
    pickle.dump(counter, open("wordcount.pkl", 'wb'))

if __name__ == '__main__':

    main("i_have_a_dream.txt")
