# Visitor 패턴
> Visitor pattern, 방문자 패턴, 실제 로직을 가지고 있는 객체(Visitor)가 로직을 적용할 객체(Element)를 방문하면서 실행하는 패턴이다.

### 왜쓰는건데?
- 로직과 구조를 분리하는 패턴으로, 구조를 수정하지 않고도 새로운 동작을 기존 객체 구조에 추가할 수 있다(개방 폐쇄 원칙을 지킬수 있음)

```php
<?php
interface ItemElement {
	public function accept(ShoppingCartVisitor $visitor);
}

class Book implements ItemElement {
	private $price;
	public function __construct($price) {
		$this->price = $price;
	}

	public function accept(ShoppingCartVisitor $visitor) {
		$visitor.visit($this);
	}
}

class Fruit implements ItemElement {
	private $price;
	public function __construct($price) {
		$this->price = $price;
	}

	public function accept(ShoppingCartVisitor $visitor) {
		$visitor.visit($this);
	}
}

interface ShoppingCartVisitor {
	// generic 지원되면 아래처럼 안되서 if else 쓸꺼임
	// public function visit(Book $book);
	// public function visit(Fruit $fruit);
	public function visit($item);
	public function show();
}

class Visitor implements ShoppingCartVisitor {
	private $book;
	private $fruit;
	public function visit($item) {
		if ($item instanceof Book) {
			$book = $item;
		} else if ($item instanceof Fruit) {
			$fruit = $item;
		}
	}

	public function show() {
		echo $this->book . $this->fruit;
	}
}

class Client {
	public function view(){
		$book = new Book(50000);
		$fruit = new Fruit(1000);
		$visitor = new Visitor();
		
		$book->accept($visitor);
		$fruit->accept($visitor);
		$visitor->show();
	}
}

$client = new Client();
$client->view();