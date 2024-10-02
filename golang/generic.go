package main

import (
	"fmt"
	"hash/fnv"
)

type MyInt int

func genericFn[T int | int32](a, b T) T {
	return a + b
}

type Integer interface {
	int8 | int16 | int32 | int64 | int
}

func genericFn2[T Integer](a, b T) T {
	return a + b
}

type IntegerWithAlias interface {
	~int8 | ~int16 | ~int32 | ~int64 | ~int
}

func genericFn3[T IntegerWithAlias](a, b T) T {
	return a + b
}

type ComparableHasher interface {
	comparable
	Hash() uint32
}

type MyString string

func (s MyString) Hash() uint32 {
	h := fnv.New32a()
	h.Write([]byte(s))
	return h.Sum32()
}

func Equal[T ComparableHasher](a, b T) bool {
	if a == b {
		return true
	}

	return a.Hash() == b.Hash()
}

func GenericExample[T, F any](t []T, f func(T) F) []F {
	result := make([]F, len(t))
	for i, v := range t {
		result[i] = f(v)
	}

	return result
}

func main() {
	fmt.Println(genericFn(1, 2))
	fmt.Println(genericFn(3, 4))

	var myInt MyInt
	myInt = 5
	fmt.Println(genericFn3(myInt, myInt))

	var MyStringA MyString = "Foo"
	var MyStringB MyString = "Bar"

	fmt.Println(Equal(MyStringA, MyStringB))

	fmt.Println(GenericExample([]int{1, 2, 3}, func(t int) int {
		return t * 2
	})) // double
}
