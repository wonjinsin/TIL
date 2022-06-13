# Factory method

> 생성패턴중 하나로 Factory class가 클라언트가 원하는 구체화된 객체를 선택해서 전달해주는 방식  

### Factory method 조건
- 같은 범위의 구체화된 객체들은 Interface은 실행하거나, 추상클래스를 상속받아야 됨
- Factory가 구체화된 객체를 정해서 전달해줘야 댐
- 가져다 쓰는 객체는 추상화에 의존해야 됨

### 왜 쓰는건데?
- 상위클래스가 구체화된 객체를 몰라도 되지만(추상화에 의존하지만), 작업에는 이상이 없게 됨
```php
<?php
class ComputerStore {
	private $computer;
	public function setComputer($type) {
		if($type == "gram") { // 이짓을 다른 instance가 처리하도록해서 결합도를 낮추기 위해 하는거
			$this->computer = new Gram();
		} else if($type == "mac") {
			$this->computer = new Mac();
		}
	}

	public function showSpec() {
		echo $this->computer->getSpec();
	}
}
```

### 사용 예시
```php
<?php
class ComputerStore {
	private $computer;
	public function setComputer($type) {
		$this->computer = ComputerFactory::getComputer($type); // Factory class가 computer instance 결정
	}

	public function showSpec() {
		echo $this->computer->getSpec();
	}
}

class ComputerFactory {
	// static이 아니여도 됨
	public static function getComputer($type): Computer{
		if($type == "gram") {
			return new Gram();
		} else if($type == "mac") {
			return new Mac();
		}
		return new Gram();
	}
}

abstract class Computer {
	abstract public function getCPU();
	abstract public function getRam();
	abstract public function getPrice();

	public function getSpec() {
		return sprintf("CPU is %s, Ram is %s, Price is %d", $this->getCPU(), $this->getRam(), $this->getPrice());
	}
}

class Gram extends Computer {
	private $cpu;
	private $ram;
	private $price;

	public function __construct() {
		$this->cpu = "gramCPU";
		$this->ram = "gramRam";
		$this->price = 1000000;
	}

	public function getCPU(){
		return $this->cpu;
	}
	public function getRam(){
		return $this->ram;
	}
	public function getPrice(){
		return $this->price;
	}
}

class Mac extends Computer {
	private $cpu;
	private $ram;
	private $price;

	public function __construct() {
		$this->cpu = "macCPU";
		$this->ram = "macRam";
		$this->price = 2000000;
	}

	public function getCPU(){
		return $this->cpu;
	}
	public function getRam(){
		return $this->ram;
	}
	public function getPrice(){
		return $this->price;
	}
}

$store = new ComputerStore();
$store->setComputer("gram");
$store->showSpec(); // CPU is gramCPU, Ram is gramRam, Price is 1000000
```

참고: https://readystory.tistory.com/117?category=822867