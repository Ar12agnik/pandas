import pandas as pd
data_frame = pd.read_csv('data.csv')#read csv


#remove Rows containing empty cells
cleaned_data = data_frame.dropna()#creates a new dataframe that has no empty rows!!
#works well when the dataset is large calclations not affected

print(f"Old dataset{data_frame.to_string()}")

print(f"New dataset{cleaned_data.to_string()}")


#if you want to change the original data 
data_frame2 = pd.read_csv('data.csv')
data_frame2.dropna(inplace=True)#modifies the original data
print(f"This original data has changed-\n{data_frame2}")
#if you dont want to delete but you want to fill a certain value to null cells

data_frame.fillna(1111,inplace=True)
print(data_frame.to_string())


# if you want to cange only one collumn's null value 
data_frame_new=pd.read_csv("crs.csv")
data_frame_new['model'].fillna("random_car",inplace=True)
print(data_frame_new)

#fill the empty cells with mean
data_frame=pd.read_csv("data.csv")
mean=data_frame['Calories'].mean()
data_frame['Calories']=data_frame['Calories'].fillna(mean)
print(data_frame)