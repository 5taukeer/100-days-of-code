# Find the max product pair in an array.

def maxProduct(arr, n): 
    if (n < 2):
        print("No pairs exists")
        return
     
    a = arr[0]; b = arr[1]
 
    for i in range(0, n): 
        for j in range(i + 1, n):
            if (arr[i] * arr[j] > a * b):
                a = arr[i]; b = arr[j]
    print("Max product pair is {", a, ",", b, "}",
                                          sep = "")

arr = [1,5,6,-3,-10]
n = len(arr)
maxProduct(arr, n)