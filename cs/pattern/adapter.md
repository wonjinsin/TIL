# Adapter

> 구조 패턴으로, 호환되지 않는 `인터페이스`로 인해 같이 사용될 수 없는 클래스들이 같이 사용될 수 있도록 하기 위한 패턴

```php
<?php

interface Worker {
	public function doWork(): string;
}

interface Developer {
	public function writeCode(): string;
}

class Employee implements Worker {
	private $developer;

	public function __construct(Developer $developer) {
		$this->developer = $developer;
	}

	public function doWork(): string{
		return $this->developer->writeCode();
	}
}

class EmployeeDeveloper implements Developer {
	public function writeCode(): string {
		return 'writeCode';
	}
}

class Employer {
	private $employee;

	public function __construct() {
		$this->employee = new Employee(new EmployeeDeveloper());
	}

	public function makeWork() {
		return $this->employee->doWork();
	}
}


$employer = new Employer();
echo $employer->makeWork(); // write code
```