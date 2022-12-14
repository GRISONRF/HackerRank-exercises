""" There are 26 employees to complete a task. The employees have IDs in the range ['a'-'z'], where employee 0 has ID = 'a', employee 1 has ID = 'b', ... employee 25 has ID = 'z'. The task runs continuously, and the employees take turns to perform the task. At any moment of time, exactly one employee is working on the task. As soon as an employee leaves the task, the following employee starts working on it.

Given the employee numbers and the times at which they leave the task in a 2-D array leaveTimes, find the ID of the employee who has the longest single time slot at the task.
leaveTimes[i][0] represent employee numbers, in the range 0-25. leaveTimes[i][1] represents the time at which the employee leaves the task. The elements will be given in ascending time order.
Note: If the same employee has two continuous slots, the slots are considered to be different.

Example

leaveTimes = [[0, 3], [2, 5], [0, 9], [1, 15]] """


def findLongestSingleSlot(leaveTimes):

    employees = {0:'a', 1:'b', 2:'c', 3:'d', 4:'e', 5:'f', 6:'g', 7:'h', 8:'i', 9:'j', 10:'k', 11:'l', 12:'m', 13:'n', 14:'o', 15:'p', 16:'q', 17:'r', 18:'s', 19:'t', 20:'u', 21:'v', 22:'w', 23:'x', 24:'y', 25:'z'}

    # need to find the greatest interval between one [x,x][1] and [y,y][1]
    intervals = 0
    nurse = int()
   
    for i in range(len(leaveTimes)-1):
         #for the first interval, where we are comparing with 0
        if i == 0:
            intervals = leaveTimes[0][1] - leaveTimes[0][0]
           
        else:
            if leaveTimes[i+1][1] - leaveTimes[i][1] > intervals:
                intervals = leaveTimes[i+1][1] - leaveTimes[i][1]
                nurse = leaveTimes[i+1][0]
    return employees[nurse]


print(findLongestSingleSlot([[0, 3], [2, 5], [0, 9], [1, 15]]))