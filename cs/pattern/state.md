# State 패턴
> 행위 패턴으로 스테이트 패턴은 객체가 특정 상태에 따라 행위를 달리하는 상황에서, 자신이 직접 상태를 체크하여 상태에 따라 행위를 호출하지 않고, 상태를 객체화 하여 상태가 행동을 할 수 있도록 위임하는 패턴을 말합니다.

```php
<?php
interface PowerState {
    public function powerPush();
}

class On implements PowerState {
	public function powerPush() {
		echo '전원 On';
	}
}

class Off implements PowerState {
	public function powerPush() {
		echo '전원 Off';
	}
}

class Saving implements PowerState {
	public function powerPush() {
		echo 'Saving';
	}
}

class Laptop {
	private $powerState;
	public function __construct() {
		$this->powerState = new Off();
	}

	public function setPowerState(PowerState $powerState) {
		$this->powerState = $powerState;
	}

	public function powerPush() {
		$this->powerState->powerPush();
	}
}

$on = new On();
$off = new Off();
$saving = new Saving();

$lapTop = new Laptop();
$lapTop->setPowerState($on);
$lapTop->powerPush(); // 전원 On
$lapTop->setPowerState($saving);
$lapTop->powerPush(); // Saving
$lapTop->setPowerState($off);
$lapTop->powerPush(); // 전원 Off
