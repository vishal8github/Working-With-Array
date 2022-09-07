import numpy

arr1 = numpy.array([eval(x) for x in input("\nEnter values for array1: ").split()])
arr2 = numpy.array([eval(x) for x in input("Enter values for array2: ").split()])

print(f"\nArray1: {arr1}    type: {type(arr1)}")
print(f"Array2: {arr2}    type: {type(arr2)}")

print(f"\nAddition of two arrays is {arr1 + arr2}")