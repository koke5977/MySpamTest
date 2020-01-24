import os, glob, pickle
import tfidf

y = []
x = []

def read_files(path, label):
    print("read_files=", path)
    files = glob.glob(path + "/*.txt")
    for f in files:
        if os.path.basename(f) == 'LICENSE.txt': continue
        tfidf.add_file(f)
        y.append(label)

read_files('./ok', 0)
read_files('./spam', 1)


x = tfidf.calc_files()

pickle.dump([y, x], open('./spam.pickle', 'wb'))
tfidf.save_dic('./spam-tdidf.dic')
print('ok')

print(len(x))
print(len(y))
