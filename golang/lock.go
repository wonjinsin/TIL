package main

import (
	"fmt"
	"sync"
	"time"
)

var (
	mu    sync.Mutex
	cond  = sync.NewCond(&mu)
	ready = false
)

// 데이터를 기다리는 고루틴
func worker(id int) {
	mu.Lock()    // or cond.L.Lock()
	for !ready { // ready가 false면 대기
		fmt.Printf("Worker %d: 대기 중...\n", id)
		// mu.unLock이 자동으로 불리고, Signal이나 Broadcast가 불리면 다시 Lock이 되면서, 대기 중인 고루틴이 깨어남
		// Signal을 받을때 위에 mu.Lock이 불리는게 아니고, 시작되려면 무조건 Lock을 자체적으로 하고 실행되는것도 cond.Wait 다음라인부터 실행되는것
		cond.Wait()
	}
	fmt.Printf("Worker %d: 데이터 처리 시작!\n", id)
	mu.Unlock() // or cond.L.Unlock()
}

func main() {
	var wg sync.WaitGroup
	numWorkers := 5

	// 5개의 worker 고루틴 실행
	for i := 1; i <= numWorkers; i++ {
		wg.Add(1)
		go func(id int) {
			defer wg.Done()
			worker(id)
		}(i)
	}

	time.Sleep(2 * time.Second) // 데이터 준비 중
	fmt.Println("데이터 준비 완료!")

	mu.Lock()
	ready = true // 데이터 준비 완료
	mu.Unlock()

	cond.Broadcast() // 모든 대기 중인 worker를 깨움

	wg.Wait() // 모든 고루틴이 끝날 때까지 대기
	fmt.Println("모든 작업 완료!")
}
