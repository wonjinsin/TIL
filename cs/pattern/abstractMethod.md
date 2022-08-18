# AbstractMethod 패턴
> 생성패턴으로 인터페이스를 이용하여 서로 연관된, 또는 의존하는 객체들을 구상 클래스를 지정하지 않고도 생성하는 패턴

### 4가지 요소
- AbstractFactory
	- 실제 생성할 Product들을 규정
- AbstractProduct
	- Factory를 통해 성생하는 Product들
- ConcreteFactory
	- AbscractFactory를 구현
- ConcreteProduct
	- AbstractProduct를 구현

```php
<?php
// AbstractFactory
interface GUIFactory {
	public function createButton();
	public function createText();
}

//AbstractProduct
interface Button {
	public function clickButton();
}

//AbstractProduct
interface Text {
	public function textDescription();
}

// ConcreteFactory
class WindowGUIFactory implements GUIFactory {
	public function createButton() {
		return new WindowButton();
	}
	
	public function createText() {
		return new WindowText();
	}
}

// ConcreteFactory
class MacGUIFactory implements GUIFactory {
	public function createButton() {
		return new MacButton();
	}
	
	public function createText() {
		return new MacText();
	}
}

// ConcreteProduct
class WindowButton implements Button {
	public function clickButton() {
		echo '윈도우 버튼 클릭';
	}
}

// ConcreteProduct
class WindowText implements Text {
	public function textDescription() {
		echo '윈도우 텍스트';
	}
} 

// ConcreteProduct
class MacButton implements Button {
	public function clickButton() {
		echo '맥 버튼 클릭';
	}
}

// ConcreteProduct
class MacText implements Text {
	public function textDescription() {
		echo '맥 텍스트';
	}
}

class Main {
	public function __construct() {
		$windowFactory = new WindowGUIFactory();
		$this->printFactory($windowFactory);

		$macFactory = new MacGUIFactory();
		$this->printFactory($macFactory);
	}

	public function printFactory(GUIFactory $factory) {
		$button = $factory->CreateButton();
		$text = $factory->CreateText();

		$button->clickButton();
		$button->textDescription();
	}
}