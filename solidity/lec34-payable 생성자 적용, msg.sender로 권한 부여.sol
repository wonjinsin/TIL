// SPDX-License-Identifier: GPL-3.0

pragma solidity >=0.7.0 < 0.9.0;

/*
payable을 생성자에 넣을때
특정 주소에게만 권한 주기
*/

contract MobileBanking{
	address owner;// smart contract 주소
	constructor() payable { // Deploy 할때 value(이더) 넣고 배포하면 알아서 스마트 컨트랙트 주소에 이더가 들어감  
		 owner = msg.sender; 
	}

	modifier onlyOwner {
		require(msg.sender == owner, "Only Owner!");
		_;
	}
    
    event SendInfo(address _msgSender, uint256 _currentValue);
    event MyCurrentValue(address _msgSender, uint256 _value);
    event CurrentValueOfSomeone(address _msgSender, address _to,uint256 _value);
   
    function sendEther(address payable _to) public onlyOwner payable {
        require(msg.sender.balance>=msg.value, "Your balance is not enough");
        _to.transfer(msg.value);    
        emit SendInfo(msg.sender,(msg.sender).balance);
    }
    
    function checkValueNow() public{
        emit MyCurrentValue(msg.sender, msg.sender.balance);
    }
    
    function checkUserMoney(address _to) public{
        emit CurrentValueOfSomeone(msg.sender, _to ,_to.balance);
    }
}