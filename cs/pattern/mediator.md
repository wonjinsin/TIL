# Mediator 패턴

> 중재자 패턴은 클래스 간의 복잡한 관계들을 캡슐화하여 하나의 클래스에서 관리하도록 처리하는 패턴입니다. M:N 관계를 해당 패턴을 사용하면 M:1 관계로 만들어 복잡도를 내리므로 유지 보수 및 확장성에 유리합니다.
> M개의 객체들 사이에 중재자를 추가하여 중재자가 모든 객체들의 통신을 담당하도록 변경하면 중재자 패턴이라 볼 수 있습니다. 이와 같이 진행하면 각 객체들은 서로 알 필요가 없고 중재자 클래스가 관리하므로 느슨한 결합(loose coupling)을 유지할 수 있고 전체적인 흐름을 읽기 편해집니다.

### 구조
- Mediator
	- Colleague 객체 간의 상호참조를 위한 인터페이스. 클라이언트 등록, 실행 등의 메소드 정의
- ConcreteMediator
	- Mediator 구현 클래스. Colleague 간의 상호참조를 조정
- Colleague
	- 다른 Colleague와의 상호참조를 위한 인터페이스
- ConcreteColleage
	- Colleague 구현 클래스. Mediator를 통해 다른 Colleague와의 상호참조

```php
<?php

interface Mediator {
	public function addUser(Colleague $user);
	public function deleteUser(Colleague $user);
	public function sendMessage(Colleague $user);
}

public abstract class Collegue {
	protected Mediator $mediator;
	protected string $name;

	public function __construct(Mediator $mediator, string $name) {
		$this->mediator = $mediator;
		$this->name = $name;
	}

	abstract public function getName();
	abstract public function send(string $msg);
	abstract public function receive(string $msg);
}

class ConcreteMediator implements Mediator {
	private $users;

	public function __construct() {
		$this->users = [];
	}

	public function addUser(Colleague $user) {
		$this->users[$user->getName()] = $user;
	}

	public function deleteUser(Colleague $user) {
		unset($this->users[$user->getName()]);
	}

	public function sendMessage(string $message, Colleague $user) {
		foreach ($this->users as $u) {
			if ($user != $u) {
				$u.receive($message);
			}
		}
	}
}

class ConcreteCollegue implements Collegue {
	private Mediator $mediator;
	private string $name;

	public function __construct(Mediator $mediator, string $name) {
		$this->mediator = $mediator;
		$this->name = $name;
	}

	public function send(string $msg) {
		echo sprintf('%s: Sending Message=%s', $this->name, $msg);
		$this->mediator->sendMessage($msg, $this);
	}

	public function receive(string $msg) {
		echo sprintf('%s: Received Message=%s', $this->name, $msg);
	}
}

Mediator mediator = new ConcreteMediator();
Colleague user1 = new ConcreteColleague(mediator, "lee");
Colleague user2 = new ConcreteColleague(mediator, "kim");
Colleague user3 = new ConcreteColleague(mediator, "park");
Colleague user4 = new ConcreteColleague(mediator, "yon");
mediator.addUser(user1);
mediator.addUser(user2);
mediator.addUser(user3);
mediator.addUser(user4);

user1.send("안녕하세요");
// lee: Sending Message=안녕하세요
// kim: Received Message:안녕하세요
// park: Received Message:안녕하세요
// yon: Received Message:안녕하세요

mediator.deleteUser(user4);

user2.send("yon없지?");
// kim: Sending Message=yon없지?
// lee: Received Message:yon없지?
// park: Received Message:yon없지?