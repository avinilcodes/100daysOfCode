package main

// Runtime
// 6ms
// Beats 53.93%of users with Go
// Memory
// 2.76MB
// Beats 77.73%of users with Go

func romanToInt(s string) int {
	var prev rune
	var total int = 0
	for _, val := range s {
		if val == rune('I') {
			total += 1
			prev = val
			continue
		}
		if prev == rune('I') && val == rune('V') {
			total += 3
			prev = val
			continue
		}
		if prev == rune('I') && val == rune('X') {
			total += 8
			prev = val
			continue
		}
		if prev == rune('X') && val == rune('L') {
			total += 30
			prev = val
			continue
		}
		if prev == rune('X') && val == rune('C') {
			total += 80
			prev = val
			continue
		}
		if prev == rune('C') && val == rune('D') {
			total += 300
			prev = val
			continue
		}
		if prev == rune('C') && val == rune('M') {
			total += 800
			prev = val
			continue
		}
		if val == rune('X') {
			total += 10
			prev = val
			continue
		}
		if val == rune('C') {
			total += 100
			prev = val
			continue
		}
		if val == rune('V') {
			total += 5
			prev = val
			continue
		}
		if val == rune('L') {
			total += 50
			prev = val
			continue
		}
		if val == rune('D') {
			total += 500
			prev = val
			continue
		}
		if val == rune('M') {
			total += 1000
			prev = val
			continue
		}
	}
	return total
}
