package main

import "fmt"

type s [3]byte

func returnType() s { // [3]byte로 해도 마찬가지
	var t s = s{1, 2, 3}
	// print pointer of t
	fmt.Printf("pointer in function is %p\n", &t[0])
	return t
}

func returnSlice() []byte {
	var t s = [3]byte{1, 2, 3}
	fmt.Printf("pointer in function is %p\n", &t[0])
	return t[:]
}

func main() {
	arr := returnType()
	fmt.Printf("pointer in arr is %p\n", &arr[0]) // 함수 내부에서 생성된 배열의 주소가 출력안됨, 값이 복사되서 return되기 때문에, 배열 자체를 반환하면 값 복사가 발생

	slice := returnSlice()
	fmt.Printf("pointer in slice is %p\n", &slice[0]) // 함수 내부에서 생성된 슬라이스의 주소가 출력됨, 값이 복사되지 않기 때문에(포인터 복사), 슬라이스는 포인터처럼 동작
}
