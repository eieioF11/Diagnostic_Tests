import os
import os
import glob
import csv
import pathlib
cwd = os.getcwd()
print(cwd)
fpath="../data/"
p = pathlib.Path('../data')
print(p)
fname=[]
for f in glob.glob(fpath+'*.csv'):
    fname.append(int(os.path.splitext(os.path.basename(f))[0]))
print(fname)
n=0
if len(fname):
    n=max(fname)
with open(fpath+str(n)+'.csv', 'w') as f:
    pass

with open(fpath+str(n)+'.csv', 'r') as f:
    reader = csv.reader(f)
    crow=[row for row in reader]
    tr=[]
    for vector in crow:
        tr.append (vector[0])
    content = list(map(int,tr))
print(content,len(content))
