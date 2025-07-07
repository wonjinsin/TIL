package main

import "fmt"

func main() {
	foo := make([]int, 3, 6)
	fmt.Println(foo[0]) // 0
	// fmt.Println(foo[4]) error
	fmt.Printf("len is %d, cap is %d\n\n", len(foo), cap(foo))

	foo = append(foo, 3, 4, 5, 6)
	fmt.Printf("After append len is %d, cap is %d\n\n", len(foo), cap(foo))

	bar := foo[1:3]
	fmt.Println("After slicing foo is", foo)
	fmt.Println("After slicing bar is", bar)
	fmt.Printf("after slicing foo's len is %d, cap is %d\n", len(foo), cap(foo))
	fmt.Printf("after slicing bar's len is %d, cap is %d\n", len(bar), cap(bar))
	fmt.Printf("Foo's address is %p and Bar's address is %p\n\n", &foo[1], &bar[0])

	bar = append(bar, 100)
	fmt.Println("After appending foo is", foo) // 여기에서 foo의 [3]이 100으로 바뀌었음
	fmt.Println("After appending bar is", bar)
	fmt.Printf("After appending foo's length is %d, cap is %d\n", len(foo), cap(foo)) // length는 같음, foo의 [3]이 바뀜
	fmt.Printf("After appending bar's length is %d, cap is %d\n", len(bar), cap(bar))
	fmt.Printf("After appending foo's address is %p\n", &foo[1])
	fmt.Printf("After appending bar's address is %p\n\n", &bar[0])

	bar = append(bar, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
	fmt.Println("After appending bar is", bar)
	fmt.Println("After appending foo is", foo)
	fmt.Printf("After appending foo's address is %p\n", &foo[1])
	fmt.Printf("After appending bar's address is %p\n", &bar[0]) // 이렇게 되면 이제 bar가 새로운 주소로 새로운 슬라이스를 만들고 값을 복사

}
