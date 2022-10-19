// SPDX-License-Identifier: GPL-30
pragma solidity >= 0.7.0 < 0.9.0;

contract lec5 {
    /*
    function 이름 () public { // (public private internal external 변경 가능
        // 내용
    }
    */
    
    /*
    public: 모든곳에서 접근 가능
    external: public 처럼 모든곳에서 접근 가능하나, external이 정의된 자기자신 컨트랙 내에서 접근 불가
    private: 오직 private이 정의된 자기 컨트랙트에서만 가능(상속 받은 자식도 불가능)
    internal: 오직 자기 컨트랙트와 상속한 자식만 사용가능
    */

    // 1. public
    uint256 public a = 5;

    // 2. private
    uint256 private a2 = 5; // 배포해도 Deployed Contrancts 변수확인에 안뜸
}

contract Public_example {
    uint256 public a = 3;

    function changeA(uint256 _value) public {
        a = _value;
    }

    function get_a() view public returns (uint256) {
        return a;
    }
}

contract Public_example_2 {
    Public_example instance = new Public_example();

    function changeA_2(uint256 _value) public {
        instance.changeA(_value);
    }
    function use_public_example_a() view public returns (uint256) {
        return instance.get_a();
    }
}