import os
import csv
import subprocess as sp
import tkinter as tk
from tkinter import filedialog
from os import system as cmd

root = tk.Tk()
# sp.Popen("airmon-ng check kill", creationflags = subprocess.CREATE_NEW_CONSOLE)

print('작업하려는 동영상 파일을 입력해주세요. (ctrl 눌러 복수선택 가능, 이름순으로 자동정렬)')
print('Tip: 입력된 파일을 모두 가상의 한 파일로 취급합니다.')
print('Tip: 파일 이름에 특수문자, 띄어쓰기 등이 들어있으면 오류가 발생합니다.')
videoPaths = filedialog.askopenfilenames(initialdir = os.getcwd(), title = 'choose your file', filetypes = (('mkv 파일','*.mkv'),('mp4 파일','*.mp4')))
videoExt = os.path.splitext(videoPaths[0])[1]
videoDurations = []
for i, path in enumerate(videoPaths):
    popen = sp.Popen('tools\\ffprobe.exe -i '+path+' -show_entries format=duration -v quiet -of csv="p=0"', shell=True, stdout=sp.PIPE)
    videoDurations.append(float(popen.stdout.read().decode('ascii')))
    pathName, pathExtension = os.path.splitext(path)
    print('[{0}]: {1} - {2}: 시간 {3}'.format(i+1, pathName, pathExtension[1:].upper(), videoDurations[i]))
input('이 순서대로 작업을 진행할까요? 계속하시려면 엔터를 눌러주세요.')

print('\n적용하려는 CSV 파일을 입력해주세요. (한개만)')
csvPath = filedialog.askopenfilename(initialdir=os.getcwd(), title='choose your file', filetypes = (('CSV 파일','*.csv'),))
csvFile = open(csvPath, 'r', encoding='utf-8-sig')
csvReader = csv.reader(csvFile)
print('CSV 파일: {0}\n'.format(csvPath))

print('앞뒤로 몇초의 여유분을 남길지 입력해주세요. (정수 혹은 실수)')
print('ex) 2를 입력하면, CSV 파일 타임라인 기준, 시작에서 2초 전, 종료에서 2초 뒤까지를 자릅니다.')
interval = int(input('interval= '))

print('\n클립모음을 내보내고 싶은 폴더를 선택해주세요.')
print('Tip: 드라이브 용량이 넉넉한지 미리 확인해주세요!')
print('Tip: 폴더 이름에 특수문자, 띄어쓰기 등이 들어있으면 오류가 발생합니다.')
outDir = filedialog.askdirectory(initialdir=os.getcwd(), title='choose your directory')
print('내보내기: {0}\n'.format(outDir))

print('클립의 이름을 입력해주세요.')
print('ex) "클립" 입력시 "클립-1", "클립-2", "클립-3"... 식으로 저장됩니다.')
clipName = input('클립 이름: ')

input('\n모든 준비가 완료됐습니다... 엔터를 누르면 작업을 시작합니다.')

def parse(string): #dateutil 이 Python 3.9 를 지원하지 않아서 기능을 흉내냈음. ":" 으로 구분된 time string 만 처리가능
    time = tuple(map(float, string.split(':')))
    return time[0]*3600 + time[1]*60 + time[2]

def timeIndex(seconds): # seconds를 넣으면 거기에 맞는 video 번호와 real time 을 반환
    total = 0
    for i, duration in enumerate(videoDurations):
        if(seconds < total + duration):
            return (i, seconds - total)
        total += duration
    raise Exception('CSV 파일의 타임라인 값이 전체 영상 길이를 초과합니다.')

for num, line in enumerate(csvReader):
    start = parse(line[0]) - interval
    startPtr, startReal = timeIndex(start)
    end = parse(line[1]) + interval
    endPtr, endReal = timeIndex(end)

    print(line)
    print('{0}:{1}-{2} / {3}-{4}-{5}'.format(start, startPtr, startReal, end, endPtr, endReal))

    if(startPtr == endPtr):
        outPath = '{0}/{1}-{2}{3}'.format(outDir, clipName, num+1, videoExt)
        cmdInput = ['tools\\ffmpeg.exe','-i',videoPaths[startPtr],'-ss',str(startReal),'-to',str(endReal),outPath]
        popen = sp.Popen(cmdInput, shell=True, stdout=sp.PIPE)

    else:
        for ptr in range(startPtr, endPtr+1):
            outPath = '{0}/{1}-{2}({3}){4}'.format(outDir, clipName, num+1, ptr+1, videoExt)
            if(ptr==startPtr):
                cmdInput = ['tools\\ffmpeg.exe','-i',videoPaths[ptr],'-ss',str(startReal),outPath]
            elif(ptr==endPtr): # 여기서 for문 끝남
                cmdInput = ['tools\\ffmpeg.exe','-i',videoPaths[ptr],'-to',str(endReal),outPath]
            else:
                cmdInput = ['tools\\ffmpeg.exe','-i',videoPaths[ptr],outPath]
            popen = sp.Popen(cmdInput, shell=True, stdout=sp.PIPE)

    print('{0} 생성 완료!'.format(outPath))

csvFile.close()

tk.messegebox.showinfo('고티죠?', '동영상 자르기 완료!')
