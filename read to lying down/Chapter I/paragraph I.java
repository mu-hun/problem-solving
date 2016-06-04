/*
* @autor BetaFish <yale2a1@gmail.com>
* @since 2016-06-04
* 1장. MAX_COUNT를 넘어선 페이지를 새로 열면 오류 메세지 보내기
*/

/*
* 이 순서 같은 페이지를 새로고침을 할때는 정상적으로 작동된다.
* 1. processPageCloseRequset
* 2. processPageOpenRequset
* 하지만 같은 페이지의 주소를 가리키는 링크를 클릭했을때는
* 1. processPageOpenRequset
* 2. processPageCloseRequset
* current_count가 MAX_COUNT값과 같아져서 버그가 발생한다.
*/

processPageOpenRequset ()
{
  if (current_count < MAX_COUNT)
  {
    sendResponse ();
    current_count++;
  }
  else
  {
    sendErrorMessage ();
  }
}
processPageCloseRequset ()
{
  current_count--;
}
