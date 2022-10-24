// SPDX-License-Identifier: GPL-3.0

pragma solidity >= 0.5.0 < 0.9.0;

contract lec32 {
	/*
	Payable 
	Payable은 이더/토큰과  상호작용시 필요한 키워드라고 생각하시면 간단합니다. 
	즉, send, trnafer, call을 이용하여, 이더를 보낼때 Payable이라는 키워드가 필요 합니다.
	이 Payable은 주로 함수,주소,생성자에 붙여서 사용된답니다. 
	
	msg.value
	msg.value는 송금보낸 코인의 값 입니다.
	
	이더를 보내는 3가지 
    1.send : 2300 gas를 소비, 성공여부를 true 또는 false로 리턴한다(error를 리턴 못하는 문제가 있음)
    2.transfer : 2300 gas를 소비, 실패시 에러를 발생 (send, call 이후에 생김,제일 많이 쓰임)
    3.call : 가변적인 gas 소비 (gas값 지정 가능), 성공여부를 true 또는 false로 리턴
             재진입(reentrancy) 공격 위험성 있음, 
			 2019년 12월 이후 send와 transfer보다 재진입을 대비할수있는 코드와 함께 call 사용을 추천 (2300gas가 코드를 실행하는데에 부족할수 있어서)
    */

	event howMuch(uint256 _value);
	function sendNow(address payable _to) public payable{ // _to는 스마트 컨트랙트 주소도 가능함, 즉 스마트 컨트랙트도 이더를 받을수 있음
		bool sent = _to.send(msg.value); // return true or false
		require(sent, "Failed to send either");
		emit howMuch(msg.value);
	}

	function transferNow(address payable _to) public payable {
		_to.transfer(msg.value); // 여기 자체내에서 error return 함
		emit howMuch(msg.value);
	}

	function callNow (address _to) public payable {
		// ~ 0.7 0.7 버전 이전 문법
		// (bool sent, ) = _to.call.gas(1000).value(msg.value)("");
		// require(sent, "Failed to send either");

		// 0.7 ~ 0.7버전 이후 문법
		(bool sent, ) = _to.call{value: msg.value , gas:1000}(""); // gas 저렇게 지정할수 있는데, 안하는게 좋음 가스가 부족할수 있으니까
		require(sent, "Failed to send either");
		
		emit howMuch(msg.value);
	}
}