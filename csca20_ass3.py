import csv
FILE_NAME = "grades.csv"
NAME_COL = 0
GRAD_COL = 1
SNUM_COL = 3    # student number at column 2

def read_csv():
    with open(FILE_NAME, "r") as reader_file:
        reader = csv.reader(reader_file, delimiter=",")
        data = list(reader)
    return (data[0], data[1:])

'''
finds the student in data by given name and return info at a specified column
'''
def get_info(name, column):
    data = read_csv()    
    for ele in data[1]:
        if ele[NAME_COL] == name:
            return ele[column]
    return -1

def write_to_csv(data):
    with open(FILE_NAME, 'w') as writer_file:
        writer = csv.writer(writer_file)
        writer.writerows(data)

def add_student (name, grade, number):
    data = read_csv()
    data = [data[0]] + data[1] + [[name, grade, number]]
    write_to_csv(data)
    print("Student information added successfully!")
    
    
def remove_student(name):
    data = read_csv()
    for grade_record in data[1]:
        if grade_record[0] == name:
            data[1].remove(grade_record)
            write_to_csv([data[0]] + data[1])
            print("Student information removed successfully!")
            return
    print("No student with such name")

    
def get_average():
    data = read_csv()[1]
    nsum = 0
    n = len(data)
    for i in range(n):
        nsum += int(data[i][GRAD_COL])
    return nsum//n
    
while(True):
    key = raw_input("Please write the number for your next action:\n" +
          "1) Print average grade\n" +
          "2) Add a new grade\n" +
          "3) Remove a student\n" +
          "4) Get information from a student\n" +
          "Write any other key to exit the program\n")
    if (key == "1") :
        print("The class average grade is: " + str(get_average()))
    elif (key == "2") :
        ans = raw_input("Please enter in one line, separated by spaces the name, grade and student id you want to add\n")
        name, grade, id = ans.split(' ')
        print(name)
        add_student(name, grade, id)
    elif (key == "3") :
        ans = raw_input("Please enter the name of student that you want to remove from the list\n")
        remove_student(ans)
    elif (key == "4") :
        name = raw_input("Please enter the name of student that you want to know\n")
        ans = raw_input("What information do you want to know?\n" +
                        "1) Grade\n" +
                        "2) Student number\n")
        print("The answer to your question is " + get_info(name, int(ans)))
    else:
        print("Program exited")
        exit(0)






