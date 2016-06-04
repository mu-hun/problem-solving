/*
* @autor BetaFish <yale2a1@gmail.com>
* @since 2016-06-04
* 1장. 정렬 알고리즘
*/

/* 정수를 저장하고 있는 배열 'array'가 주어졌다. 이 array에 저장되어 있는 원소(element)들이
* 순서대로 정렬되어 있으면 1을 반환하고, 정렬되어 있지 않으면 0을 반환하는 함수를 작성하라.
* 함수의 시그니쳐는 다음과 같다.
* lenght는 배열 array의 길이를 의미한다.
* int isSorted (int* array, int lenght)
*/
int isSorted (int* array, int lenght)
{
  for (int i = 0; i < lenght-1; i++)
  {
    if (array[i] > array[i+1])
    {
      return 0;
    }
  }
  return 1;
}
