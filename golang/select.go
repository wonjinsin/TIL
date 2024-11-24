package main

import (
	"fmt"
	"time"
)

func main() {
	ch := make(chan string)
	ticker := time.NewTicker(1 * time.Second)

	i := 0
	for {
		select {
		case <-ticker.C:
			go func() {
				i++
				ch <- fmt.Sprintf("tick%v", i)
			}()
		case msg := <-ch:
			fmt.Println(msg)
		} // Blocks forever
	}
}
