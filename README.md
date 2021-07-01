# DDOL3Cutter
![matstar](https://user-images.githubusercontent.com/81800589/124090781-207ada00-da90-11eb-84e7-7c37bf11d4ab.png)

똘삼커터는 크라우드소싱 편집에 최적화된 동영상 타임라인 자르기 툴입니다.  
CSV 파일로 MP4 및 MKV 파일을 빠르게 잘라낼 수 있습니다.  
림월드 팀 똘찌 동영상 편집 작업에 사용되었습니다.  



### 사용방법
1. 릴리즈 파일 다운로드(https://github.com/CodePsy-2001/DDOL3Cutter/releases) 후 압축풀기
2. 동영상 파일, CSV 파일, interval 값, 내보낼 폴더, 내보낼 이름 순서대로 입력
3. ffmpeg.exe 를 주어진 값에 맞게 실행시켜 동영상을 초스피드로 잘라줍니다. (15시간 UHD MP4 영상 기준 클립 200개 생성 30분컷 가능)

interval 값이란? 주어진 타임라인 앞뒤에 여유분으로 추가할 값입니다. 정수 및 실수로 입력 가능하며, 음수를 넣으면 역으로 여유분을 잘라냅니다.  
CSV 파일이란? 쉼표와 줄바꿈으로 구분된 형태의 자료구조입니다. 엑셀의 원시형태라고 보시면 됩니다.  
여기(https://github.com/CodePsy-2001/DDOL3Cutter/blob/main/5.csv) 에 림월드 5화에 사용된 CSV 파일 예제를 올려두었으니 참고 바랍니다. 엑셀에서 다른 이름으로 저장 누르고 CSV 확장자 선택하면 됩니다.  



### 발생 가능한 에러
 - 압축을 푼 폴더의 파일 중 하나라도 소실되면 에러가 발생합니다.
 - 드라이브 남은 용량을 체크하지 않습니다. 빈 공간을 넉넉히 준비해두시기 바랍니다.



### 특수기능
 - 동영상 여러개를 입력하면 이름순으로 정렬한 다음 가상의 하나의 파일로 취급합니다. (예: 2시간씩 잘린 mkv 다시보기 파일)
 - 매우 가볍습니다. 특수기능인가?



### 후원하기
트윕: https://twip.kr/codepsy  
여러분들의 소중한 후원은 팀 똘찌의 얼쭈 먹방에 사용됩니다.
