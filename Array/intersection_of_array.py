nums1=[1,2,3,2]
nums2=[6,8,7,2]
def common(a,b):

    a=set(nums1)
    b=set(nums2)
    common_elements=a.intersection(b)
    if common_elements:
        print (common_elements)
    else :
        print("sorry")

common(nums1,nums2)
#to find the common elements between two sets we can use a function called as set ,the set has property like union and intersection from which we can find numbers common