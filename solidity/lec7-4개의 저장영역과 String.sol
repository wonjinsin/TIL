// SPDX-License-Identifier: GPL-30
pragma solidity >= 0.7.0 < 0.9.0;

contract lec7 {
    /*
    storage: 대부분의 변수, 함수들이 저장되며, 영속성으로 저장이되어 가스 비용이 비싸다.
    memory: 함수의 파라미터, 리턴값, 레퍼런스 타입이 주로 저장됨.
            그러나 storage 처럼 영속적이지 않고, 함수내애서만 유효하기에 storage보다 가스비용이 쌈.
    colldata: 주로 external function의 마라미터에서 사용 됨.
    stack: EVM (Ethereum Virtual Machine) 에서 stack data를 관리할때 쓰는 영역인데 1024mb 제한적입니다.
    */

    uint256 public a = 1; // storage에 저장됨
    function read_a() public view returns(uint256) {
        return a + 2;
    }

    // 2.pure
    function read_a2() public pure returns(uint256) { // parameter와 return값도 memory에 저장됨
        uint256 b = 1; // memory에 저장됨
        return 4 + 2 + b;
    }

    // string은 memory를 써줘야됨
    function get_string(string memory _str) public pure returns(string memory) {
        return _str;
    }
}