from os import system
import time


class TrafficLight:
    def __init__(self):
        self._color = 'R'
    
    def running(self, switchCnt: int = 10):
        runCnt = 0

        while runCnt < switchCnt:
            if self._color == 'R':
                startTime = 7
                
            if self._color == 'Y':
                startTime = 2

            if self._color == 'G':
                startTime = 5

            while startTime > 0:
                system('cls')
                print(f'{self._color} - {startTime}')
                time.sleep(1)
                startTime -= 1
            
            if self._color == 'R':
                self._color = 'Y'
            elif self._color == 'Y':
                self._color = 'G'
            else:
                self._color = 'R'

            runCnt += 1
            
