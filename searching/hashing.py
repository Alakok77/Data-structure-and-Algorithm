"""mod doc"""
class Student:
    def __init__(self, std_id, name, gpa):
        self.__std_id = std_id
        self.__name = name
        self.__gpa = gpa

    def getStd_id(self):
        return self.__std_id

    def getName(self):
        return self.__name
    
    def getGPA(self):
        return self.__gpa

    def print_details(self):
        print(f"ID: {self.__std_id}")
        print(f"Name: {self.__name}")
        print(f"GPA: {self.__gpa:.2f}")

class ProbHash:
    def __init__(self, size):
        self.__size = size
        self.__hash_table = []
        for _ in range(size):
            self.__hash_table.append(None)

    def hash_func(self, key):
        return key%self.__size
    
    def rehash_func(self, key):
        return (key + 1) % self.__size

    def insert_data(self, student: "Student"):
        index = self.hash_func(student.getStd_id())
        if all(self.__hash_table):
            print(f"The list is full. {student.getStd_id()} could not be inserted.")
            return
        while self.__hash_table[index]:
            index = self.rehash_func(index)

        if index > self.__size:
            print(f"The list is full. {student.getStd_id()} could not be inserted.")
        else:
            self.__hash_table[index] = student
            print(f"Insert {student.getStd_id()} at index {index}")

    def search_data(self, std_id):
        index = self.hash_func(std_id)
        count = 0
        while self.__hash_table[index]:
            if self.__hash_table[index].getStd_id() == std_id:
                print(f"Found {std_id} at index {index}")
                return self.__hash_table[index]
            if count > self.__size:
                break
            index = self.rehash_func(index)
            count += 1
            
        print(f"{std_id} does not exist.")
            
def main():
    import json
    size = int(input())
    hashtable = ProbHash(size)
    while True:
        finish = input()
        if finish == "Done":
            break
        condition, data = finish.split(" = ")
        if condition == "I":
            std_in = json.loads(data)
            std = Student(std_in["ID"], std_in["Name"], std_in["GPA"])
            hashtable.insert_data(std)
        elif condition == "S":
            print("------")
            student = hashtable.search_data(int(data))
            if student is not None:
                student.print_details()
            print("------")
        else:
            print("Invalid Condition!")
main()