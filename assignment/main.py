import os
from fastapi import FastAPI
from functools import reduce
from itertools import product
import numpy as np
from datetime import datetime
import unittest
import asyncio

# fastAPI happens according to https://fastapi.tiangolo.com/tutorial/
# Run and test the API #apitest
# to test api -> uvicorn main:app --reload --host=0.0.0.0

app = FastAPI()

@app.post("/optimize/efficient")
async  def efficient(lists,m,f):
    #Dynamics Programming by producing partial solution
    result_arrays= reduce(lambda L1,L2 :{
        ((f(l2)+l1)%m) for l1,l2 in product(L1,L2)
    },lists,{0})
    return {"result":max(result_arrays)}

 
@app.post("/optimize/naive")
async def naive(lists,m,f):
    #producing all possible combinations
    result_arrays= map(lambda item:sum(f(i) for i in item)%m, 
     product(*lists)
    )
    return {'result':max(result_arrays)} 

@app.post("/benchmark/naive")
async def ben_naive(replication,num_list,num_elements):
    naive_test=test(replication,num_list,num_elements)
    results=naive_test.naive_random_test()
    return {'avg':test.average(results),'std':test.std(results)}


@app.post("/benchmark/efficient")
async def ben_naive(replication,num_list,num_elements):
    naive_test=test(replication,num_list,num_elements)
    results=naive_test.efficient_random_test()
    return {'avg':test.average(results),'std':test.std(results)}

# a sample function for testing
def square(x):
    return x**2

#testing for benchmarking
class test:
    def __init__(self,replication,num_list,num_elements):

        self.replication=replication
        self.num_list=num_list
        self.num_elements=num_elements

    def random_list_gerarator(self):

        np.random.seed(np.random.randint(0,self.replication))
        #min:0 max:1e9
        # number of elements is between num_elements and num_elements+10 : from the number of elements was not clear
        x=  np.random.randint(0, 1e9, size=(self.num_list, np.random.randint(self.num_elements,self.num_elements+10)))    
        return x

    def naive_random_test(self):
        
        test_results=[]
        for _ in range(self.replication):
            test_results.append(naive(self.random_list_gerarator,5,square))
            return test_results

    def efficient_random_test(self):
        
        test_results=[]
        for _ in range(self.replication):
            test_results.append(efficient(self.random_list_gerarator,5,square))
            return test_results

    def average(x):
        return np.avg(x)

    def std(x):
        return np.std(x)    

#unittesting
class non_random_test(unittest.TestCase):
     
    def test_k_3_naive(self):
        lists=([5, 4], [7, 8, 9], [5, 7, 8, 9, 10])
        m=40 
        start_time = datetime.now()
        naive_results=naive(lists,m,square)
        print ((datetime.now() - start_time), " for naive function") 
        loop=asyncio.get_event_loop()
        naive_results=loop.run_until_complete(naive_results)  
        self.assertEqual(naive_results["result"],37)
        
    def test_k_3_efficient(self):
        lists=([5, 4], [7, 8, 9], [5, 7, 8, 9, 10])
        m=40 
        start_time = datetime.now()
        efficient_results=efficient(lists,m,square)
        print ((datetime.now() - start_time), " for efficient function")   
        loop=asyncio.get_event_loop()
        efficient_results=loop.run_until_complete(efficient_results) 
        self.assertEqual(efficient_results["result"],37)

    def test_k_3_1_naive(self):
        lists=([2, 5, 4], [3, 7, 8, 9], [5, 5 ,7 ,8 ,9 ,10] )
        m=1000
        start_time = datetime.now()
        naive_results=naive(lists,m,square)
        print ((datetime.now() - start_time), " for naive function")          
        loop=asyncio.get_event_loop()
        naive_results=loop.run_until_complete(naive_results)  
        self.assertEqual(naive_results["result"],206)

    def test_k_3_1_efficient(self):
        lists=([2, 5, 4], [3, 7, 8, 9], [5, 5 ,7 ,8 ,9 ,10] )
        m=1000
        start_time = datetime.now()
        efficient_results=efficient(lists,m,square)
        print ((datetime.now() - start_time), " for efficient function") 
        loop=asyncio.get_event_loop()
        efficient_results=loop.run_until_complete(efficient_results)            
        self.assertEqual(efficient_results["result"],206)



    def test_k_7_naive(self):
        lists=([2, 5, 4], [3, 7, 8, 9], [5, 5 ,7 ,8 ,9 ,10],[3,5,6,7],[4,7,8,4,5],[5, 2, 8, 9, 5],[4,7,4,6,8] )
        m=1000
        start_time = datetime.now()
        naive_results=naive(lists,m,square)
        print ((datetime.now() - start_time), " for naive function")   
        loop=asyncio.get_event_loop()
        naive_results=loop.run_until_complete(naive_results)          
        self.assertEqual(naive_results['result'],464)

    def test_k_7_efficient(self):
        lists=([2, 5, 4], [3, 7, 8, 9], [5, 5 ,7 ,8 ,9 ,10],[3,5,6,7],[4,7,8,4,5],[5, 2, 8, 9, 5],[4,7,4,6,8] )
        m=1000
        start_time = datetime.now()
        efficient_results=efficient(lists,m,square)
        print ((datetime.now() - start_time), " for efficient function")  
        loop=asyncio.get_event_loop()
        efficient_results=loop.run_until_complete(efficient_results)           
        self.assertEqual(efficient_results['result'],464) 



    def test_k_12_naive(self):
        lists=([2, 5, 4], [3, 7, 8, 9], [5, 5 ,7 ,8 ,9 ,10],[3,5,6,7],[4,7,8,4,5],[5, 2, 8, 9, 5],[4,7,4,5,8], [4,4,4,6,8],[2,7,4,6,8],[1,7,4,7,8],[4,4,6,11],[9,6,6,11])
        m=100
        start_time = datetime.now()
        naive_results=naive(lists,m,square)
        print ((datetime.now() - start_time), " for naive function") 
        loop=asyncio.get_event_loop()
        naive_results=loop.run_until_complete(naive_results)         
        self.assertEqual(naive_results['result'],99)

    def test_k_12_efficient(self):
        lists=([2, 5, 4], [3, 7, 8, 9], [5, 5 ,7 ,8 ,9 ,10],[3,5,6,7],[4,7,8,4,5],[5, 2, 8, 9, 5],[4,7,4,5,8], [4,4,4,6,8],[2,7,4,6,8],[1,7,4,7,8],[4,4,6,11],[9,6,6,11])
        m=100
        start_time = datetime.now()
        efficient_results=efficient(lists,m,square)
        print ((datetime.now() - start_time), " for efficient function")  
        loop=asyncio.get_event_loop()
        efficient_results=loop.run_until_complete(efficient_results)         
        self.assertEqual(efficient_results['result'],99) 

if __name__=="__main__":
      unittest.main()





