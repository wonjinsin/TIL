# Indexing에 유리한 조건

### B-tree 인덱싱과 Range scan을 이용하는 경우로 가정
- Btree란? 
	- [Btree 참고 링크](https://hyungjoon6876.github.io/jlog/2018/07/20/btree.html)

- Range scan이란?
	- 시작점 부터 특정 범위를 스캔하는 방식

### 유리한 조건

- Cardinality가 높은 경우
	- Cardinality란?
      - 중복도가 낮으면 Cardinality가 낮다고 할 수 있음
	- Cardinality가 낮으면(중복이 많으면) 그만큼 검색을 할때 찾아야 하는 범위가 커지기 때문에 성능 낮아짐

- Selectivity(선택도) 가 낮은 경우
	- Selectivity란?
    	- 검색된 값들과 중복되는 다른 rows의 수 / 테이블의 총 rows * 100
    	- ex) 성별 column이 남자인 rows 수 count / 테이블의 총 rows * 100
  	- 즉, columns들의 값들이 특이한 경우일 수록 인덱스 설정에 좋다

- Where에서 자주 사용되는 값

##### `Boolean`이나 `Enum` 같이 중복이 많이 있는 column에는 안거는게 좋다