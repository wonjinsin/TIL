// SPDX-License-Identifier: GPL-3.0
pragma solidity >= 0.7.9 < 0.9.0;

contract lec21 {
    string private outcome = "";

    function isIT5(uint256 _number) public returns (string memory) {
        if (_number == 5) {
            outcome = "Yes, it is 5";
            return outcome;
        } else if (_number == 6) { // else 도 가능
            outcome = "yes, it is 6";
        }
        
        outcome = "No, it is not 5";
        return outcome;
        
    }
}