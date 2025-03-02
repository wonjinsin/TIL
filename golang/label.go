package main

import "fmt"

func main() {
label:
	for i := 0; i < 10; i++ {
		for j := 0; j < 10; j++ {
			if i == 5 {
				fmt.Println("continue")
				continue label // 5는 건너뛰고 6부터 다시 시작
			}
			fmt.Println(i, j)
		}
	}
	fmt.Println("end1")

label2:
	for i := 0; i < 10; i++ {
		if i == 5 {
			fmt.Println("break")
			break label2 // 5에서 멈춤
		}
		fmt.Println(i)
	}
	fmt.Println("end2")

	for i := 0; i < 10; i++ {
	label3:
		for j := 0; j < 10; j++ {
			if j == 5 {
				fmt.Println("break") // 5에서 멈춤, 그리고 다음 i loop
				break label3
			}
			fmt.Println(i, j)
		}
	}
}
