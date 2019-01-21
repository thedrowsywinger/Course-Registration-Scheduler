# Divide-and-Conquer-Algorithms
This was an assignment in university that me and my friend ( https://github.com/mahieyin-rahmun ) implemented. The task here was to create a student list for a course registration schedule. 
The rules are the following:
should come before student s2 if 
either 
(i) s1 completed more credits than s2 
or 
(ii) s1 and s2 completed same number of credits but s1 has higher CGPA than s2. 

For example, if s1 and s2 completed 100 and 110 credits respectively, then s1 should come before s2 in the sorted order. On the other hand, if both of them completed same credits each, then the one with higher CGPA will come before the other one; e.g. if s1 and s2 both completed 100 credits each but s1 had 3.5 CGPA whereas s2 had 3.2 CGPA then s1 should come before s2 in the sorted order.
 
Inputs:  A text file called input.txt (should be in the same folder where your code resides) containing all info of students. Each line of this file should contain the id, name, credits_completed, and CGPA separated by tabs; e.g. 12345 Abid Raihan 30 3.4 26345 Hafiz Adnan 100 3.24 17345 Jakaria Ahmed 80 2.94 72845 Harun Yahia 100 3.84 23745 Jabid Hannan 80 3.47  A number read from user (1 for InsertionSort, 2 for MergeSort, 3 for RandomizedQuickSort, etc ) 

Outputs:  A text file called output.txt containing the student-records in sorted order; e.g. for the above input the output.txt should look like: 72845 Harun Yahia 100 3.84 26345 Hafiz Adnan 100 3.24 23745 Jabid Hannan 80 3.47 17345 Jakaria Ahmed 80 2.94 12345 Abid Raihan 30 3.4  Show the time taken to complete the sorting (in micro-second or milli-second) in console. For this we note the current time before calling your sorting function and the current time after that function returns (using clock_t, for e.g.), and then take their difference.


