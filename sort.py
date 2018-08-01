from math import floor #need this for finding the mid point in merge sort
import time
from random import randint

class Student:
    def __init__(self, id_no, first, last, credits, cgpa):
	    self.id_no = id_no
	    self.first = first
	    self.last = last
	    self.cgpa = cgpa
	    self.credits = credits
  
    def get_credits(self):
        return self.credits

    def get_cgpa(self):
        return self.cgpa

    def get_firstname(self):
        return self.first

    def get_lastname(self):
        return self.last

    def get_id_no(self):
        return self.id_no

#end of defining class methods
        
#defining mergesort
        
def mergeSort(students_list, n):
    
    if n>1:
        mid = floor(n/2)
        left = mid
        right = n - mid
        left_list = []
        right_list = []
    
        for i in range(0,mid):
            left_list.append(students_list[i])
        
        for j in range(mid, n):
            right_list.append(students_list[j])
        
        mergeSort(left_list, left)
        mergeSort(right_list, right)
        merge(students_list, left_list, left, right_list, right)
    
def merge(students_list, left_list, left, right_list, right):
    
    i = j = k = 0
    
    while i<left and j<right:
        
        if int(left_list[i].get_credits()) > int(right_list[j].get_credits()):
            
            students_list[k] = left_list[i]
            i+=1
            k+=1
        elif int(left_list[i].get_credits()) == int(right_list[j].get_credits()) and float(left_list[i].get_cgpa()) > float(right_list[j].get_cgpa()):
            students_list[k] = left_list[i]
            i+=1
            k+=1
        else:
            students_list[k] = right_list[j]
            j+=1
            k+=1
    while(i<left):
        students_list[k] = left_list[i]
        i+=1
        k+=1
    while(j<right):
        students_list[k] = right_list[j]
        j+=1
        k+=1
    
    
    
    
#defining insertionsort
        
def insertionSort(students_list, n):
    for j in range(1, n):
        key = students_list[j]
        i = j - 1
        
        while i > -1 and int(students_list[i].get_credits()) < int(key.get_credits()):
            students_list[i + 1] = students_list[i]
            i -= 1
            
        if int(students_list[i].get_credits()) == int(key.get_credits()) and float(students_list[i].get_cgpa()) <= float(key.get_cgpa()):
            students_list[i + 1] = students_list[i]
            i -= 1
        
        students_list[i + 1] = key


#define quicksort function
def quicksort(students_list, low_index, high_index):
    if low_index < high_index:
        pivot = quicksort_partition_r(students_list, low_index, high_index)
        quicksort(students_list, low_index, pivot - 1)
        quicksort(students_list, pivot + 1, high_index)

def swap(students_list, i, j):
    temp = students_list[i]
    students_list[i] = students_list[j]
    students_list[j] = temp

def quicksort_partition_r(students_list, low_index, high_index):
    rand_var = randint(low_index, high_index)
    swap(students_list, rand_var, high_index)
    return quicksort_partition(students_list, low_index, high_index)


def quicksort_partition(students_list, low_index, high_index):
	pivot_element = students_list[high_index]
	i = low_index - 1

	for j in range(low_index, high_index):
		if int(students_list[j].get_credits()) > int(pivot_element.get_credits()):
			i += 1
			swap(students_list, i, j)
		elif int(students_list[j].get_credits()) == int(pivot_element.get_credits()):
			if float(students_list[j].get_cgpa()) > float(pivot_element.get_cgpa()):
				i += 1
				swap(students_list, i, j)

	swap(students_list, (i + 1), high_index)
	return (i + 1)

#defining the heap function

def heapify(students_list, n, i):
    largest = i  
    l = 2 * i + 1     
    r = 2 * i + 2     
 
   
    if l < n:
        if int(students_list[i].get_credits()) > int(students_list[l].get_credits()):
            largest = l
        elif int(students_list[i].get_credits()) == int(students_list[l].get_credits()) and float(students_list[i].get_cgpa()) > float(students_list[l].get_cgpa()):
            largest = 1
 
    if r < n:
        if int(students_list[largest].get_credits()) > int(students_list[r].get_credits()):
            largest = r
        elif int(students_list[largest].get_credits()) == int(students_list[r].get_credits() and float(students_list[largest].get_cgpa()) > float(students_list[r].get_cgpa())):
            largest = r
 
    if largest != i:
        students_list[i],students_list[largest] = students_list[largest],students_list[i]  # swap
 
        heapify(students_list, n, largest)
 
# The main function to sort an array of given size
def heapSort(students_list):
    n = len(students_list)
 
    for i in range(n, -1, -1):
        heapify(students_list, n, i)
 
    for i in range(n-1, 0, -1):
        students_list[i], students_list[0] = students_list[0], students_list[i]   # swap
        heapify(students_list, i, 0)

#define the print list function

def printlist(students_objects):
    for student in students_objects:
        print(student.get_firstname() + " " + student.get_lastname() + " " + student.get_cgpa() + " " + student.get_credits())    

#driver part of the program
path = './data.txt'
students_file = open(path, 'r')
students_data = students_file.readlines()
students_objects = []

for individual_data in students_data:
    temp_data = individual_data.strip('\n').split(' ')
    students_objects.append(Student(temp_data[0], temp_data[1], temp_data[2], temp_data[3], temp_data[4]))

print("Before sorting: ")
printlist(students_objects)

while True:
    try:
        case = int(input("Enter 1 to use Quick Sort, 2 to use Insertion Sort, 3 to use MergeSort and 4 to use HeapSort >> "))
    except ValueError:
        case = -1

    if case == 1:
        start = time.time()
        quicksort(students_objects, 0, len(students_objects) - 1)
        end = time.time()
        print("After quick sorting: ")
        printlist(students_objects)
        print("Total time taken is: " + str(round(end - start, 5)) + " seconds.")
        break
    elif case == 2:
        start = time.time()
        insertionSort(students_objects, len(students_objects))
        end = time.time()
        print("After insertion sorting: ")
        printlist(students_objects)
        print("Total time taken is: " + str(round(end - start, 5)) + " seconds.")
        break
    elif case == 3:
        start = time.time()
        mergeSort(students_objects, len(students_objects))
        end = time.time()
        print("After merge sorting: ")
        printlist(students_objects)
        print("Total time taken is: " + str(round(end - start, 5)) + " seconds.")
        break
    elif case ==4:
        start = time.time()
        heapSort(students_objects)
        end = time.time()
        print("After Heap sorting: ")
        printlist(students_objects)
        print("Total time taken is: " + str(round(end - start, 5)) + " seconds.")
        break        
    else:
        print("Invalid choice!")
        continue

