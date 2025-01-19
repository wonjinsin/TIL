package main

import "fmt"

func main() {
	// aboutBitMasking()
	// aboutUnixTime()
	getMaxValue()
}

func aboutBitMasking() {
	// 비트마스킹이란? &연산으로 특정 비트 이상이 생기지 않도록 값을 제한하기 위해 사용

	// 예를들어 초를 2진수로 표현했을때 6비트를 사용해야하는데, 컴퓨터는 4,8,16,32비트는 사용하기 때문에 결국 컴퓨터는 8비트가 됨,
	// 그리고 유저가 초를 7비트 이상(64초 이상)을 입력하면 값이 이상하게 들어가기 때문에 이를 방지하기 위한 용도도 있음
	// 메모리 관리가 효율적이고, 컴퓨터의 연산도 더 빠름
	seconds := 54    // 110110, 컴퓨터는 00110110으로 표현
	bitField := 0x3F // 16진수로 표현하면 0011 1111, 00111111로 표현됨

	maskedSeconds := seconds & bitField // 00110110 & 00111111 = 00110110, 54, 만약 seconds가 63초를 초과해도 54가 됨, 이게 비트마스킹

	fmt.Println(seconds)
	fmt.Println(maskedSeconds)
	fmt.Printf("%08b", maskedSeconds)

}

func aboutUnixTime() {
	// 예시 값: 1일, 12시, 34분, 56초
	days := 1     // 5비트
	hours := 12   // 5비트
	minutes := 34 // 6비트
	seconds := 56 // 6비트

	// 비트 필드로 저장 (각 필드를 6비트, 5비트 등으로 이동하여 결합)
	bitField := (days << 21) | (hours << 16) | (minutes << 11) | (seconds << 5)

	// 복원 (각 비트 필드에서 추출)
	recoveredDays := (bitField >> 21) & 0x1F    // 5비트
	recoveredHours := (bitField >> 16) & 0x1F   // 5비트
	recoveredMinutes := (bitField >> 11) & 0x3F // 6비트
	recoveredSeconds := (bitField >> 5) & 0x3F  // 6비트

	// 출력
	fmt.Printf("원래 값: %d일, %d시, %d분, %d초\n", days, hours, minutes, seconds)
	fmt.Printf("복원된 값: %d일, %d시, %d분, %d초\n", recoveredDays, recoveredHours, recoveredMinutes, recoveredSeconds)
}

func getMaxValue() {
	t := 0b1010 // golang에서 2진수 표현, -는 안됨
	fmt.Println(t)

	// x비트의 최대값 구하기
	x := 8                   // 8비트
	maxValue := (1 << x) - 1 // 2진수는 0부터 시작하기 때문에 마지막에 -1을 해줘야함, 100000000 - 1 = 011111111

	fmt.Printf("%08b\n", maxValue)
	fmt.Println(maxValue)
}
