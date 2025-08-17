def find_median_sorted_arrays(nums1, nums2):
    nums = sorted(nums1 + nums2)
    n = len(nums)
    return (nums[n//2] + nums[~(n//2)]) / 2

if __name__ == "__main__":
    nums1 = list(map(int, input("Enter first sorted array: ").split()))
    nums2 = list(map(int, input("Enter second sorted array: ").split()))
    print("Median:", find_median_sorted_arrays(nums1, nums2))
