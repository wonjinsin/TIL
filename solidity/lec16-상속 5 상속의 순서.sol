// SPDX-License-Identifier:GPL-30
pragma solidity >= 0.7.0 < 0.9.0;

contract Father {
    event FatherName(string name);
    function who() public virtual {
        emit FatherName("KimDaeho");
    }
}

contract Mother {
    event MotherName(string name);
    function who() public virtual {
        emit MotherName("leeSol");
    }
}

contract Son is Father, Mother {
    function who() public override(Father, Mother) {
        super.who(); // 상속 할때, Mother를 최근에 상속 해서 Mother의 who가 불림
    }
}