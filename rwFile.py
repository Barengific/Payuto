# -*- coding: utf-8 -*-
"""

@author: barengific
"""

file = open('words.txt')

outp = "resPass.txt"
outf = "resFail.txt"

iop= open(outp,'w')
iof = open(outf, 'w')

count = 0

for line in file:
    lineS = line.split()
    if lineS[2] == 'P':
        #print(line)
        iop.write(line)
    else:
        iof.write(line)
        
    #print(str(count) + line)
    #count = count + 1
    

print(file.read())
file.close()
iop.close()
iof.close()