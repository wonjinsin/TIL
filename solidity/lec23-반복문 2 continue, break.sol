// SPDX-License-Identifier: GPL-3.0
pragma solidity >= 0.7.9 < 0.9.0;

// for, while, do-while
contract lec22 {
	event CountryIndexName(uint256 indexed _index, string _name);
	string [] private countryList = ["South Korea", "North Korea", "USA", "China", "Japan"];

	function useContinue() public {
		for (uint256 i = 0; i < countryList.length; i++) {
			if (i % 2 == 1) { // odd
				continue;
			}
			emit CountryIndexName(i, countryList[i]);
		}
	}

	function useBreak() public {
		for (uint256 i = 0; i < countryList.length; i++) {
			if (i == 2) {
				break;
			}
			emit CountryIndexName(i, countryList[i]);
		}
	}
}