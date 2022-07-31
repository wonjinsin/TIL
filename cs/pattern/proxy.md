# Proxy 패턴

> 구조패턴으로 Proxy는 우리말로 대리자, 대변인 이라는 뜻입니다. 대리자, 대변인은 다른 누군가를 대신해서 그 역할을 수행하는 존재입니다. 프로그램에서 봤을 때도 똑같습니다. 프록시에게 어떤 일을 대신 시키는 것입니다. 

### 왜쓰는건데?
- 구체적으로 인터페이스를 사용하고 실행시킬 클래스에 대한 객체가 들어갈 자리에 대리자 객체를 대신 투입해 클라이언트 쪽에서 실제 실행시킬 클래스에 대한객체를 통해 메서드를 호출하고 반환 값을 받는지, 대리자 객체를 통해 메서드를 호출하고 반환 값을 받는지 전혀 모르게 처리하는 것입니다. 
- 일종의 프록시는 비서역할을 하는 것 같네요. 중요한 것은 흐름제어만 할 뿐 결과값을 조작하거나 변경시키면 안됩니다.
- 예를 들어, 큰 이미지를 로딩할때 해당 이미지를 기다리는건 너무 오래걸려서 로딩창 같은걸 띄워놓고, 프록시가 작동하도록 만들수 있음

### 구조
- Subject
	- interface
- realConcreteService
	- Subject를 실행하고, proxy로 부터 실행됨
- proxyConcreteSubject
	- realConcreteService를 실행

```php
<?php
public interface Image {
    public function displayImage();
}

class RealImage extends Image {
	$this->filename = $filename;
	public function __construct(string $filename) {
		$this->filename = $filename;
		$this->loadFromDisk($filname);
	}

	private function loadFromDisk(string $filename) {
		echo sprintf('Loading %s', $filename);
	}

	public function displayImage(string $filename) {
		echo sprintf('Displaying %s', $filename);
	}
}

class ProxyImage implements Image {
	private $realImage;
    private $fileName;

    public function __construct(string $fileName) {
        $this->fileName = $fileName;
    }

    public function displayImage() {
        $realImage = new RealImage($this->fileName);
		$realName->displayImage();
    }
}

$image1 = new ProxyImage("test1.png");
$image2 = new ProxyImage("test2.png");
$image1->displayImage();
$image2->displayImage();