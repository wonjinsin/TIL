// SPDX-License-Identifier:GPL-30
pragma solidity >= 0.7.0 < 0.9.0;

contract lec17 {
    mapping(uint256=>uint256) private ageList; // 길이를 알수는 없다

    function setAgeList(uint256 _index, uint256 _age) public {
        ageList[_index] = _age;
    }

    function getAge(uint256 _index) public view returns(uint256) {
        return ageList[_index]; // _index에 해당하는 key없으면 0 나옴
    }
}