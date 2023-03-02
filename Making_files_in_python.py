#  Using this program we can make a file using Python and perform File input output operations on it....
f=open('My_File.txt','w')
f.write("My name is Yashveer Singh Makhloga. I am the real owner of this File")
f.close()   # After opening a file we should not forget to close it using f.close()


f=open('My_File.txt','r')   #Using this we can open a file and read its data
data=f.read()
print(data)
f.close()
