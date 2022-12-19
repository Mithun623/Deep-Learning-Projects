import os
path=path=r"C:\Users\admin\Desktop\Fruits\My Data\10"
files=os.listdir(path)
for index,file in enumerate(files):
    os.rename(os.path.join(path,file),os.path.join(path,''.join([str(index),'.jpg'])))
