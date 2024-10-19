# Simple sort using recursion ("Bubble Sort")
iteration: int = 0
step: int = 0


def sort_numbers(nums) -> int:
    """Sorts a list of numbers using the Bubble Sort algorithm recursively.

    Args:
      nums: The input list of numbers to be sorted.

    Returns:
      The sorted list of numbers.
    """
    global iteration
    global step
    no_changes: list[bool] = []
    swapped: str

    if len(nums) <= 1:
        return nums

    iteration += 1

    for i in range(len(nums) - 1):
        step += 1

        print(f">>> Iteration {iteration}, step {step} [{step * '#'}]")
        print(f"Source list: {nums}")
        print(
            "Compare elements: "
            f"{nums[i]}[index {i}] and {nums[i + 1]}[index {i + 1}]"
        )
        if nums[i] > nums[i + 1]:
            nums[i], nums[i + 1] = nums[i + 1], nums[i]
            no_changes.append(False)
            swapped = "Yes"
        else:
            no_changes.append(True)
            swapped = "No"

        print(f"Swap values ({nums[i]} <-> {nums[i + 1]})? -- {swapped}")
        print(f"Result of step {step}: {nums}\n")

    if not all(no_changes):
        sort_numbers(nums)

    return nums


numbers: list = [5, 4, 3, 2, 1]

print("Recursively sort using the Bubble Sort algorithm")
print("------------------------------------------------\n")

print(f"Unsorted list: {numbers}")
print(f"Length of the list: {len(numbers)} elements\n")
print(f"Sorted list: {sort_numbers(numbers)}")
print(f"Iterations: {iteration}, steps: {step}")
