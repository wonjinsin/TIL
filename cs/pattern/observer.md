# Observer 패턴

> 행위 패턴으로 객체 사이에 일 대 다의 의존 관계를 정의해 두어, 어떤 객체의 상태가 변할 때 그 객체에 의존성을 가진 다른 객체들이 그 변화를 통지받고 자동으로 갱신될 수 있게 만드는 패턴이다.
> 주체가 되는 객체와 이를 구독하는 객체가 1:N으로 매핑

### 구조
- Subject
	- Observer가 이용하는 interface
- Observer
	- Subject에서 변화했다고 알렸을때, 갱신해야하는데 필요한 인터페이스를 정의
- ConcreteSubject
	- Subject interface를 실행하고, 객체에게 알려줘야할 상태를 저장하고, notify 해야할 함수를 가지고 있는 Subject
- ConcreteObserver
	- Observer interface를 실행하고, noti를 받았을떄 행동할 로직을 작성합니다.

```php
<?php
public interface Observer {
    public function noti();
    public function getTitle();
}

class Client1 implements Observer {
    private $title;
    public function __construct(string $title) {
        $this->title = $title;
    }
    public function noti() {
        echo sprintf('클라이인트 %s에 변경사항이 반영됨');
    }

    public function getTitle() {
        echo $this->title;
    }

}

class Client2 implements Observer {
    private $title;
    public function __construct(string $title) {
        $this->title = $title;
    }
    public function noti() {
        echo sprintf('클라이인트 %s에 변경사항이 반영됨');
    }
    
    public function getTitle() {
        echo $this->title;
    }
}

interface Subject {
    public function attach(Observer $observer);
    public function detach(Observer $observer);
    public function notifyObserver();
}

class ConcreteSubject implements Subject {
    private $clients;

    public function attach(Observer $observer) {
        $this->clients[$observer->getTitle()] = $observer;
    }

    public function detach(Observer $observer) {
        unset($this->clients[$observer->getTitle()]);
    }

    public function notifyObserver() {
        foreach ($this->clients as $client) {
            $client->noti();
        }
        echo '[Subject] 메세지를 전송하였습니다.';
    }
}


$subject = new ConcreteSubject();
$client1 = new Client1('유저 1');
$client2 = new Client2('유저 2');

$subject->attach($client1);
$subject->attach($client2);
$subject->notifyObserver();