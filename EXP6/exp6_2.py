def file_read(fname):
        with open(fname) as f:    
                content_list = f.readlines()
                print(content_list)

f = input("Enter the file name in double quotes you want to open ")

file_read(f)
