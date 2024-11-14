package main

import (
	"fmt"
	"net/http"
	"os"
	"os/signal"
	"syscall"
)

func handler(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintf(w, "Hello, World!")
}

func main() {
	// 핸들러 등록
	http.HandleFunc("/", handler)

	// 채널 생성
	quit := make(chan os.Signal, 1)
	signal.Notify(quit, syscall.SIGINT, syscall.SIGTERM)

	// 서버 시작 (여기서 블로킹)
	go func() {
		fmt.Println("Starting server on :8080")
		if err := http.ListenAndServe(":8080", nil); err != nil {
			fmt.Println("Error starting server:", err)
		}
	}()

	// 종료 신호 대기
	<-quit
	fmt.Println("Shutting down server...")
}
