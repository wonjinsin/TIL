# Singleton

> 자원 공유를 위해서 객체를 한개만 생성하고, 이를 공유해서 사용하는 패턴

### 왜 쓰는건데?
- DB 커넥터나 Logging처럼 하나의 클래스에 하나의 객체만이 존재해서, 이를 여러군데에서 공유해서 사용하게끔 하는게 효율적인 경우를 위해 사용

### 사용 예시
```php
<?php
class ComputerStore {
	private $instance;

	static public function getInstance() {
		if (self::$instance === null) {
			self::$instance = new ComputerStore();
		}
		return self::$instance;
	}

	public function setString($string) {
		return $this->string = $string;
	}

	public function getString() {
		return $this->string;
	}
}

$instance = ComputerStore::getInstance();
$instance->setString('test1');
echo $instance->getString();

$instance2 = ComputerStore::getInstance();
$instance2->setString('test2');

echo $instance->getString(); // test2
echo $instance2->getString(); // test2
```
