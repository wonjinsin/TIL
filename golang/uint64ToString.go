package main

import "fmt"

func main() {
	fmt.Println(uint64ToString(123456789012345678))
}

func uint64ToString(n uint64) string {
	// U+0030 = 0, ASCII = 0x30, decimal = 48
	// ...
	// U+0039 = 9, ASCII = 0x39, decimal = 57

	var a [20]byte
	i := 20

	var q uint64
	for n >= 10 {
		i--
		q = n / 10
		a[i] = uint8(n-q*10) + 0x30
		n = q
	}

	i--
	a[i] = uint8(n + 0x30)
	return string(a[i:])
}
