def linear_name(arr,key):
    for i in range (len(arr)):
     if arr[i]==key:
        print(f"{key} found at index: {i}")
    return None
name=["Amna","Ali","Nadeem","Sara"]
linear_name(name,"Ali")
