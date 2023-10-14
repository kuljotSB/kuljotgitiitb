import numpy as np
import pandas as pd
my_list=[1,2,3,4]
print(my_list)
loss_functions=['mean absolute error', 'mean squared error', 'huber loss', 'log loss', 'hinge loss']
print(len(loss_functions))
print(loss_functions[0])
print(loss_functions[1:4])
loss_functions = loss_functions + ['hello']
print(loss_functions)
print(min(loss_functions))
print(sorted(loss_functions))
loss_functions.append('kuljot')
print(loss_functions)
loss_functions.sort(reverse=True)
print(loss_functions)
prime_array=np.array([1,2,3,4])
print(prime_array)
alma_array = np.array([[1,2,3],[4,5,6]])
print(alma_array)
print(alma_array.shape)
array_of_integers=np.array([0,1,2,3,4,5,6,7,8,])
print('size is:' , array_of_integers.size)
list_of_lists = [['Amar',10], ['Akbar', 15], ['Anthony', 14]]
df=pd.DataFrame(list_of_lists, columns=['Name','Age'])
print(df)
employee_dict={'Employee Name':['Rajeev', 'Sumit', 'Aviral'], 'Income':[20,40,50]}
employee_df=pd.DataFrame(employee_dict)
print(employee_df)
employee_no = [['kuljot',20], ['Amar', 40], ['Aadit', 50]]
employee_pdf=pd.DataFrame(employee_no, columns=['name', 'salary'])
print(employee_pdf)
employee_practice={'Employee Name':['Kuljot', 'Aadit'], 'Income':[20,40]}
employee_practice_pd=pd.DataFrame(employee_practice)
print(employee_practice_pd)
some_2D_array=np.random.randint(4,5,(3,4))
first_dataframe=pd.DataFrame(some_2D_array, columns=['Akshay','Devashish', 'Divy', 'Monika'], index=['First','Second','Third' ])
print(first_dataframe)
string1='abc'
string2='def'
print(string1+string2)
print(string1+str(4)+string2)
algorithm='Neural Networks'
print(algorithm)
print(len(algorithm))
print(algorithm.upper)
print(algorithm.count('Ne'))
print(algorithm.count('e'))
print(algorithm.count(''))
print(algorithm.find('e'))
print(algorithm.count('Neural'))
algorithm.replace(' ', '-')


 


                
       