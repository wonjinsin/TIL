// SPDX-License-Identifier:GPL-30
pragma solidity >= 0.7.0 < 0.9.0;

contract lec14 {
    event numberTracker(uint256 num, string str);
    // indexed를 통해 원하는 이벤트만 필터해서 가져올수 있다.
    // 아래는 호출예시: numberTracker2에 대한 과거 이벤트 기록을 가져오는데, num이 1이나 2인 것(즉, 첫번째와 두번째 실행된 이벤트)에 대해서만 가져오고, 찾는 block은 1(첫번쨰)꺼부터 최신 블락 전부다
    // lectruer14.getPastEvents('numberTrackger2', {filter: {num:[2,1]}, fromBlock: 1, to Block: "latest"});
    event numberTracker2(uint256 indexed num, string str);

    uint256 num = 0;
    function PushEvent(string memory _str) public {
        emit numberTracker(num, _str);
        emit numberTracker(num, _str);
        num++;
    }
}