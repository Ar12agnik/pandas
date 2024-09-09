import pandas as pd
names = ["Agnik","Ayanabha","Shivam"]
names_var = pd.Series(names)
print(names_var)
#This is a basic example of a series in pandas
#The above searies can be accessed using 
print(names_var[0])#here 0 stands for the label
#by default the lable is numaric
#we can change it using
name_var2 = pd.Series(names,index=["A","Ay","S"])
print(name_var2['A'])
print(name_var2['Ay'])
print(name_var2['S'])