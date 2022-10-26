// SPDX-License-Identifier: GPL-3.0

pragma solidity >=0.7.0 < 0.9.0;
/*
call :로우레벨 함수 
1. 송금하기
2. 외부 스마트 컨트랙 함수 부르기 
3. 가변적인 gas
4. 이스탄불 하드포크, 2019년 12월이후 function들을 실행하기 위한 gas의 가격 상승 때문에, fallback 함수까지 동작하는데 2300gas를 초과하는 경우가 생김, call 사용 권장/ send tranfer = 2300gas 
5. re-entrancy(재진입) 공격위험 있기에, Checks_Effects_Interactions_pattern 사용  
*/



contract add{
    event JustFallback(string _str);
    event JustReceive(string _str);
    function addNumber(uint256 _num1, uint256 _num2) public pure returns(uint256){
        return _num1 + _num2;
    }
    fallback() external payable  {
     emit JustFallback("JustFallback is called");
    }
    receive() external payable {
     emit JustReceive("JustReceive is called");
    }
}

contract caller{
    event calledFunction(bool _success, bytes _output);
   
    //1. 송금하기 
    function transferEther(address payable _to) public payable{
        (bool success,) = _to.call{value:msg.value}("");
        require(success,"failed to transfer ether");
    }
    
    //2. 외부 스마트 컨트랙 함수 부르기 
    function callMethod(address _contractAddr,uint256 _num1, uint256 _num2) public{

		// success 인지, call한 function의 output
        (bool success, bytes memory outputFromCalledFunction) = _contractAddr.call( // ether 안보내고 외부 함수만 부르니까 fallback 불림
			// abi란 이더리움의 contracts들 사이에 상호작용 하기위한 방법
             abi.encodeWithSignature("addNumber(uint256,uint256)",_num1,_num2)
            );
              
        require(success,"failed to transfer ether");
        emit calledFunction(success,outputFromCalledFunction);
    }
    
    function callMethod3(address _contractAddr) public payable{
        
        (bool success, bytes memory outputFromCalledFunction) = _contractAddr.call{value:msg.value}(
             abi.encodeWithSignature("Nothing()") // 없는 method불러서 fallback 불림
            );
              
        require(success,"failed to transfer ether");
        emit calledFunction(success,outputFromCalledFunction);
    }
}
