# TemplateMethod 패턴
> 생성패턴으로 템플릿 메소드 패턴은 여러 작업들이 완전히 동일한 단계를 갖지만, 일부 동작은 각각 다르게 구현해야할 때 사용되는 패턴이다.

```php
<?php
abstract class teacher {
    public function start_class() {
		$this->inside();
		$this->attendance();
		$this->teach();
		$this->outside();
	}

	public function inside() {
		echo '선생님이 들어오신다';
	}

	public function attendance() {
		echo '선생님이 출석을 부릅니다';
	}
	
	abstract public function teach() {}
	
	public function outside() {
		echo '선생님이 나가십니다';
	}
}

class KoreanTeacher extends teacher {
	public function teach() {
		echo '국어를 가르킵니다.';
	}
}

class EnglishTeacher extends teacher {
	public function teach() {
		echo '영어를 가르킵니다.';
	}
}

class MathTeacher extends teacher {
	public function teach() {
		echo '수학을 가르킵니다.';
	}
}

$kr = new KoreanTeacher();
$en = new EnglishTeacher();
$math = new MathTeacher();

$kr->start_class();
$en->start_class();
$math->start_class();