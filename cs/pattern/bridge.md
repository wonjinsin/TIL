# Bridge method

> 구조패턴 중 하나로 각자 독립적으로 변형 및 확장이 가능하도록 기능과 구현을 별도의 클래스로 구현

### Factory method 조건
- Abstraction (기능 추상화 클래스)
	- 추상 클래스 (기능 계층의 최상 클래스)
- RefinedAbstration (기능)
	- 기능 추상클래스를 상속받은 클래스
- Implementation (구현 인터페이스)
	- Abstraction이 실행하는 Interface
- ConcreateImplementor (구현)
	- 실제 기능을 구현하는 클래스

```php
<?php

// Implementation
interface ExerciseHandler {
	public function warmUp();
	public function exercise();
	public function coolDown();
}

// ConcreateImplementor
class LowerBody implements ExerciseHandler {
	public function warmUp()
    {
        echo("하체를 열심히 달군다");
    }
    public function exercise()
    {
        echo("본세트를 임하여 걷지 못 할 정도로 열심히 하체를 찢는다.");
    }
    public function coolDown()
    {
        echo("달군 하체를 차분히 식혀준다.");
    }
}

// ConcreateImplementor
class UpperBodyMethod implements ExerciseHandler {
	public function warmUp()
    {
        echo("상체를 열심히 달군다");
    }
    public function exercise()
    {
        echo("본세트를 임하여 손이 들리지 않을 정도로 열심히 상체를 찢는다.");
    }
    public function coolDown()
    {
        echo("달군 상체를 차분히 식혀준다.");
    }
}

// Abstraction
abstract class Exerciser {
    private $excercise;
    
    public function __construct(ExerciseHandler exerciseHandler)
    {
        $this->excercise = exerciseHandler;
    }
    public function warmUp()
    {
        $this->excercise->warmUp();
    }
    public function exercise()
    {
        $this->excercise->exercise();
    }
    public function coolDown()
    {
        $this->excercise->coolDown();
    }
    public function start();
}

// RefinedAbstration
class OnlyLower extends Exerciser
{
    public function start()
    {
        echo("하체충의 운동은 어떻게?");
    }
}

// RefinedAbstration
public class OnlyUpper extends Exerciser
{
    public function start()
    {
        echo("상체충의 운동은 어떻게?");
    }
}

```