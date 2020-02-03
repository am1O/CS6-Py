fname1=input("Enter the file name you want to open\n")
fname2=input("Enter the file name you want to open\n")
with open(fname1) as fh1, open(fname2) as fh2:
    for line1, line2 in zip(fh1, fh2):
        # line1 from abc.txt, line2 from test.txtg
        print(line1+line2)
