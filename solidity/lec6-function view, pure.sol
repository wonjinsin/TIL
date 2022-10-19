// SPDX-License-Identifier: GPL-30
pragma solidity >= 0.7.0 < 0.9.0;

contract lec6 {
    /*
    function 이름 () public { // (public private internal external 변경 가능
        // 내용
    }
    */
    
    /*
    function get_a() view external returns (uint256)
    */

    /*
    view: function 밖의 변수들을 읽을수 있으나 변경 불가능
    pure: function 밖의 변수들을 읽지 못하고, 변경도 불가능
    view와 pure 둘다 명시 안할때: function 밖의 변수들을 읽고, 변경 가능
    */

    // 1.view
    uint256 public a = 1;
    function read_a() public view returns(uint256) {
        return a + 2;
    }

    // 2.pure
    function read_a2() public pure returns(uint256) {
        uint256 b = 1;
        return 4 + 2 + b;
    }

    // 3. pure, view: X
    function read_a3() public returns(uint256) {
        a = 13;
        return a;
    }

}