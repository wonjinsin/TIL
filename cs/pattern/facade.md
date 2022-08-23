# Facade 패턴
> 구조패턴으로 어떤 서브시스템의 일련의 인터페이스에 대한 통합된 인터페이스를 제공한다. 퍼사드에서 고수준 인터페이스를 정의하기 때문에 서브시스템을 더 쉽게 사용할수 있다.

### 왜쓰는건데?
- 복잡한 소프트웨어 바깥쪽의 코드가 라이브러리의 안쪽 코드에 의존하는 일을 감소시켜 주고, 복잡한 소프트웨어를 사용 할 수 있게 간단한 인터페이스를 제공해줍니다.

### 4가지 요소
- Client
	- Facade 패턴을 실행하는 역할 (Facade에게 특정 행동을 실행해달라고 요청)
- Facade
	- 클라이언트의 요청을 적절한 서브시스템 클래스에 위임
- Subsystem class
	- 서브시스템 기능을 구현. facade에 의해서만 실행됨

```php
<?php
class RemoteControl {
	public function turnOn() {
		return print('TV를 켜다');
	}

	public function turnOff() {
		return print('TV를 끄다');
	}
}

class Movie {
	private $name;
	public function __construct($name = '') {
		$this->name = $name;
	}

	public function searchMovie() {
		return print(sprintf('%s 영화를 찾다', $this->name));
	}

	public function chargeMovie() {
		return print('영화를 결제하다');
	}

	public function playMovie() {
		return print('영화를 재생하다');
	}
}

class Beverage {
	private $name;
	public function __construct($name = '') {
		$this->name = $name;
	}

	public function prepare() {
		return print(sprintf('%s 음료 준비완료', $this->name));
	}
}

class Facade {
	private $beverage;
	private $movieName;

	public function __construct($beverage = '', $movieName = '') {
		$this->beverage = $beverage;
		$this->movieName = $movieName;
	}

	public function viewMovie() {
		$beverage = new Beverage($this->beverage);
		$remoteControl = new RemoteControl();
		$movie = new Movie($this->movieName);

		$beverage->prepare();
		$remoteControl->turnOn();
		$movie->searchMovie();
		$movie->chargeMovie();
		$movie->playMovie();
	}
}

class Client {
	public function view(){
		$facade = new Facade('콜라', '어벤져스');
		$facade->viewMovie();
	}
}

$client = new Client();
$client->view();