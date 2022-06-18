# Starategy

> 행위 패턴으로, 특정 동작들 자체를 인터페이스화 하고 이에 대한 객체(전략)들을 만든 후에, 이를 이용하는 객체들은 이 전략을 이용해서 동적으로 행동할 수 있도록 하는 패턴

### 왜 쓰는건데?
- 아래와 같은 경우에 OCP(Open-Closed principle)을 위반하고, 중복되는 method가 계속 생김.
- 날으는 차가 생긴다고 가정하면, Car의 move ground라는 항목 자체를 바꿔야 함
- Bike가 생기면 move ground라는 중복되는 method 만들어서 써야 됨
```php
<?php
interface Movable {
	public function move()
}

class Car implements Movable {
	public function move() {
		echo 'move ground';
	}
}

class Airplane implements Movable {
	public function move() {
		echo 'move air';
	}
}
```

### 사용 예시
```php
<?php
interface Transportation {
	public function move()
}

interface MoveStrategy {
	public function move()
}

class GroundStrategy implements MoveStrategy {
	public function move() {
		echo 'move ground';
	}
}

class AirStrategy implements MoveStrategy {
	public function move() {
		echo 'move air';
	}
}

class Car implements Transportaion {
	private $strategy;
	public function __construct(MoveStrategy $strategy) {
		$this->strategy = $strategy;
	}
	public function move() {
		return $this->strategy->move();
	}
}

class Airplane implements Transportaion {
	private $strategy;
	public function __construct(MoveStrategy $strategy) {
		$this->strategy = $strategy;
	}
	public function move() {
		return $this->strategy->move();
	}
}

$groundStrategy = new GroundMoveStrategy();
$airStrategy = new GroundMoveStrategy();
$car = new Car($groundStrategy);
$airplane = new Airplane($airStrategy);
$car->move(); // move ground
$airplne->move(); // move air