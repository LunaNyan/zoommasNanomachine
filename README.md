# [작동 예시](https://www.youtube.com/watch?v=ew_YJhzZvJI)
### 플래시게임 깨주는 사이버맨

## 이게 대체 뭔가요?
[고기굽기 플래시게임](https://flasharch.com/archive/play/4a637f61659230c42484a2e2de7f4f42)을 자동화하는 스크립트입니다.

고득점(최소 6자리수)을 목표로 게임을 자동 플레이합니다.

## 어떻게 사용하나요?
1. 우선 [Python3](https://www.python.org/downloads/)가 필요합니다. 3.8 이상을 권장합니다. 개발 환경은 3.10.6입니다.
2. 이 레포지토리를 clone한 뒤, pip install -r requirements.txt를 실행하여 필요한 디펜던시를 설치합니다.
3. [플래시 플레이어](https://archive.org/details/flash-player-portable)를 다운로드받습니다.
4. [SWF 파일](https://flasharch.com/cdn/uploads/archived/2020/10/10/a28704038763ec6850c48bd5682454e7_20201010215850.swf)을 다운로드받은 뒤, 열려있는 플래시 플레이어에 던져넣습니다.
5. 열려있는 플레이어의 제목 표시줄을 포함한 좌상단 모서리를 화면 좌상단에 밀착시킵니다.
6. main.py를 실행한 뒤 Enter를 누릅니다.

## TODO
- [ ] 제출 이후 불판에 고기가 남아있는 경우(드래그 인식 불량)에 대한 대응
- [ ] 오브젝트 디텍션이 AI(TensorFlow)를 사용하도록 코드 리라이트
- [ ] 플래시 플레이어의 창 위치를 인식시키기

tensorflow-gpu를 사용할 경우 NVIDIA 기준 GeForce GTX 1050, 드라이버 450.80.02 이상이 필요합니다.
