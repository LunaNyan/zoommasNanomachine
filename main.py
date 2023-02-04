import pyautogui
import time
import sys
from locations import *

def mainWork(delay, detMin, detMax, offset):
    print("[Stage 1] 생고기 접시 이미지 매칭")
    print("색상 감지 최소값 : " + str(detMin))
    print("색상 감지 최대값 : " + str(detMax))
    for pos in areaWork:
        print(pos)
        catched = False
        # 생고기 올려져있는 영역을 찍는다
        im1 = pyautogui.screenshot(region=(areaTarget.X1, areaTarget.Y1, areaTarget.X2, areaTarget.Y2))
        for ay in range(areaTarget.Y2 - areaTarget.Y1):
            try:
                for ax in range(areaTarget.X2 - areaTarget.X1):
                    px = im1.getpixel(xy=(ax, ay))
                    if detMin[0] <= px[0] <= detMax[0] and detMin[1] <= px[1] <= detMax[1] and detMin[2] <= px[2] <= detMax[2]:
                        print("고기 발견")
                        print("X_Pos=" + str(ax) + ", Y_Pos=" + str(ay))
                        print("클릭 오프셋 : " + str(offset))
                        pyautogui.moveTo(areaTarget.X1 + ax + offset[0], areaTarget.Y1 + ay + offset[1])
                        pyautogui.mouseDown()
                        pyautogui.moveTo(pos[0], pos[1])
                        pyautogui.mouseUp()
                        catched = True
                        raise ValueError
                    ax += 1
            except ValueError:
                break
            ay += 1
        if not catched:
            print("고기를 찾을 수 없음, 스크립트 종료")
            sys.exit()

    print(str(delay) + "초 기다림")
    time.sleep(delay)

    print("[Stage 2] 뒤집기")
    for pos in areaWork:
        print("X_Pos=" + str(pos[0]) + ", Y_Pos=" + str(pos[1]))
        pyautogui.moveTo(pos[0], pos[1])
        pyautogui.mouseDown()
        pyautogui.mouseUp()
        time.sleep(.15)

    print(str(delay) + "초 기다림")
    time.sleep(delay)

    print("[Stage 3] 제출")
    for pos in areaWork:
        print("X_Pos=" + str(pos[0]) + ", Y_Pos=" + str(pos[1]))
        pyautogui.moveTo(pos[0], pos[1])
        pyautogui.mouseDown()
        pyautogui.moveTo(dish[0], dish[1])
        pyautogui.mouseUp()
        time.sleep(.1)

input("Ready?")

for pos in startGame:
    print("시작버튼 광클")
    pyautogui.moveTo(pos[0], pos[1])
    pyautogui.mouseDown()
    pyautogui.mouseUp()

while True:
    mainWork(0, (240, 60, 60), (255, 90, 100), (0, 0)) # 소고기?
    mainWork(1.5, (240, 50, 50), (255, 170, 170), (-5, 5)) # 삼겹살
