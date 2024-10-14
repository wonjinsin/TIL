package main

import "fmt"

type NodeMulti[T1 any, T2 any] struct {
	val1 T1
	val2 T2
	next *NodeMulti[T1, T2]
}

func NewNodeMulti[T1 any, T2 any](v1 T1, v2 T2) *NodeMulti[T1, T2] {
	return &NodeMulti[T1, T2]{val1: v1, val2: v2}
}

func (n *NodeMulti[T1, T2]) Push(v1 T1, v2 T2) *NodeMulti[T1, T2] {
	node := NewNodeMulti(v1, v2)
	n.next = node
	return node
}

func main() {
	node1 := NewNodeMulti(1, 2)
	node1.Push(3, 4).Push(5, 6).Push(6, 7)

	for node1 != nil {
		fmt.Print(node1.val1, " - ", node1.val2)
		node1 = node1.next
	}
	fmt.Println()

	node2 := NewNode("Hi")
	node2.Push("Hello").Push("How are you")

	for node2 != nil {
		fmt.Print(node2.val, " - ")
		node2 = node2.next
	}
}
