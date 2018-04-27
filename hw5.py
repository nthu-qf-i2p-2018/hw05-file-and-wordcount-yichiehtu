import csv
import json
import pickle
import string

def main(filename):
    txtfile = open(filename)
    lines = txtfile.readlines()

    all_words = []

    for line in lines:
        words = line.split()
        
        for word in words:
            word = word.strip(string.punctuation)
            
            if word !="":
                all_words.append(word)
                
    from collections import Counter
    counter = Counter(all_words)
    counter = Counter()
    counter.update(all_words)
    
    with open('wordcount.csv', 'w') as csv_file:
        writer = csv.writer(csv_film)
        writer.writerow(['word', 'count'])
        writer.writerows(counter.items())
    
    with open('wordcount.json', 'w') as json_file:
        json.dump(counter, json_film)
                
    pickle.dump(counter, open("wordcount.pkl", 'wb'))

if __name__ == '__main__':

    main("i_have_a_dream.txt")
