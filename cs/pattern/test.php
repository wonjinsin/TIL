<?php

class ComputerStore {
	private $instance;

	static public function getInstance() {
		if (self::$instance === null) {
			self::$instance = new ComputerStore();
		}
		return self::$instance;
	}

	public function setString($string) {
		return $this->string = $string;
	}

	public function getString() {
		return $this->string;
	}
}

$instance = ComputerStore::getInstance();
$instance->setString('test1');
echo $instance->getString();

$instance2 = ComputerStore::getInstance();
$instance2->setString('test2');

echo $instance->getString(); // test2
echo $instance2->getString(); // test2