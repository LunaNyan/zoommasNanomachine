# 고기굽기 플래시게임 (https://flasharch.com/archive/play/4a637f61659230c42484a2e2de7f4f42) 매크로 스크립트

import random

import pyautogui
import time
import sys
import ctypes
from locations import *

def mainWork(delay, detMin, detMax, offset):
    print("[Stage 1] 생고기 접시 이미지 매칭")
    print("색상 감지 최소값 : " + str(detMin))
    print("색상 감지 최대값 : " + str(detMax))
    catchLimit = 30
    cnt = 1
    time.sleep(.2)
    for pos in areaWork:
        print(pos)
        catched = False
        # 생고기 올려져있는 영역을 찍는다
        im1 = pyautogui.screenshot(region=(areaTarget.X1, areaTarget.Y1, areaTarget.X2, areaTarget.Y2))
        for ay in range(areaTarget.Y2 - areaTarget.Y1): # 수직 주사
            try:
                for ax in range(areaTarget.X2 - areaTarget.X1): # 수평 주사
                    px = im1.getpixel(xy=(ax, ay)) # 픽셀 하나하나를 찍는다
                    if detMin[0] <= px[0] <= detMax[0] and detMin[1] <= px[1] <= detMax[1] and detMin[2] <= px[2] <= detMax[2]:
                        # 고기 발견☆
                        print("고기 발견 (" + str(ax) + ", " + str(ay) + ", 색상값 : " + str(px) + ")")
                        catched = True
                        catchLimit -= 1 # 무한루프 방지
                        print("클릭 오프셋 : " + str(offset))
                        ctypes.windll.user32.SetCursorPos(areaTarget.X1 + ax + offset[0], areaTarget.Y1 + ay + offset[1]) # 고기를 집어서
                        ctypes.windll.user32.mouse_event(2, 0, 0, 0, 0) # 마우스 누름
                        time.sleep(.05)
                        print(str(cnt) + "번 자리로 가져다 놓음")
                        ctypes.windll.user32.SetCursorPos(pos[0], pos[1]) # 불판으로 마우스 강제이동
                        ctypes.windll.user32.mouse_event(4, 0, 0, 0, 0) # 메우스 뗌
                        time.sleep(.05)
                        pyautogui.click() # 인식불량 방지
                        cnt += 1
                        raise ValueError
                    if catchLimit < 0:
                        # 무한 캐칭을 방지하기 위한 안전장치
                        # 30번 이상 catch한 경우 스크립트를 강제 종료함
                        print("[Error] 이미지 매칭 부분 무한루프 발생")
                        im1.save("bug.png")
                        sys.exit(6794)
                    ax += 1
            except ValueError:
                break
            ay += 1
        if not catched:
            # 게임 클리어한 것으로 간주
            print("고기를 찾을 수 없음, 스크립트 종료")
            im1.save("bug.png")
            sys.exit()

    print(str(delay) + "초 기다림")
    time.sleep(delay)

    print("[Stage 2] 뒤집기")
    cnt = 1
    for pos in areaWork:
        print(str(cnt) + "번 자리 뒤집음 (" + str(pos[0]) + ", " + str(pos[1]) + ")")
        ctypes.windll.user32.SetCursorPos(pos[0], pos[1]) # 지정된 자리에 올라가있는 고기를
        ctypes.windll.user32.mouse_event(2, 0, 0, 0, 0) # 눌렀다
        ctypes.windll.user32.mouse_event(4, 0, 0, 0, 0) # 뗌
        time.sleep(.1) # 인식불량 방지
        cnt += 1

    print(str(delay) + "초 기다림")
    time.sleep(delay)

    print("[Stage 3] 제출")
    cnt = 1
    for pos in areaWork:
        print(str(cnt) + "번 자리 제출 (" + str(pos[0]) + ", " + str(pos[1]) + ")")
        ctypes.windll.user32.SetCursorPos(pos[0], pos[1]) # 지정된 자리에 올라가있는 고기를
        ctypes.windll.user32.mouse_event(2, 0, 0, 0, 0) # 눌러서
        time.sleep(.05)
        ctypes.windll.user32.SetCursorPos(dish[0] + random.randint(-5, 5), dish[1] + random.randint(-5, 5)) # 접시로
        ctypes.windll.user32.mouse_event(4, 0, 0, 0, 0) # 갖다놓는다
        time.sleep(.05)
        cnt += 1

input("Ready?")

for pos in startGame:
    print("시작버튼 광클")
    ctypes.windll.user32.SetCursorPos(pos[0], pos[1])
    ctypes.windll.user32.mouse_event(2, 0, 0, 0, 0)  # left down
    time.sleep(.05)
    ctypes.windll.user32.mouse_event(4, 0, 0, 0, 0)  # left up
    time.sleep(.05)

while True:
    mainWork(3.2, (240, 60, 60), (255, 90, 100), (0, 0)) # 소고기?
    mainWork(5, (240, 50, 50), (255, 200, 200), (-5, 5)) # 삼겹살
