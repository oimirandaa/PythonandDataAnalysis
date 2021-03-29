import os

#This program renames all the files in the path variable. In this case, it renames the files as img.
def main():
    i = 1
    path = ""
    for filename in os.listdir(path):
        my_dest = "img" + str(i) + ".jpg"
        
        my_source = path + filename
        
        my_dest = path + my_dest

        os.rename(my_source, my_dest)
        
        i += 1


if __name__ == '__main__':
    main() 
    
