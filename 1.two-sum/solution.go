package twosum

func twoSum(nums []int, target int) []int {
	numLength := len(nums)
	var (
		first  int
		second int
	)

	for i := 0; i < numLength-1; i++ {
		for j := i + 1; j < numLength; j++ {
			first = nums[i]
			second = nums[j]
			if first+second == target {
				return []int{i, j}
			}
		}
	}

	return []int{}
}
