# Interpreter 패턴

> 문법 규칙을 클래스화 한 구조로, 일련의 규칙으로 정의된 문법적 언어를 해석하는 패턴입니다.(SQL, SHELL...) 인터프리터 패턴은 SQL과 같은 계층적 언어를 해석하기 위해 계층 구조를 표현할 수 있습니다.

### 구조
- AbstractExpression
	- interpret을 정의
- TerminalExpression
	- interpret을 구현
- NonTerminalExpression
	- NonTermianl의 interpret을 구현, TerminalExpression을 가지고 interpret을 하는 역할
- Client
	- interpret을 호출

```php
<?php

interface Expression {
	public function interpreter(string $con);
}

class TerminalExpression implements Expression {
	private string $data;

	public function __construct(string $data) {
		$this->data = $data;
	}

	public function interpret(string $con) {
		if (strpos($this->data, $con) !== false) {
			return true;
		}
		return false;
	}
}

class OrExpression implements Expression {
	private Expression $person1;
	private Expression $person2;

	public function __construct(Expression $person1, Expression $person2) {
		$this->person1 = $persion1;
		$this->person2 = $persion2;
	}

	public function interpreter(string $con) {
		return $this->persion1->interpret($con) || $this->persion2->interpret($con);
	}
}

class AndExpression implements Expression {
	private Expression $person1;
	private Expression $person2;

	public function __construct(Expression $person1, Expression $person2) {
		$this->person1 = $persion1;
		$this->person2 = $persion2;
	}

	public function interpreter(string $con) {
		return $this->persion1->interpret($con) && $this->persion2->interpret($con);
	}
}

class Client {
	public function run() {
		$person1 = new TerminalExpression('Tom');
		$person2 = new TerminalExpression('Tommy');
		$isExistOneInPeople = new OrExpression($person1, $person2);
		$isExistToAllPeople = new AndExpression($person1, $person2);

		echo $isExistOneInPeople->interpret('Tommy'); // true
		echo $isExistToAllPeople->interpret('Tommy'); // false
	}
}