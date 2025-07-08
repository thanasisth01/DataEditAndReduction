# IB2

def getting_the_data(end_of_list,original_dataset):

    # points_list is a list containing arrays of the every object's characteristics
    points_list=[]

    # class list is a list containing the class of every object in the dataset
    class_list=[]

    for anObject in original_dataset:

        # getting the class of the object
        item_class=anObject[end_of_list]
        class_list.append(item_class)

        # getting the characteristics of the object in an np-array
        if end_of_list==4:
            aPoint=np.array((anObject[0],anObject[1],anObject[2],anObject[3]))
        else:
            aPoint=np.array((anObject[0],anObject[1],anObject[2],
                             anObject[3],anObject[4],anObject[5],
                             anObject[6],anObject[7],anObject[8],
                             anObject[9],anObject[10],anObject[11],
                             anObject[12],anObject[13],anObject[14],
                             anObject[15]))

        points_list.append(aPoint)

    # returning the findings
    return points_list,class_list

def making_the_subset(end_of_list,original_dataset,dataset,subset):

    # getting the points and class list from the function getting_the_data
    points_list,class_list=getting_the_data(end_of_list,original_dataset)

    # printing subset's initial length 
    print("Length of initial subset is:",len(subset),"\n")

    # for every object in the data set we do:
    for dataItem in dataset:

        # making a list of the distances between the dataItem and an object from the subset
        distance_list=[]
        # finding the position of the dataset object we want to define in the original dataset
        index_1=original_dataset.index(dataItem)
        # finding the point of the dataset object in the points_list
        dataPoint=points_list[index_1]

        # for every object in the subset
        for subItem in subset:

            # finding the position of the subset object we want to define in the original dataset
            index_2=original_dataset.index(subItem)
            # finding the point of the subset object in the points_list
            subPoint=points_list[index_2]

            # calculating the distance between the two objects
            distance=np.linalg.norm(dataPoint-subPoint)
            # adding the distance to the distances list
            distance_list.append([distance,index_1,index_2])

        # sorting the distances_list by the E.D. 
        distance_list.sort(key=lambda distance_list:distance_list[0])

        # getting the indexes of the objects who are the nearest (1st object)
        dataIndex=distance_list[0][1]
        subIndex=distance_list[0][2]

        # finding the class of each object given the indexes we just found
        # from the class_list
        sub_class=class_list[subIndex]
        data_class=class_list[dataIndex]

        # if the class of the subset object is different from the object of the dataset
        # we add the object to the subset list
        if sub_class!=data_class:
            subset.append(dataItem)
            print("An item is added! The new added subset class is:",data_class,"\n")

    # printing subset's final length 
    print("Length of final subset is:",len(subset),"\n")
            
    return subset


# importing the needed libraries
import pandas as pd
import random
import numpy as np

# reading data from csv file
# enter "normalized_iris.csv" or "normalized_letter-recognition.csv"
document=pd.read_csv("normalized_letter-recognition.csv")

# changing DataFrame objects to a list
original_dataset=document.values.tolist()

# length of the training set
orig_data_len=len(original_dataset)
print("Length of the original data set is:",orig_data_len,"\n")

# creating the condensed subset and the dataset from which we will remove the objects from
# so we don't alter the original dataset
subset=[]
dataset=[]
dataset=original_dataset.copy()

# picking a random object as the first object to enter in the subset
first_x=random.choice(original_dataset)
print("Picking a random object from the dataset:",first_x,"\n")

# adding the first object to the subset
subset.append(first_x)

# removing the first object from the dataset
dataset.remove(first_x)

# checking the dataset's length
len_dataset=len(dataset)
print("Length of altered dataset is:",len_dataset,"\n")

# different execution depending on the given file
if orig_data_len==150:
    # the file entered is "iris.csv"
    end_of_list=4
    # the final subset
    subset=making_the_subset(end_of_list,original_dataset,dataset,subset)
else:
    # the file entered is "iris.csv"
    end_of_list=16
    # the final subset
    subset=making_the_subset(end_of_list,original_dataset,dataset,subset)

# writing out the data on a cvs file by transforming the list in a DataFrame for pandas library
if orig_data_len==150:
    new_df=pd.DataFrame(subset, columns=['sepall','sepalw','petall','petalw','class'])
    new_df.to_csv('irisIB2.csv',index=False)
    print("IB2 has ended. There is a new file called: irisIB2.csv\n")
else:
    new_df=pd.DataFrame(subset, columns=['xbox','ybox','width','high','onpix','xbar',
                                             'ybar','x2bar','y2bar','xybar','x2ybar','xy2bar',
                                             'xege','xegvy','yege','yegvx','class'])
    new_df.to_csv('letter-recognitionIB2',index=False)
    print("IB2 has ended. There is a new file called: letter-recognitionIB2.csv\n")

# things to do:
#     * εκτέλεση με letter-recognition
#     * να δημιουργήσω τα files irisIB2 και letter-recognitionIB2
