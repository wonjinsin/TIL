// SPDX-License-Identifier:GPL-30
pragma solidity >= 0.7.0 < 0.9.0;

contract Father {
    string public familiyName = "Kim";
    string public givenName = "Jung";
    uint256 public money = 100;

    constructor (string memory _givenName) {
        givenName = _givenName;
    }

    function getFamilyName() view public returns (string memory) {
        return familiyName;
    }

    function getGivenName() view public returns(string memory) {
        return givenName;
    }

    // virtual은 overiding 가능 하다는 뜻
    function getMoney() view virtual public returns(uint256) {
        return money;
    }
}

contract Son is Father {

    constructor() Father("James") {
        
    }

    uint256 public earning = 0;
    function work() public {
        earning += 100;
    }

    function getMoney() view public override returns(uint256) {
        return money+earning;
    }
}