# Memento 패턴

> 객체의 상태 정보를 가지는 클래스를 따로 생성하여, 객체의 상태를 저장하거나 이전 상태로 복원할 수 있게 해주는 행위 패턴
> 원하는 시점의 상태 복원이 가능하다(실행취소 같은 기능).

### 구조
- Memento
	- Originator의 State들을 가지고 있는 객체
- Originator
	- 현재의 state를 저장하는 Memento 객체를 생성할 수 있음
- CareTaker
	- Memento 객체들을 저장하여 Originator의 동작을 추적

### 단점
- Memento를 너무 많이 생성하면 메모리가 많이 사용됨

```php
<?php
class Originator {
	private string $state
	
	public function __construct(string $state) {
		$this->state = $state;
	}

	public function getState() {
		return $this->state;
	}

	public function saveStateToMemento() {
		return new Memento($this->state);
	}

	public function getStateFromMemento(Memento $memento) {
		$this->state = $memento->getState();
	}
}

class Memento {
	private string $state
	
	public function __construct(string $state) {
		$this->state = $state;
	}

	public function getState() {
		return $this->state;
	}
}

public class CareTaker {
	private array $mementoList;

	public function add(Mediator $memento) {
		return array_push($this->mementoList, $memento);
	}

	public function get(int $index) {
		return $this->mementoList->get($index);
	}
}

$originator = new Originator();
$careTaker = new CareTaker();
$originator->setState("State #1");
$originator->setState("State #2");
$careTaker->add($originator->saveStateToMemento());
$originator->setState("State #3");
$careTaker->add($originator->saveStateToMemento());
$originator->setState("State #4");

echo "Current State: " . $originator->getState());
$originator->getStateFromMemento($careTaker->get(0));
echo "First saved State: " . $originator->getState());
$originator->getStateFromMemento($careTaker->get(1));
echo "Second saved State: " . $originator->getState());