# Flyweight

> 구조 패턴중 하나로 공유할 수 있는 인스턴스는 공유하게 하여, new를 이용한 메모리 낭비를 막을수 있는 방법

### 3가지 요소
- 실제 공유될 객체
- 객체 인스턴스를 생성하고 공유해주는 팩토리(Factory)
- 패턴을 사용할 client

```php
<?php

class Tree {
	private $color;
	private $x;
	private $y;

	public function __construct($color) {
		$this->color = $color;
	}

	public function setX($x) {
		return $this->x = $x;
	}

	public function setY($y) {
		return $this->y = $y;
	}

	public function install() {
		return sprintf('x: %d, y:%d, %s색 나무를 설치했습니다.', $this->x, $this->y, $this->color);
	}
}

class Treefactory {
	private $treeMap;

	public function getTree($color) {
		$tree = $this->treeMap[$color];
		if (!$tree) {
			$tree = new Tree($color);
			$treeMap[$color] = $tree;
		}

		return $tree
	}
}

class Client {
	public function install() {
		$factory = new Treefactory();
		$tree = $factory->getTree('red');
		$tree->setX(10);
		$tree->setY(20);
		$tree->install();

		$tree2 = $factory->getTree('red'); // 기존에 생성된 인스턴스가 return됨
		$tree2 = $factory->setX(20);
		$tree2 = $factory->setY(30);

		$tree3 = $factory->getTree('blue'); // 존재하지 않기 때문에 새로운게 생성 되고, treeMap에 저장됨
		$tree3 = $factory->setX(40);
		$tree3 = $factory->setY(50);
	}
}

$client = new Client();
$client->install();
```

참고: https://velog.io/@hoit_98/%EB%94%94%EC%9E%90%EC%9D%B8-%ED%8C%A8%ED%84%B4-Flyweight-%ED%8C%A8%ED%84%B4