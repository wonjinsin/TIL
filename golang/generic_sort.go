package main

import (
	"fmt"
	"io"
	"os"
	"sort"
)

type sliceFn[T any] struct {
	s       []T
	Compare func(T, T) bool
}

func (s sliceFn[T]) Len() int {
	return len(s.s)
}

func (s sliceFn[T]) Less(i, j int) bool {
	return s.Compare(s.s[i], s.s[j])
}

func (s sliceFn[T]) Swap(i, j int) {
	s.s[i], s.s[j] = s.s[j], s.s[i]
}

func main() {
	s := sliceFn[int]{s: []int{3, 2, 1}, Compare: func(a, b int) bool {
		return a < b
	}}
	sort.Sort(s)
	fmt.Println(s.s)

	var t io.Writer
	t = os.Stdout
}
