# Iterator 패턴

> 행위패턴으로 컬렉션 구현 방법을 노출시키지 않으면서 집합체에 있는 항목에 접근할 수 있도록 해주는 패턴

### 왜쓰는 건데?
- 집합체 내에서 어떤식으로 일이 처리되는지 몰라도 그 안에 들어있는 항목들에 대하여 반복잡업을 수행할 수 있다.
- 집합체 클래스의 응집도를 높여준다.

### 구조
- Iterator
	- 집합체의 요소들을 순서대로 검색하기 위한 Interface
- ConcreteIterator
	- Iterator 인터페이스 구현
- Aggregate
	- 여러 요소들로 이루어져 있는 집합체
- ConcreteAggregate
	- Aggregate 인터페이스를 구현하는 클래스

```php
<?php

class Book
{
    private $name;

    public function __construct($name)
    {
        $this->name = $name;
    }

    public function __getName()
    {
        return $this->name;
    }
}

// Aggregate
class BookShelf implements \IteratorAggregate
{
    private array $books = [];
    private int $size = 0;
    private int $last = 0;

    public function __construct($size)
    {
        $this->size = $size;
    }

    public function getBook(int $index): Book
    {
        return $this->books[$index];
    }

    public function getLength(): int
    {
        return $this->last;
    }

    public function appendBook(Book $book): void
    {
        if ($this->size > count($this->books)) {
            array_push($this->books, $book);
        } else {
            echo '책꽃이가 꽉 찼습니다!';
        }
    }

    public function getIterator(): BookShelfIterator
    {
        return new BookShelfIterator($this);
    }
}

class BookShelfIterator implements \Iterator
{
    private $collection;
    private int $position = 0;

    public function __construct($collection)
    {
        $this->collection = $collection;
    }

    public function current()
    {
        return $this->collection->getItems()[$this->position];
    }

    public function key()
    {
        return $this->position;
    }

    public function next(): void
    {
        $this->position = $this->position + 1;
    }

    public function rewind(): void
    {
        $this->postion = 0;
    }

    public function valid(): bool
    {
        return isset($this->collection->getItems()[$this->position]);
    }
}

$bookShelf = new Bookshelf(10);
$book1 = new Book('책1');
$book1 = new Book('책2');
$book1 = new Book('책3');

echo sprintf('책 개수: %d권', $bookShelf->getLength());
$bookIterator = $bookShelf->getIterator();
foreach ($bookIterator as $book) {
	echo sprintf('%s', $book->__getName());
}