// SPDX-License-Identifier: GPL-3.0
pragma solidity >=0.7.9 <0.9.0;

// modifier require랑 같이 쓰임
// revert 나오는 조건이 정해져 있을때 이용
// 아래 onlyAdults를 각 function 마다 써줘야 되는데 그걸 방지할수 있음

contract lec30 {
	modifier onlyAdults {
		revert("You are not allowed to pay for ther cigarette");
		_; // 함수가 어디 올지, 아래 BuyCigarette가 옴
	}

	function BuyCigarette() public pure onlyAdults returns (string memory) {
		return "Your payment is succeeded";
	}

	modifier onlyAdults2(uint256 _age) {
		require(_age > 18, "You are not allowed to pay for the cigarette");
		_;
	}

	function BuyCigarette2(uint256 _age) public pure onlyAdults2(_age) returns (string memory) {
		return "Your payment is succeeded";
	}

	uint256 public num = 5;
	modifier numChange {
		_;
		num = 10;
		// 결국 10이 됨
	}
	function numChangeFunction() public numChange {
		num = 15;
	}
}