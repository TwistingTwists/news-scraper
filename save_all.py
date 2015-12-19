# from hindu_datewise import fwrite
import datetime
import newspaper
import os
import sys
today = datetime.date.today().isoformat()

u='2015-11-27'

def makefolder(filename):
    folder = filename[0:10]
    if not os.path.exists(folder):
            os.makedirs(folder)
    return folder


def fwrite(s, filename='1.txt'):
    f = open(filename,'w+')
    f.write(s.encode("utf-8"))
    f.close()


def save_all(filename='please-provide-datetime-file.txt'):
    if os.path.exists(filename):
        f = open(filename,'r')
    else:
        print ("'please-provide-datetime-file.txt'")


    read_all = f.readlines()
    f.close()
    folder = makefolder(filename)
    i=0
    for r in read_all:
        i = i+1
        B = newspaper.Article(r[:-1])
        print i," .txt"
#        B = newspaper.Article(r)
        B.download()
        B.parse()
        # print "\n ----------------------------------------------------------Text---------------------------------",B.text
        # filename = "./"+u+"/"+B.title+".txt"
        fi = "./"+folder+"/"+str(i)+".txt"
        fwrite(B.text,fi)

    return

if __name__ == '__main__':
    command = sys.argv[1:]
    text_file= command[0]
    if not os.path.exists(text_file):
        print("FIle does not exist. Please check filename.")
    else:
        save_all(text_file)