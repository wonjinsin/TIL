// SPDX-License-Identifier:GPL-30
pragma solidity >= 0.7.0 < 0.9.0;

contract Father {
    uint256 public fatherMoney = 500;
    function getFatherName() public pure returns (string memory) {
        return "KimJung";
    }

    function getMoney() public view virtual returns(uint256) {
        return fatherMoney;
    }
}

contract Mother {
    uint256 public motherMoney = 500;
    function getMotherName() public pure returns (string memory) {
        return "Leesol";
    }
    function getMoney() public view virtual returns(uint256) {
        return motherMoney;
    }
}

// 다중 상속시 상속된 contract에 같은 function이 있으면 override 해줘야됨 
contract Son is Father, Mother {
    function getMoney() public view override(Father, Mother) returns(uint256) {
        return fatherMoney + motherMoney;
    }
}