# importing the needed libraries
import pandas as pd

# enter the csv file you want to read from
# either "iris.csv" or "letter-recognition.csv"
df=pd.read_csv("letter-recognition.csv")

# list with the data from each column
columns_list=[]

# list with the class from every object of the csv file
class_list=[]

# printing the length of the document file
df_len=len(df)
print("The document file's length is:",df_len,"\n")

# filling the lists depending on which file is entered
if df_len==150:
    # the "iris.csv" is entered
    columns_list.append(df.iloc[:,0])
    columns_list.append(df.iloc[:,1])
    columns_list.append(df.iloc[:,2])
    columns_list.append(df.iloc[:,3])
    class_list=df.iloc[:,4]
else:
    # the "letter-recognition.csv" is entered
    columns_list.append(df.iloc[:,0])
    columns_list.append(df.iloc[:,1])
    columns_list.append(df.iloc[:,2])
    columns_list.append(df.iloc[:,3])
    columns_list.append(df.iloc[:,4])
    columns_list.append(df.iloc[:,5])
    columns_list.append(df.iloc[:,6])
    columns_list.append(df.iloc[:,7])
    columns_list.append(df.iloc[:,8])
    columns_list.append(df.iloc[:,9])
    columns_list.append(df.iloc[:,10])
    columns_list.append(df.iloc[:,11])
    columns_list.append(df.iloc[:,12])
    columns_list.append(df.iloc[:,13])
    columns_list.append(df.iloc[:,14])
    columns_list.append(df.iloc[:,15])
    class_list=df.iloc[:,16]

# a list containing the transformed from normalization
new_columns_list=[]

# for each column in the columns list
for aColumn in columns_list:

    # finding the max and min of each column 
    column_min=min(aColumn)
    column_max=max(aColumn)

    # the new_list contains the transformed version of every object of one column // they
    # are being appended by column later to new_columns_list
    new_list=[]
    # the normalization process (using the min and max found from each column)
    for j in range(0,len(aColumn)):
        # the object we want to normalize
        theX=aColumn[j]
        new_x=(theX-column_min)/(column_max-column_min)
        # rounding the value up to 6 decimal digits
        new_list.append(round(new_x,6))

    # appending the new values of each object from each column to the list containing ALL
    # the columns
    new_columns_list.append(new_list)

# depending the given file, we make a different dictionary
if df_len==150:
    dictionary={'sepall':new_columns_list[0], 'sepalw':new_columns_list[1], 'petall':new_columns_list[2],
                'petalw':new_columns_list[3], 'class':class_list}
else:
    dictionary={'xbox':new_columns_list[0], 'ybox':new_columns_list[1], 'width':new_columns_list[2],
                'high':new_columns_list[3], 'onpix':new_columns_list[4], 'xbar':new_columns_list[5],
                'ybar':new_columns_list[6], 'x2bar':new_columns_list[7], 'y2bar':new_columns_list[8],
                'xybar':new_columns_list[9], 'x2ybar':new_columns_list[10], 'xy2bar':new_columns_list[11],
                'xege':new_columns_list[12], 'xegvy':new_columns_list[13], 'yege':new_columns_list[14],
                'yegvx':new_columns_list[15], 'class':class_list}

# writing out on a csv file, the dictionary we made
new_df=pd.DataFrame(dictionary)
if df_len==150:
    new_df.to_csv('normalized_iris.csv',index=False)
    print("Normalization has ended. There is a new file called: normalized_iris.csv\n")
else: 
    new_df.to_csv('normalized_letter-recognition.csv',index=False)
    print("Normalization has ended. There is a new file called: normalized_letter-recognition.csv\n")

