
def mergefile():
    file1 = open('C:\\mergefile\\textch.txt','r')
    file2 = open('C:\\mergefile\\texten.txt','r')
    file3 = open('C:\\mergefile\\textall.txt','w')
    n = 1
    while line1 = file1.readline() and line2 = file2.readline():
        file3.writeline(line1)
        if n%3 == 0:
            file3.write(line2)
        n += 1
    file1.close()
    file2.close()
    file3.close()

if __name__ == '__main__':
    mergefile()