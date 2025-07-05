package main

import (
	"fmt"
	"sync/atomic"
	"time"
)

var id atomic.Int64

func main() {
	var signal = make(chan bool)

	go func() {
		for {
			_, ok := <-signal
			fmt.Println("Received signal", ok)
			if !ok {
				fmt.Println("Exit Worker")
				return
			}

			for {
				latest := id.Swap(0)
				if latest == 0 {
					break
				}

				fmt.Printf("ID is %d\n", latest)
				time.Sleep(1 * time.Second)
			}
		}
	}()

	for i := int64(0); i < 40; i++ {
		time.Sleep(100 * time.Millisecond)
		id.Store(i + 1)

		select {
		case signal <- true:
			fmt.Println("Sent signal")
			// 이 default가 없으면, signal에 데이터를 넣는게 block이 되기 때문에,
			// go routine안에 최상의 forloop가 다음으로 가기 전까지 위에있는 signal <- true가 계속 대기함
			// 즉, non-blocking이 안됨
			// default:
		}
	}
	close(signal)
	time.Sleep(2 * time.Second)
}
