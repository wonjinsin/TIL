# Command

> 행위 패턴으로 이벤트가 동적으로 바뀔수 있을때 사용할 수 있는 패턴으로, 행위 자체(메소드)를 객체로 만들어 이를 참조하게 하는 패턴

### 왜 쓰는건데?
- 객체에 직접 접근해서 행동을 하게하면, OCP에 위배되고 method에서 분기가 늘어남
```php
<?php
class Heater {
	public function powerOn() {
		echo 'Heater on';
	}
}

class Lamp {
	public function turnOn() {
		echo 'turn on';
	}
}

class OkGoogle {
	private $heater;
	private $lamp;

	public function __construct() {
		$this->heater = new Heater();
		$this->lamp = new Lamp();
	}

	public function setMode(string $mode) {
		$this->mode = $mode;
	}

	// 기능 많아 질수록 property 늘어남
	public function talk() {
		switch ($this->mode) {
			case 'heater':
				$this->heater->powerOn();
			case 'lamp':
				$this->lamp->turnOn();
		}
	}
}

$okGoogle = new OkGoogle();
$okGoogle->setMode('heater');
$okGoogle->talk();

$okGoogle->setMode('lamp');
$okGoogle->talk();
```

### 4가지 요소
- Invoker
	- 기능을 호출하는 클래스
- Command
	- 실행될 기능에 대한 인터페이스
- ConcreteComponent
	- Command 인터페이스를 구현
- Receiver
	- ConcreteCommand에서 execute 메서드를 구현할 때 필요한 클래스

```php
<?php

interface Command {
	public function execute();
}

class HeaterCommand implements Command {
	private $heater;
	public function __construct($heater) {
		$this->heater = $heater;
	}
	public function execute() {
		return $this->heater->powerOn();
	}
}

class LampCommand implements Command {
	private $lamp;
	public function __construct($lamp) {
		$this->lamp = $lamp;
	}
	public function execute() {
		return $this->lamp->turnOn();
	}
}


class Heater {
	public function powerOn() {
		echo 'Heater on';
	}
}

class Lamp {
	public function turnOn() {
		echo 'turn on';
	}
}

class OkGoogle {
	private $command;

	public function setCommand($command) {
		$this->command = $command;
	}

	// 기능 많아 질수록 property 늘어남
	public function talk() {
		$this->command->execute();
	}
}

$heater = new Heater();
$lamp = new Lamp();
$heaterCommand = new HeaterCommand($this->heater);
$lampCommand = new LampCommand($this->lamp);

$okGoogle = new OkGoogle();
$okGoogle->setCommand($heaterCommand);
$okGoogle->talk();

$okGoogle->setCommand($lampCommand);
$okGoogle->talk();
```

참고: https://dailyheumsi.tistory.com/198