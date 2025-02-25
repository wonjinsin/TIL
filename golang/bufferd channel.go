package main

import "time"

func main() {
	// unbuffered()
	time.Sleep(100 * time.Millisecond)
	buffered()
}

func unbuffered() {
	done := make(chan bool)

	go func() {
		done <- true                  // done을 누가 수신 하기전에 block, block
		print("print after use done") // done 수신되고 print (5초 기다림)
	}()
	time.Sleep(5 * time.Second)
	<-done // done 수신
	time.Sleep(100 * time.Millisecond)
	print("Finish")

	// wait 5 seconds
	// print after use done
	// Finish
}

func buffered() {
	done := make(chan bool, 1)

	go func() {
		done <- true                   // done을 누가 수신 하든말든 다음 동작함, non-blocking
		print("print before use done") // 안기다리고 바로 print
	}()
	time.Sleep(5 * time.Second)
	<-done // done 수신
	time.Sleep(100 * time.Millisecond)
	print("Finish")

	// print before use done
	// wait 5 seconds
	// Finish
}
