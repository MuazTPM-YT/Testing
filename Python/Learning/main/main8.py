def binarysearch(array,key):
    low=0
    high=len(array)-1
    mid=0

    while low<=high:
        mid=(low+high)//2
        if array[mid]==key:
            print(f"Element found in {mid}")
            break
        
        elif array[mid]<key:
            low=mid+1
        
        elif array[mid]>key:
            high=mid-1
    
    else:
        print(f"Element not found in the array")

        if array[mid]<key:
            high+=1
            low-=1
            print(f"Element is between {low} and {high}")
        
        elif array[mid]>key:
            low-=1
            high+=1
            print(f"Element is between {low} and {high}")

ar=[2,4,6,8,10,12]
key=7

binarysearch(ar,key)