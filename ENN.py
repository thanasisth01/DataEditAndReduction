# Edited Nearest Neighbor ALgorithm

# finding the classes of the k nearest neighbors of an object
def major_class(kNN_list):

    # list with all the class of the k nearest objects of our object
    classes_of_other_items=[]

    # finding the classes of the k nearest objects of our object
    for i in kNN_list:
        my_item=i[1]
        other_item=i[2]
        class_of_other_item=class_list[other_item]
        classes_of_other_items.append(class_of_other_item)

    # major class of the classes of the k nearest objects of our object
    major_class_found=find_common_class(classes_of_other_items)

    return major_class_found


# finding the most common class between a number of classes of a list of objects
def find_common_class(neigh_class):

    # removing from the neigh class the duplicates and saving it to a new list
    rem_dupl_list=list(set(neigh_class))

    # number of original classes appearig in the neigh classes
    rem_length=len(rem_dupl_list)

    # a list to count the appearance of each class found on the neigh class
    counting_list=[]

    # initializing the counting list
    for i in range(0,rem_length):
        counting_list.append([rem_dupl_list[i],0])

    # for each neighbor of our object we add +1 to the class it is from
    for neigh in neigh_class:
        if neigh in rem_dupl_list:
            myIndex=rem_dupl_list.index(neigh)
            counting_list[myIndex][1]=counting_list[myIndex][1]+1

    # sorting descending the counting list and returning the first object (most common class)
    counting_list.sort(key=lambda counting_list:counting_list[1],reverse=True)
    return counting_list[0][0]
        

# importing the needed libraries
import numpy as np
import pandas as pd

# reading data from csv file
# enter "normalized_letter-recognition.csv" or "normalized_iris.csv"
df=pd.read_csv("normalized_letter-recognition.csv")

# changing DataFrame objects to a list
train_set=df.values.tolist()

# length of the training set
length=len(train_set)
print("Length of training set is:",length)

# a list with the classes of every object of the training set
class_list=[]

# points of every object of the training set
points_list=[]

# filling the upper lists with data from the train_set list
if length==150:
    for column in train_set:
        ch1=column[0]
        ch2=column[1]
        ch3=column[2]
        ch4=column[3]
        class_list.append(column[4])

        # setting an np.array to calculate later the Euclidean Distance
        aPoint=np.array((ch1,ch2,ch3,ch4))
        points_list.append(aPoint)
else:
    for anObject in train_set:
        # setting an np.array to calculate later the Euclidean Distance
        aPoint=np.array((anObject[0],anObject[1],anObject[2],
                             anObject[3],anObject[4],anObject[5],
                             anObject[6],anObject[7],anObject[8],
                             anObject[9],anObject[10],anObject[11],
                             anObject[12],anObject[13],anObject[14],
                             anObject[15]))
        class_list.append(anObject[16])

        points_list.append(aPoint)
    
# choose k nearest neighbors to find
k=3

# every k N.N. of each object of the training set
every_k_nn=[]

# objects whose class is not the same with the k nearest neighbors
to_be_excluded=[]

# for every object in the training set find the Euclidean Distance with every other object
for i in range(0,length):

    # list with Euclidean Distances of i object with every other object from the training set
    distances_list=[]

    # setting the first point of the E.D.
    point1=points_list[i]

    # checking the other objects
    for j in range(0,length):

        # so we don't calculate the E.D. between the same object
        if i!=j:

            # setting the second point of the E.D.
            point2=points_list[j]
            # calculating the E.D.
            dist = np.linalg.norm(point1-point2)
            # adding the calculated distance in the distances_list
            distances_list.append([dist,i,j])

    # sorting the distances_list by the E.D. 
    distances_list.sort(key=lambda distances_list:distances_list[0])

    # finding the k nearest neighbors of i object
    k_nn=[]
    for l in range(0,k):
        k_nn.append(distances_list[l])

    # adding the k nearest neighbors of i object to the list of every object
    every_k_nn.append(k_nn)

    # the class of the i object
    it_is=class_list[i]

    # the major class of the k nearest neighbors
    sup_to_be=major_class(k_nn)

    # if the class of i object is not the same of the k nearest objects, it is added to the
    # excluded objects, which will not be inserted into the edited set
    if sup_to_be!=it_is:
        print("It is supposed to be: ",sup_to_be," and is a: ",it_is)
        to_be_excluded.append(i)

# setting the edited set
edited_set=[]

# number of objects that have to be excluded from the edited_set
exc_length=len(to_be_excluded)
print("Number of the objects to be excluded: ",exc_length)

# adding the non-excluded objects in the edited_set
for i in range(0,length):
    if i not in to_be_excluded:
        edited_set.append(train_set[i])

# length of the final edited_set (has to be equals to length-exc_length)
edit_len=len(edited_set)
print("Length of edited set is:",edit_len)
print("\n")

# checking which objects are not appearing in the edited set
for i in range(0,exc_length):
    item=to_be_excluded[i]

    # printing the object
    print("Item:",item,"with these features:",train_set[item])

    # printing the classes of the k nearest neighbors of our object
    print("Item's k nearest neighbors are the class of: ")
    for each_neighbor in every_k_nn[item]:
        neigh_item=each_neighbor[2]
        neigh_class=class_list[neigh_item]
        print("*",neigh_class)
        
    print("\n")

# writing out the data on a cvs file by transforming the list in a DataFrame for pandas library
if length==150:
    new_df=pd.DataFrame(edited_set, columns=['sepall','sepalw','petall','petalw','class'])
    new_df.to_csv('irisENN.csv',index=False)
    print("ENN has ended. There is a new file called: irisENN.csv\n")
else:
    new_df=pd.DataFrame(edited_set, columns=['xbox','ybox','width','high','onpix','xbar',
                                             'ybar','x2bar','y2bar','xybar','x2ybar','xy2bar',
                                             'xege','xegvy','yege','yegvx','class'])
    new_df.to_csv('letter-recognitionENN',index=False)
    print("ENN has ended. There is a new file called: letter-recognitionENN.csv\n")

# it works

# πρέπει να αλλάξει για να μπορώ να κάνω ENN και τις τιμές και του άλλου αρχείου
# δηλαδή πρέπει να δημιουργει αυτόματα chN και να τα κάνει append στην np.array.
# + ότι άλλες αλλαγές χρειάζονται
