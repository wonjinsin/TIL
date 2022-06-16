# Chain of responsibility

> 행동 패턴중 하나로 클라이언트의 요청을 처리하기 위해 여러 객체가 필요한 경우, 여러 객체를 체인으로 불러서 이를 처리
Request --> Handler --> Handler --> Handler --> Ordering system
				|			|			|
				|			|			|
				|			|			|
			   Stop		   Stop		   Stop
### 실제 Chain of responsibility
- 각각의 Handler가 다음 Handler를 알고 있어서, 이를 처리

### 사용 예시
```php
<?php

interface withdrawChain
{
    public function setNext(withdrawChain $next);

    public function withdraw();
}

class chunwonWithdraw implements withdrawChain
{
    private $next;

    public function setNext(withdrawChain $next)
    {
        $this->next = $next;
    }

    public function withdraw()
    {
        echo '천원 인출';
        if ($this->next) {
            return $this->next->withdraw();
        }
        echo '끝!';
    }
}

class manwonWithdraw implements withdrawChain
{
    private $next;

    public function setNext(withdrawChain $next)
    {
        $this->next = $next;
    }

    public function withdraw()
    {
        echo '만원 인출';
        if ($this->next) {
            return $this->next->withdraw();
        }
        echo '끝!';
    }
}

class ohmanwonWithdraw implements withdrawChain
{
    private $next;

    public function setNext(withdrawChain $next)
    {
        $this->next = $next;
    }

    public function withdraw()
    {
        echo '5만원 인출';
        if ($this->next) {
            return $this->next->withdraw();
        }
        echo '끝!';
    }
}

$ohmanwonWithdraw = new ohmanwonWithdraw();
$manwonWithdraw = new manwonWithdraw();
$chunwonWithdraw = new chunwonWithdraw();

$ohmanwonWithdraw->setNext($manwonWithdraw);
$manwonWithdraw->setNext($chunwonWithdraw);
$ohmanwonWithdraw->withdraw(); // 5만원 인출 만원 인출 천원 인출 끝!
```

참고: https://k0102575.github.io/articles/2020-02/chain-of-responsibility-pattern, https://brownbears.tistory.com/552