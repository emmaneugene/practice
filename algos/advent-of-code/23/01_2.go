package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
	"unicode"
)

type numberString struct {
	val int
	str string
}

func main() {
	if len(os.Args) < 2 {
		fmt.Println("Please provide a file path")
		return
	}

	var sum, left, right int
	numStrs := []numberString{{1, "one"}, {2, "two"}, {3, "three"}, {4, "four"}, {5, "five"}, {6, "six"}, {7, "seven"}, {8, "eight"}, {9, "nine"}}

	filePath := os.Args[1]

	file, err := os.Open(filePath)
	if err != nil {
		fmt.Println("Error opening file:", err)
		return
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)

	for scanner.Scan() {
		s := scanner.Text()
		left, right = 0, 0
		leftFound, rightFound := false, false

		for i := 0; i < len(s); i++ {
			if unicode.IsDigit(rune(s[i])) && s[i] >= '0' && s[i] <= '9' {
				left = int(s[i]) - int('0')
				leftFound = true
			}

			for _, numStr := range numStrs {
				if i+len(numStr.str) > len(s) {
					continue
				}
				if strings.Compare(numStr.str, s[i:i+len(numStr.str)]) == 0 {
					left = numStr.val
					leftFound = true
					break
				}
			}

			if leftFound {
				break
			}
		}

		for i := len(s) - 1; i > 0; i-- {
			if unicode.IsDigit(rune(s[i])) && s[i] >= '0' && s[i] <= '9' {
				right = int(s[i]) - int('0')
				rightFound = true
			}

			for _, numStr := range numStrs {
				if i+len(numStr.str) > len(s) {
					continue
				}
				if strings.Compare(numStr.str, s[i:i+len(numStr.str)]) == 0 {
					right = numStr.val
					rightFound = true
					break
				}
			}

			if rightFound {
				break
			}
		}

		sum += left*10 + right
	}

	// Expected value: 281
	fmt.Println("Final sum:", sum)
}
