def file_read(fname):
        txt = open(fname)
        print(txt.read())

fname=input("Enter the file name you want to open\n")
file_read(fname)

