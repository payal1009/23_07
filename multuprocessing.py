import multiprocessing
import multiprocessing.process
import requests
import time
def download_file(url,name):
    print(f"download start {name}....")
    r = requests.get(url)
    open(f'{name}.jpg', 'wb').write(r.content)
    print(f"download end {name}...")
if __name__ == '__main__':
    url='https://www.pexels.com/photo/short-fur-white-and-black-cat-sitting-on-window-1540258/'
    x=[]
    start,end=0,0
    for i in range(5):
        start=start+time.time()
        p=multiprocessing.Process(target=download_file,args=[url,i]) #process
        p.start()   
        end=end+time.time()
        x.append(p)# append process in lsit
    print(f"Total time multiprocessing : {end-start}")
    for p in x: #all processess are joined
        p.join() 
    #without multiprocessing
    s,e=0,0
    for i in range(5):
        s=s+time.time()
        download_file(url,i)
        e=e+time.time()
    print(f"Total time without multiprocessing : {e-s}")     
    
    
#we can also use here process pool executor