package main

import (
	"context"
	"fmt"
	"time"
)

func main() {
	ctx, cancel := context.WithCancel(context.Background())
	ch := make(chan int)

	go square(ch)
	ch <- 9

	time.Sleep(time.Second * 3)
}

func square(c <-chan int) {
	select {
	case msg := <-c:
		fmt.Println(msg * msg)
		time.Sleep(time.Second * 1)
	default:
		fmt.Println("no message")
	}
}
