import pandas as pd 
data = {
    "model":['CHALLENGER SRT® HELLCAT REDEYE','GT Fastback','GR Supra GT4 EVO'],
    "Company":['Dogge','Ford','toyota'],
    "price":["$10k","$20k","$30k"]
}
cars_data = pd.DataFrame(data)
print(cars_data)
#Locate Row
print(cars_data.loc[1])
#use as a list of indices
print("*************************************************")
print(cars_data.loc[[1,2]])
#change index names
cars_data2 = pd.DataFrame(data,index=['car1','car2','car3'])#index name changed!!
print(cars_data2)
print(cars_data2.loc['car2'])
#read from csv file!!
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
read_csv=pd.read_csv('Day 1/dataframe/readme.csv')
print(read_csv)