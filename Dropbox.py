import csv ,shutil,os
path= "C:/Users/sutichai/Dropbox/IEO"

exampleFile = open('IEO2018list.csv')
exampleReader = csv.reader(exampleFile)
os.chdir(path)
for row in exampleReader:
    if exampleReader.line_num == 1 :
        continue
    print(str(row[1])+'_'+str(row[2][0]))
    os.makedirs(str(row[1])+'_'+str(row[2][0]))



