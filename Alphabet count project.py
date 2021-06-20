print("To count number of times a particular word starts with particular alphabet")


used_alpha=[]

file_ob=open('filename.txt','r')   #type the file name here and open the file in read mode

file_txt=file_ob.read()
list=file_txt.split(' ')
print(list)

def start(alpha):
    if alpha not in used_alpha:
        count=0
        for j in list:
            if j[0]==alpha:
                count=count+1
        print('count of',alpha,'=' ,count)
        used_alpha.append(alpha)

for i in list:
    start(i[0])


file_ob.close()   
