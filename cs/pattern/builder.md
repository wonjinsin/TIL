# Builder

> 생성패턴중 하나로 setter를 이용해서 새로운 객체를 전달해주는 방식  

### Builder pattern 조건
- Builder class의 setMethod의 경우 자기 자신을 return 해야함

### 왜 쓰는건데?
- Setter를 이용해서 생성을 하기 떄문에 생성자의 parameter를 직접 넣는게 아니라 동적으로 만들 수 있음
```php
<?php
// 아래와 같은 경우 타입, 순서등이 다르기 떄문에 관리가 쉽지 않고 에러가 날 확률이 높음
$computer = new Computer('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i');
```

### 사용 예시
```php
<?php
class Computer {
	private $hdd;
	private $ram;
	private $graphicCard;

	public function setHDD($hdd) {
		$this->hdd = $hdd;
	}

	public function setRam($ram) {
		$this->ram = $ram;
	}

	public function setGraphicCard($graphicCard) {
		$this->graphicCard = $graphicCard;
	}

	public function getHDD() {
		return $this->hdd;
	}

	public function getRam() {
		return $this->ram;
	}

	public function getRam() {
		return $this->graphicCard;
	}
}

class ComputerBuilder {
	private $hdd;
	private $ram;
	private $graphicCard;

	public function setHDD($hdd) {
		$this->hdd = $hdd;
	}

	public function setRam($ram) {
		$this->ram = $ram;
	}

	public function setGraphicCard($graphicCard) {
		$this->graphicCard = $graphicCard;
	}

	// 이렇게 안하고, new Computer($hdd, $ram, $graphicCard), new Computer($this) 같이 쓰기도 함
	public function build() {
		$computer = new Computer();
		$computer->setHDD($this->hdd);
		$computer->setRam($this->ram);
		$computer->setGraphicCard($this->graphicCard);
		return $computer;
	}
}

$computer = new ComputerStore()->setHDD('512')->setRam('128')->setGraphicCard('3080')->build();
```

참고: https://readystory.tistory.com/117?category=822867