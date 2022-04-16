# Decorator

> 구조 패턴으로 객체에 동적으로 기능추가를 하기 위한 패턴

### 왜 쓰는건데?
- 객체에 동적으로 기능추가를 할 수 있다
- 합성 관계를 이용해서 다른 객체를 참조
- 추상 클래스 Decorator를 이용

### 4가지 요소
- Component
	- ConcreteComponent와 Decorator가 구현할 interface
- ConcreteComponent
	- Decorate를 받을 객체 (기능 추가를 받을 기본 객체)
- Decorator
	- Decorate를 할 객체의 추상 클래스 (기능 추가할때 이 객체를 상속받는다)
- ConcreteDecorator
	- Decorate를 상속받아 구현한 다양한 기능의 객체


```php
<?php

// Component
interface ChristmasTree
{
    public function decorate(): string;
}

// ConcreteComponent (제일 기본 객체)
class DefaultChristmasTree implements ChristmasTree
{
    public function decorate(): string
    {
        return 'ChristmasTree';
    }
}

// Decorator
abstract class TreeDecorator implements ChristmasTree
{
    private ChristmasTree $christmasTree;

    public function __construct(ChristmasTree $christmasTree)
    {
        $this->christmasTree = $christmasTree;
    }

    public function decorate(): string
    {
        return $this->christmasTree->decorate();
    }
}

// ConcreteDecorator
class Lights extends TreeDecorator
{
    private $parent;

    public function __construct(ChristmasTree $christmasTree)
    {
        $this->parent = $christmasTree;
    }

    private function addLights(): string
    {
        return ' with Lights';
    }

    public function decorate(): string
    {
        return $this->parent->decorate() . $this->addLights();
    }
}

// ConcreteDecorator2
class Flowers extends TreeDecorator
{
    private $parent;

    public function __construct(ChristmasTree $christmasTree)
    {
        $this->parent = $christmasTree;
    }

    private function addFlowers(): string
    {
        return ' with Flowers';
    }

    public function decorate(): string
    {
        return $this->parent->decorate() . $this->addFlowers();
    }
}

class Main
{
    public function test()
    {
        // 기본 트리
        $tree = new DefaultChristmasTree();
        echo $tree->decorate();
        echo PHP_EOL;

        // 기본트리 + Lights 기능
        $treeWithLights = new Lights(new DefaultChristmasTree());
        echo $treeWithLights->decorate();
        echo PHP_EOL;

        // 기본트리 + Lights 기능 + Flower 기능
        $treeWithLights = new Flowers(new Lights(new DefaultChristmasTree()));
        echo $treeWithLights->decorate();
        echo PHP_EOL;
    }
}

$main = new Main();
$main->test();
```

참고: https://dailyheumsi.tistory.com/198