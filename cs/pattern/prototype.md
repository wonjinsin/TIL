# Prototype

> 생성 패턴으로 prototype으로 사용할 인스턴스를 준비하고, 이를 기반으로 하는 instance들은 이 prototype 인스턴스를 clone해서 사용하도록 하는 패턴

### 왜 쓰는건데?
- 인스턴스를 생성할때마다 DB에서 값을 불러와서(제일 기본이되는) 새로운 인스턴스들을 생성하는 비용이, 미리 prototype을 만들어서 이를 clone해서 사용하는 비용이 적게 들기 때문

```php
<?php

abstract class BookPrototype {
    protected $title;
    protected $topic;
    function getTitle() {
        return $this->title;
    }
    function setTitle($titleIn) {
        $this->title = $titleIn;
    }
    function getTopic() {
        return $this->topic;
    }
}

class PHPBookPrototype extends BookPrototype {
    function __construct() {
        $this->topic = 'PHP';
    }
}

class SQLBookPrototype extends BookPrototype {
    function __construct() {
        $this->topic = 'SQL';
    }
}

writeln('BEGIN TESTING PROTOTYPE PATTERN');
writeln('');

$phpProto = new PHPBookPrototype();
$sqlProto = new SQLBookPrototype();

$book1 = clone $sqlProto;
$book1->setTitle('SQL For Cats');
writeln('Book 1 topic: '.$book1->getTopic());
writeln('Book 1 title: '.$book1->getTitle());
writeln('');

$book2 = clone $phpProto;
$book2->setTitle('OReilly Learning PHP 5');
writeln('Book 2 topic: '.$book2->getTopic());
writeln('Book 2 title: '.$book2->getTitle());
writeln('');

$book3 = clone $sqlProto;
$book3->setTitle('OReilly Learning SQL');
writeln('Book 3 topic: '.$book3->getTopic());
writeln('Book 3 title: '.$book3->getTitle());
writeln('');

writeln('END TESTING PROTOTYPE PATTERN');

function writeln($line_in) {
  echo $line_in."\n";
}

// BEGIN TESTING PROTOTYPE PATTERN

// Book 1 topic: SQL
// Book 1 title: SQL For Cats

// Book 2 topic: PHP
// Book 2 title: OReilly Learning PHP 5

// Book 3 topic: SQL
// Book 3 title: OReilly Learning SQL

// END TESTING PROTOTYPE PATTERN
```