package main

import (
	"errors"
	"fmt"
	"log"
	"net/http"
)

type options struct {
	Port int
}

type Opts func(*options) error

func WithPort(port int) Opts {
	return func(o *options) error {
		if port <= 0 {
			return errors.New("Port is invalid")
		}

		o.Port = port
		return nil
	}
}

func NewHTTPServer(opts ...Opts) (*http.Server, error) {
	var options *options
	for _, opt := range opts {
		if err := opt(options); err != nil {
			return nil, err
		}
	}

	port := options.Port

	return &http.Server{
		Addr: fmt.Sprintf(":%d", port),
	}, nil
}

func main() {
	server, err := NewHTTPServer(
		WithPort(8080),
	)
	if err != nil {
		log.Fatalf(err.Error())
	}
	server.ListenAndServe()
}
