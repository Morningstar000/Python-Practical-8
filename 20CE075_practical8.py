# 20CE075 Parth Parmar
# Practical 8: Write a Program in Python to implement a Stack Data Structure using Class and Objects, with push, pop, and traversal method.
# https://github.com/Morningstar000/Python-Practical-8

class stack:
    def __init__(self):
        self.arr = []

    def push(self, data):
        self.arr.append(data)

    def pop(self):
        return self.arr.pop()

    def is_empty(self):
        return self.arr == []

    def display(self):
        if self.is_empty():
            print("No element in stack")
        for i in self.arr:
            print(i, end=" ")
        print("\n")

st = stack()
st.push(94)
st.push(86)
st.push(75)
print("Number of  element in stack:")
st.display()
st.pop()
print("Number of element in stack")
st.display()
