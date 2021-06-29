from datetime import date
from datetime import time
from datetime import datetime
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
import csv

def parse(string): #dateutil이 Python 3.9 를 지원하지 않아서 기능을 흉내냈음. ":" 으로 구분된 time string만 처리가능
    timetuple = tuple(map(int, string.split(':')))
    return datetime(date.today().year, date.today().month, date.today().day, timetuple[0], timetuple[1], timetuple[2])

print("분리를 원하는 비디오 파일(mp4)명을 입력해주세요(확장자 제외).")
print("같은 이름의 csv 파일이 같은 폴더 위치에 들어있어야 합니다.")
video = input("video= ")
print("앞뒤로 몇초를 더할지 입력해주세요.")
print("예를 들어 2를 입력하면, CSV 파일 타임라인 기준, 시작에서 2초 전, 종료에서 2초 뒤까지를 자릅니다.")
interval = int(input("interval= "))

fcsv = open(video+'.csv', 'r', encoding='utf-8-sig')
rcsv = csv.reader(fcsv)

count = 0
for line in rcsv:
    print(line)
    start = (parse(line[0]) - datetime.combine(date.today(), time.min)).total_seconds() - interval
    end = (parse(line[1]) - datetime.combine(date.today(), time.min)).total_seconds() + interval
    print(start, end)

    count += 1
    #ffmpeg_extract_subclip("full.mp4", start_seconds, end_seconds, targetname="cut.mp4")
    ffmpeg_extract_subclip(video+'.mp4', start, end, targetname=video+'-'+str(count)+'.mp4') # video-count.mp4
fcsv.close()

print("총 "+str(count)+"개의 클립이 생성되었습니다.")
input("종료하려면 엔터를 누르세요.")