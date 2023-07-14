def find_duplicate(nums):
    """Faça o código aqui."""
    if (
        not nums
        or isinstance(nums, str)
        or len(nums) == 1
        or len(set(nums)) == len(nums)
    ):
        return False
    if min(nums) < 0:
        return False

    nums.sort()

    seen = set()
    for num in nums:
        if num in seen:
            return num
        seen.add(num)
    return False
