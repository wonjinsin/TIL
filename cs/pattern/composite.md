# Command

> 구조 패턴으로 전체-부분의 관계를 갖는 객체들 사이의 관계를 정의할때 유용
> 클라이언트는 전체와 부분을 구분하지 않고 동일한 인터페이스를 사용할 수 있다

### 왜 쓰는건데?
- 전체-부분의 관계에서 OCP를 만족하지 않고, 확장성이 좋지 않음
```php
<?php
class Keyboard {
	private $price;
	private $power;

	public function __construct($price, $power) {
		$this->price = $price;
		$this->power = $power;
	}

	public function getPrice() {
		return $this->price;
	}

	public function getPower() {
		return $this->power;
	}
}

class Mouse {
	private $price;
	private $power;

	public function __construct($price, $power) {
		$this->price = $price;
		$this->power = $power;
	}

	public function getPrice() {
		return $this->price;
	}

	public function getPower() {
		return $this->power;
	}
}

class Computer {
	private $keyboard;
	private $mouse;

	public function addKeyBoard($keyboard) {
		$this->keyboard = $keyboard;
	}

	public function addMouse($mouse) {
		$this->mouse = $mouse;
	}

	public function getPrice() {
		return $this->keyboard->getPrice() + $this->mouse->getPrice();
	}

	public function getPower() {
		return $this->keyboard->getPower() + $this->mouse->getPower();
	}
}

class Client {
	public function calculate() {
		$keyboard = new Keyboard(100000, 300);
		$mouse = new Mouse(50000, 100);

		$computer = new Computer();
		$computer->addKeyBoard($keyboard);
		$computer->addMouse($keyboard);

		echo $computer->getPrice();
		echo $computer->getPower();
	}
}

$client = new Client();
$client->calculate();
```
- 다른 computer 부품이 추가될때 마다 Computer가 바뀌여야함, OCP 위반 

### 3가지 요소
- Component
	- 공통으로 쓰이는 인터페이스
- Leaf
	- 구체적인 부분 클래스
	- Composite 객체의 부품으로 설정
	- ex) keyboard, mouse
- Composite
	- 전체 클래스
	- 복수의 Leaf, 혹은 복수의 Composite도 가질수 있음

```php
<?php

interface Component {
	public function getPrice();
	public function getPower();
}

class Keyboard implements Component {
	private $price;
	private $power;

	public function __construct($price, $power) {
		$this->price = $price;
		$this->power = $power;
	}

	public function getPrice() {
		return $this->price;
	}

	public function getPower() {
		return $this->power;
	}
}

class Mouse implements Component {
	private $price;
	private $power;

	public function __construct($price, $power) {
		$this->price = $price;
		$this->power = $power;
	}

	public function getPrice() {
		return $this->price;
	}

	public function getPower() {
		return $this->power;
	}
}

class Computer implements Component {
	private $components;

	public function addComponent($component) {
		array_push($this->components, $component);
	}

	public function getPrice() {
		$price = 0;
		foreach ($components => $component) {
			$price += $component->getPrice();
		}
		return $price
	}

	public function getPower() {
		$power = 0;
		foreach ($components => $component) {
			$power += $component->getPower();
		}
		return $power
	}
}

class Client {
	public function calculate() {
		$keyboard = new Keyboard(100000, 300);
		$mouse = new Mouse(50000, 100);

		$computer = new Computer();
		$computer->addComponent($keyboard);
		$computer->addComponent($mouse);

		echo $computer->getPrice();
		echo $computer->getPower();
	}
}

$client = new Client();
$client->calculate();
```

참고: https://gmlwjd9405.github.io/2018/08/10/composite-pattern.html