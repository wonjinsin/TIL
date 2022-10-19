// SPDX-License-Identifier: GPL-30
pragma solidity >= 0.7.0 < 0.9.0;

contract lec3 {
    // 스마트 컨트랙트 사용할떄 이용하는 비용 = Gwei
    // 스마트 컨트랙트가 길거나 복잡할 수록 Gwei가 더 많이 듬
	// 함수 실행할때마다 스마트 컨트랙트 주인은 gas를 내야됨
    // ethereum Yellow paper에 남아있음

    // 1 ether = 10^9 Gwei = 10^18 wei
    // 0.00000000000000001 ether = 1^-18 = 1 wei
    // 0.01 ether - 10^16wei

    uint256 public value = 1 ether;
    uint256 public value2 = 1 wei;
    uint256 public value3 = 1 gwei;
}