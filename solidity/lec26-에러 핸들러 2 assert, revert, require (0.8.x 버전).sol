// SPDX-License-Identifier: GPL-3.0
pragma solidity >=0.7.9 <0.9.0;

// 에러핸들러: require, revert, assert, try/catch

contract lec26 {
    /*
		0.8.0 포함 x
		0.8.1 ~
		assert: 오직 내부적 에러 테스트 용도, 불변성 체크 용도. 0.8부터는 가스 환불해줌
				assert가 에러를 발생시키면, Panic(uint256) 이라는 에러타입의 에러 발생 
	*/

    // use 300000 gas
    function assertNow() public pure {
        assert(false); // test 용으로 많이씀, 환불 안해주니까, false일때 작동
    }

    // use 21322 gas, revert 호출에 대한 가스비용만 내고, 나머지 호출들에 대한 비용은 환불해줌
    function revertNow() public pure {
        revert("error!!"); // if 문에서 보통 이용
    }

    // 21338 gas
    function requireNow() public pure {
        require(false, "occured"); // false일때 작동
    }

    function onlyAdults(uint256 _age) public pure returns (string memory) {
        if (_age < 19) {
            revert("You are not allowed to pay for the cigarette");
        }
        return "Your payment is succeeded";
    }

    function onlyAdults2(uint256 _age) public pure returns (string memory) {
        require(_age > 19, "You are not allowed to pay for the cigarette");
        return "Your payment is succeeded";
    }
}
