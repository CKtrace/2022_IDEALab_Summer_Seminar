import sys, re

regex = sys.argv[1] #sys.argv[0] -> Output = Scipt Name ex) ".\Sample_Data.txt" 

for line in sys.stdin:
    if re.search(regex, line):
        sys.stdout.write(line)
    
print(regex)