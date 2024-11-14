package main

import (
	"fmt"
	"io"
	"log"
	"net"
)

func main() {
	// Create a listener on a random port.
	listener, err := net.ListenAndServe("tcp", "127.0.0.1:")
	if err != nil {
		log.Fatalf(fmt.Sprintf("%v", err))
	}

	done := make(chan struct{})
	go func() {
		defer func() { done <- struct{}{} }()

		for {
			conn, err := listener.Accept()
			if err != nil {
				fmt.Print(err)
				return
			}

			go func(c net.Conn) {
				defer func() {
					c.Close()
					done <- struct{}{}
				}()

				buf := make([]byte, 1024)
				for {
					n, err := c.Read(buf)
					if err != nil {
						if err != io.EOF {
							fmt.Print(err)
						}
						return
					}

					fmt.Printf("received: %q", buf[:n])
				}
			}(conn)
		}
	}()

	conn, err := net.Dial("tcp", listener.Addr().String())
	if err != nil {
		log.Fatal(err)
	}

	select {}

	conn.Close()
	<-done
	listener.Close()
	<-done
}
