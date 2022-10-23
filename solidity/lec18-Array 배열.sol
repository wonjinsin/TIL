// SPDX-License-Identifier:GPL-30
pragma solidity >= 0.7.0 < 0.9.0;

contract lec18 {
    uint256[] public ageArray;
    uint256[10] public ageFixedSizeArray;
    string[] public nameArray = ["Kal", "Jhon", "Kerri"];

    function AgeLength() public view returns(uint256) {
        return ageArray.length;
    }

    function AgePush(uint256 _age) public {
        ageArray.push(_age);
    }

    function AgeGet(uint256 _index) public view returns(uint256) {
        return ageArray[_index];
    }

    function AgePop() public {
        ageArray.pop();
    }

    // 0 -> 10, 1 -> 70 => 0 -> 0, 1 -> 70 : 즉 index의 값이 0이 되는거 길이는 안달라짐 
    function AgePop(uint256 _index) public {
        delete ageArray[_index];
    }

    // index 값 넘는거 넣으면 에러생김, push로 길이 늘려줘야됨
    function AgeChange(uint256 _index, uint256 _age) public {
        ageArray[_index] = _age;
    }
}