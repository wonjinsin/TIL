package main

import (
	"testing"
	"time"
)

// BenchmarkTest ...
func BenchmarkTest(b *testing.B) {
	for n := 0; n < 10; n++ {
		_ = n * 1
		_ = n*n/2 + 1
	}
	time.Sleep(time.Second)
	fmt.Println("done")
}
