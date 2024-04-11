package main

import (
	"bufio"
	"fmt"
	"os"
	"unicode"
)

func main() {
	if len(os.Args) < 2 {
		fmt.Println("Please provide a file path")
		return
	}

	var sum, left, right int

	file, err := os.Open(os.Args[1])
	if err != nil {
		fmt.Println("Error opening file:", err)
		return
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)

	for scanner.Scan() {
		s := scanner.Text()
		runes := []rune(s)
		for i := 0; i < len(runes); i++ {
			if unicode.IsDigit(runes[i]) && runes[i] >= '0' && runes[i] <= '9' {
				left = int(runes[i]) - int('0')
				break
			}
		}

		for i := len(runes) - 1; i > 0; i-- {
			if unicode.IsDigit(runes[i]) && runes[i] >= '0' && runes[i] <= '9' {
				right = int(runes[i]) - int('0')
				break
			}
		}

		sum += left*10 + right
	}

	if err := scanner.Err(); err != nil {
		fmt.Println("Error reading file:", err)
	}

	// Expected test output: 142
	fmt.Println("Final sum:", sum)
}
