package main

import "fmt"

func lengthOfLongestSubstring(s string) int {
	length := len(s)
	if length < 2 {
		return length
	}
	maxSize := 1
	i := 0
	j := 1
	letters := map[byte]bool{
		s[i]: true,
	}

	for j < length {
		if counted, found := letters[s[j]]; counted && found {
			if j-i+1 > maxSize {
				maxSize = j - i
			}
			i++
			j = i + 1
			letters = map[byte]bool{
				s[i]: true,
			}
		} else {
			if j-i+1 > maxSize {
				maxSize = j - i + 1
			}
			letters[s[j]] = true
			j++
		}
	}

	return maxSize
}

func main() {
	fmt.Println(lengthOfLongestSubstring("abcabcbb")) // 3
	fmt.Println(lengthOfLongestSubstring("bbbb"))     // 1
	fmt.Println(lengthOfLongestSubstring("pwwkew"))   // 3
	fmt.Println(lengthOfLongestSubstring(""))         // 0
	fmt.Println(lengthOfLongestSubstring("a"))        // 1
	fmt.Println(lengthOfLongestSubstring("ab"))       // 2
	fmt.Println(lengthOfLongestSubstring("bb"))       // 1
	fmt.Println(lengthOfLongestSubstring("aab"))      // 2
}
