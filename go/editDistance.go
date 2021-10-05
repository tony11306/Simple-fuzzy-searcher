package main

import "unicode/utf8"
import "C"
import "math"

func lenStr(s string) int {
	return utf8.RuneCountInString(s)
}

func min(nums ...int) int {
	minValue := math.MaxInt32

	for _, val := range nums {
		if val < minValue {
			minValue = val
		}
	}

	return minValue
}

func max(nums ...int) int {
	maxValue := math.MinInt32

	for _, val := range nums {
		if val > maxValue {
			maxValue = val
		}
	}

	return maxValue
}

//export LongestCommonSubsequenceLength
func LongestCommonSubsequenceLength(s1 string, s2 string) int {
	s1Len := lenStr(s1)
	s2Len := lenStr(s2)

	if s1Len == 0 || s2Len == 0 {
		return 0
	}

	dp := make([][]int, s1Len+1)

	for i := 0; i <= s1Len; i++ {
		dp[i] = make([]int, s2Len+1)
	}

	for i := 1; i <= s1Len; i++ {
		for j := 1; j <= s2Len; j++ {
			if s1[i-1] == s2[j-1] {
				dp[i][j] = dp[i-1][j-1] + 1
			} else {
				dp[i][j] = max(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
			}
		}
	}

	return dp[s1Len][s2Len]

}

//export LevenshteinDistance
func LevenshteinDistance(s1 string, s2 string) int {
	s1Len := lenStr(s1)
	s2Len := lenStr(s2)

	if s1Len == 0 || s2Len == 0 {
		return max(s1Len, s2Len)
	}

	dp := make([][]int, s1Len+1)

	for i := 0; i <= s1Len; i++ {
		dp[i] = make([]int, s2Len+1)
	}

	for i := 1; i <= s1Len; i++ {
		dp[i][0] = i
	}

	for j := 1; j <= s2Len; j++ {
		dp[0][j] = j
	}

	for i := 1; i <= s1Len; i++ {
		for j := 1; j <= s2Len; j++ {
			cost := 1
			if s1[i-1] == s2[j-1] {
				cost = 0
			}

			dp[i][j] = min(dp[i-1][j]+1, dp[i][j-1]+1, dp[i-1][j-1]+cost)
			
		}
	}

	return dp[s1Len][s2Len]
}

func main()  {
}