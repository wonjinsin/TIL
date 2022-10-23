// SPDX-License-Identifier: GPL-3.0
pragma solidity >= 0.7.9 < 0.9.0;

// for, while, do-while
contract lec22 {
	event CountryIndexName(uint256 indexed _index, string _name);
	string [] private countryList = ["South Korea", "North Korea", "USA", "China", "Japan"];

	function lenearSearch(string memory _search) public view returns (uint256, string memory) {
		for (uint256 i = 0; i < countryList.length; i++) {
			// solidity는 string 비교가 안됨, 해쉬함수로 만들어서 비교해야 됨
			if (keccak256(bytes(countryList[i])) == keccak256(bytes(_search))) {
				return (i, countryList[i]);
			}
		}

		return (0, "Nothing");
	}
}