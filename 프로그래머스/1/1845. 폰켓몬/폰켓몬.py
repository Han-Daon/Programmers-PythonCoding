def solution(nums):
    num_set = set(nums) #중복 제거
    n = len(nums)
    k = n//2 #만약 다 한종류씩 있을때
    return min(k, len(num_set))