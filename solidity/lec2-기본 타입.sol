// SPDX-License-Identifier: GPL-30
pragma solidity >= 0.7.0 < 0.9.0;

contract lec2 {
    // data type
    // bolean: true /false
    bool public b = false;

    // ! || == &&
    bool public b1 = !false; // true
    bool public b2 = false || true; // true
    bool public b3 = false == true; // false
    bool public b4 = false && true; // false 

    // byte 1 ~ 32
    bytes4 public bt = 0x12345678;
    bytes public bt2 = "STRING";

    // address : 지갑의 주소 (계좌번호 개념), 지갑뿐만 아니라 스마트 컨트랙트마다에도 주소 생김, 20 byte
    address public addr = 0x5B38Da6a701c568545dCfcB03FcB875f56beddC4;

    // int vs uint

    // int8
    // -2^7 ~ 2^7 - 1
    int8 public it = 4;

    // uint8
    // 0 ~ 2^8 -1
    uint256 public uit = 133213;

    // + - * /
    uint8 public uit2 = 255; // 256 이상이면 error, 범위 넘김
}