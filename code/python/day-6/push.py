# Push all the zero to end.
# Maintain the relative order of all the items inside array.

def pushzeroes(arr):
    c=0
    # Move all non zero to one end.
    for i in range(len(arr)):
        if arr[i]!=0:
            arr[c]=arr[i]
            c+=1
    # Move 0's to other end.
    while c<len(arr):
        arr[c]=0
        c+=1
    print(arr)
ar=[3,0,1,0,5,9,0,6,7]
pushzeroes(ar)