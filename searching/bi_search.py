"""mod doc"""
import json
class Student:
    def __init__(self, std_id, name, gpa):
        self.__std_id = std_id
        self.__name = name
        self.__gpa = gpa

    def getStId(self):
        return self.__std_id

    def getName(self):
        return self.__name
    
    def getGPA(self):
        return self.__gpa

    def print_details(self):
        print(f"ID: {self.__std_id}")
        print(f"Name: {self.__name}")
        print(f"GPA: {self.__gpa:.2f}")

def binary_search(data, name):
    begin = 0
    end = len(data) - 1
    mid = int((begin + end) / 2)
    time = 0
    
    while begin <= end:
        time += 1
        mid = int((begin + end) / 2)
        if data[mid].getName() == name:
            print(f"Found {name} at index {mid}")
            data[mid].print_details()
            print(f"Comparisons times: {time}")
            return
        if name > data[mid].getName():
            begin = mid + 1
        else:
            end = mid - 1

    print(f"{name} does not exists.")
    print(f"Comparisons times: {time}")

def main():
    lst = json.loads(input())
    students = []
    name = input()
    for i in lst:
        students.append(Student(i["id"], i["name"], i["gpa"]))
    binary_search(students, name)
main()