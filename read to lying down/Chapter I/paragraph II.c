/*
* @autor BetaFish <yale2a1@gmail.com>
* @since 2016-06-04
* 2장. 52장의 카드를 저장하기
*/

/* 구조체 : full_card
* 보통 char형 변수는 1바이트를 차지하고 int형 변수는 4바이트의 공간을 차지한다.
* 아래에서 정의한 구조체 'full_card'는 char 형의 배열을 가리키는 포인터(평균 6바이트)와
* int형(4바이트)으로 구성되어 있기 때문에 하나의 카드가 10바이트의 메모리 공간을 차지하게 된다.
* 메모리 공간을 적게 차지하려면 어떻게 하는것이 좋겠는가?
*/
struct full_card {
  char *shape;
  char number;
} cards[] = {
  "spade", 1,
  "heart", 1,
  "diamond", 1,
  "colobber", 1,
  "spade", 2,
  "heart", 2,
  "diamond", 2,
  "colobber", 2,
  // 이하 생략
}

/* 구조체 : short_card
* 아래와 같이 카드의 무늬와 숫자가 모두 char형 변수로 충분히 표현될 수 있다.
* 카드 한장이 차지하는 공간이 2바이트로 대폭 줄어듬
*/
struct short_card {
  char shape;
  char number;
} cards[] = {
  'S', '1',
  'H', '1',
  'D', '1',
  'C', '1',
  'S', '2',
  'H', '2',
  'D', '2',
  'C', '2',
  // 이하 생략
}

/* 그런데 char형 변수에 저장된 정보를 full_card 식으로 변환하려면 시간이 많이 소요됨
* 알고리즘을 작성하다 보면 프로그램의 실행 속도를 의미하는 '시간'(full_card)과
* 메모리의 사용량을 의미하는 '공간'(short_card)이 항상 대립한다는 사실을 알 수 있다.
*/
