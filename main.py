from add import Add
from subtract import Subtract

def calc():
    print('Test')
    num1=10
    num2=20

    results_add = Add(num1,num2)
    results_subracts= Subtract(num1,num2)

    print('Sum is', results_add)
    print('Differnce', results_subracts) 
calc()
