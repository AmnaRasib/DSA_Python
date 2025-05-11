def Binary_Search(arr,gps):
    size=len(arr)-1
    left=0
    right=size
    while left<=right:
        mid=(left+right)//2
        if arr[mid]==gps:
            return mid
        elif arr[mid]<gps:
            left=mid+1
        elif arr[mid]>gps:
            right=mid-1
    return None
# Example usage:
# Let's assume `gps_coordinates` is a sorted list of GPS locations (e.g., tuples with lat, long)
gps_coordinates = [(40.7128, -74.0060), (34.0522, -118.2437), (51.5074, -0.1278), (48.8566, 2.3522)]
target_location = (34.0522, -118.2437)

print("Element found at index:", Binary_Search(gps_coordinates, target_location))
    
