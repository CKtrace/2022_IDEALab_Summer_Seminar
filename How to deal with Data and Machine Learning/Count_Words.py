import sys
from collections import Counter

try:
    num_words = int(sys.argv[1]) #sys.argv[0] -> Output = Scipt Name ex) ".\Sample_Data.txt" 
except:
    print("Usage: Count_Words.py num_words")
    sys.exit(0)

counter = Counter(word.lower() 
                for line in sys.stdin 
                for word in line.strip().split() 
                if word)

for word, cnt in counter.most_common(num_words):
    sys.stdout.write(str(cnt))
    sys.stdout.write("\t")
    sys.stdout.write(word)
    sys.stdout.write("\n")



    