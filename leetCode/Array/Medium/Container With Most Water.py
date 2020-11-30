def maxArea(height):
    # set two pointers at either end of array
    # initialize empty max array

    left, right, max_area = 0, len(height) - 1, 0

    while left < right:

        # We know that the area is limited by the smallest of two heights so
        if height[right] >= height[left]:
            # area is the product of index distance by the height of shorter wall
            area_so_far = (right - left) * height[left]
            print(area_so_far)
            # encourage bias towards height
            left += 1

            # if this value is largest so far, store if.
            max_area = max(max_area, area_so_far)

        # mirror case for if left height is larger
        else:
            area_so_far = (right - left) * height[right]
            print(area_so_far)
            right -= 1
            max_area = max(max_area, area_so_far)
    return max_area


a = list(map(int, input().split()))
print(maxArea(a))



