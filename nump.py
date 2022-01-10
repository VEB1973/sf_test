
import numpy as np 
import time as tm

def random_predict(cnt:int=1) -> int:
    print(np.random.randint(1,101))


#if __name__== "__main__":
loc_start = tm.time()
for i in range(1,11):
    random_predict(i)
loc_finish = tm.time()
print(loc_finish-loc_start)    
