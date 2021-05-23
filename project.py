## Module Import ##
import sys
from PyQt5.QtCore import QDate  #GUI를 사용하기 위한 PyQt Module
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *   #PyQt의 다양한 Widget들을 사용할 수 있게 해주는 모듈

import pandas as pd     #pandas module import (data management)
import sqlite3  #Database Module
from datetime import datetime   #날짜를 활용하기 위한 module import

#데이터베이스 연동
con = sqlite3.connect("./database.db")
dataframe = pd.read_sql("SELECT * FROM TABLE_FOOD", con)

#전역변수 Count, fridge, sort 선언 및 초기화
global Count, fridge, sort
Count = len(dataframe)  #Count는 혹시 저장된 data가 있을 수 있으니 dataframe의 row의 개수로 설정
fridge = 0
sort = 0

## Class ##
class MainWindow(QMainWindow):
    def __init__(self):     #첫 화면 실행
        super(MainWindow, self).__init__()
        loadUi("start.ui", self)    #첫 화면 ui 실행
        self.pushButton.clicked.connect(self.gotoScreen2)   #화면 클릭 시 screen2로 연결

    def gotoScreen2(self):  #Screen2로 연결해주는 함수
        screen2 = Screen2()
        widget.addWidget(screen2)
        widget.setCurrentIndex(widget.currentIndex() + 1)


class Screen2(QMainWindow):
    def __init__(self):     #메뉴 화면(Screen2) 실행
        super(Screen2, self).__init__()
        loadUi("menu.ui", self)     #메뉴 ui 실행
        self.pushButton.clicked.connect(self.gotoScreen3)       #1. 새 음식 넣기
        self.pushButton_2.clicked.connect(self.gotoFridge3)     #2. 유통기한 확인
        self.pushButton_3.clicked.connect(self.gotoScreen11)    #3. 분리수거법 확인
        self.pushButton_4.clicked.connect(self.gotoScreen8)     #4. 음식 빼기
        self.pushButton_9.clicked.connect(self.gotoScreen1)     #Back 버튼 클릭 시 첫 화면으로 연결

    def gotoScreen1(self):  #첫 화면으로 연결해주는 함수
        mainwindow = MainWindow()
        widget.addWidget(mainwindow)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def gotoScreen3(self):  #1번 메뉴 선택 시 냉동고 냉장고 선택하는 Screen3으로 연결해주는 함수
        screen3 = Screen3()
        widget.addWidget(screen3)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def gotoFridge3(self):  #2번 메뉴 선택 시 냉동고 냉장고 선택하는 Fridge3으로 연결해주는 함수
        fridge3 = Fridge3()
        widget.addWidget(fridge3)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def gotoScreen8(self):  #4번 메뉴 선택 시 버릴 음식 선택하는 Screen8로 연결해주는 함수
        screen8 = Screen8()
        widget.addWidget(screen8)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def gotoScreen11(self): #3번 메뉴 선택 시 분리수거 방법 안내하는 Screen11로 연결해주는 함수
        screen11 = Screen11()
        widget.addWidget(screen11)
        widget.setCurrentIndex(widget.currentIndex() + 1)


class Screen3(QDialog):
    def __init__(self):     #냉장고 냉동고 선택하는 Screen3 실행
        super(Screen3, self).__init__()
        loadUi("fridge.ui", self)   #냉장고 냉동고 선택 ui 실행
        self.pushButton_3.clicked.connect(self.gotoScreen2)     #Back 버튼 클릭 시 전 화면(Screen2)으로 연결
        self.pushButton_1.clicked.connect(self.gotoScreen4_1)   #냉동고
        self.pushButton_2.clicked.connect(self.gotoScreen4_2)   #냉장고

    def gotoScreen2(self):  #Screen2로 연결
        screen2 = Screen2()
        widget.addWidget(screen2)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def gotoScreen4_1(self):    #냉동고 선택 시
        global fridge
        fridge = 0      #전역변수 fridge를 0으로 설정
        #Screen4로 연결
        screen4 = Screen4()
        widget.addWidget(screen4)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def gotoScreen4_2(self):    #냉장고 선택 시
        global fridge
        fridge = 1      #전역변수 fridge를 1로 설정
        #Screen4로 연결
        screen4 = Screen4()
        widget.addWidget(screen4)
        widget.setCurrentIndex(widget.currentIndex() + 1)


class Screen4(QMainWindow):
    def __init__(self):     #Screen4 실행
        super(Screen4, self).__init__()
        loadUi("sort.ui", self)     #음식 종류를 고르는 sort ui 실행
        self.pushButton_9.clicked.connect(self.gotoScreen3)     #Back 버튼 클릭 시 전 화면(Screen3)으로 연결
        self.pushButton.clicked.connect(self.gotoScreen6)       #우유, 유제품
        self.pushButton_2.clicked.connect(self.gotoScreen6_2)   #채소류
        self.pushButton_3.clicked.connect(self.gotoScreen6_3)   #음료, 주류
        self.pushButton_4.clicked.connect(self.gotoScreen6_4)   #계란
        self.pushButton_5.clicked.connect(self.gotoScreen6_5)   #육류
        self.pushButton_6.clicked.connect(self.gotoScreen6_6)   #해산물
        self.pushButton_7.clicked.connect(self.gotoScreen6_7)   #과일, 견과류
        self.pushButton_8.clicked.connect(self.gotoScreen6_8)   #기타

    def gotoScreen3(self):  #Screen3으로 연결
        screen3 = Screen3()
        widget.addWidget(screen3)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def gotoScreen6(self):  #우유, 유제품 선택 시
        global sort
        sort = 1    #전역변수 sort를 1로 설정
        #Screen6으로 연결
        screen6 = Screen6()
        widget.addWidget(screen6)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def gotoScreen6_2(self):    #채소류 선택 시
        global sort
        sort = 2    #전역변수 sort를 2로 설정
        #Screen6으로 연결
        screen6 = Screen6()
        widget.addWidget(screen6)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def gotoScreen6_3(self):    #음료, 주류 선택 시
        global sort
        sort = 3    #전역변수 sort를 3으로 설정
        #Screen6으로 연결
        screen6 = Screen6()
        widget.addWidget(screen6)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def gotoScreen6_4(self):    #계란 선택 시
        global sort
        sort = 4    #전역변수 sort를 4로 설정
        #Screen6으로 연결
        screen6 = Screen6()
        widget.addWidget(screen6)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def gotoScreen6_5(self):    #육류 선택 시
        global sort
        sort = 5    #전역변수 sort를 5로 설정
        #Screen6으로 연결
        screen6 = Screen6()
        widget.addWidget(screen6)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def gotoScreen6_6(self):    #해산물 선택 시
        global sort
        sort = 6    #전역변수 sort를 6으로 설정
        #Screen6으로 연결
        screen6 = Screen6()
        widget.addWidget(screen6)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def gotoScreen6_7(self):    #과일, 견과류 선택 시
        global sort
        sort = 7    #전역변수 sort를 7로 설정
        #Screen6으로 연결
        screen6 = Screen6()
        widget.addWidget(screen6)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def gotoScreen6_8(self):    #기타 선택 시
        global sort
        sort = 8    #전역변수 sort를 8로 설정
        #Screen6으로 연결
        screen6 = Screen6()
        widget.addWidget(screen6)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        

class Screen5(QMainWindow):
    def __init__(self):     #새로 넣어준 음식의 남은 일수를 출력해주는 Screen5 실행
        super(Screen5, self).__init__()
        loadUi("state.ui", self)    #state ui 실행
        self.menu.clicked.connect(self.gotoScreen2)     #1번 메뉴의 실행이 끝났으므로 Menu로 돌아감

        global dataframe, Count    #전역 변수 Count를 dataframe에 저장된 정보 출력을 위한 index로 활용
        foodname = dataframe.iloc[Count][2]
        day = dataframe.iloc[Count][6]
        date = str(day)

        self.label.setText(foodname)    #음식 이름 출력
        self.label_3.setText(date)      #남은 일수 출력

        Count = Count + 1   #Count(Index) 1 증가

    def gotoScreen2(self):  #Screen2로 연결
        screen2 = Screen2()
        widget.addWidget(screen2)
        widget.setCurrentIndex(widget.currentIndex() + 1)


class Screen6(QMainWindow):
    def __init__(self):     #음식 정보 입력하는 Screen6 실행
        #음식 관련 정보 입력 변수 선언 및 초기화
        self.year = 0           #유통기한 연도
        self.month = 0          #유통기한 월
        self.day = 0            #유통기한 일
        self.food_name = ""     #음식 이름
        self.date_diff = 0      #유통기한 남은 일수

        super(Screen6, self).__init__()
        loadUi("input.ui", self)    #음식 정보 입력하는 input ui 실행
        
        print(dataframe)
        
        self.pushButton_9.clicked.connect(self.gotoScreen4)     #Back 버튼 클릭 시 전 화면(Screen4)으로 연결
        self.pushButton.clicked.connect(self.gotoScreen5)       #Enter 버튼 클릭 시 다음 화면(Screen5)으로 연결

        # dateEdit의 값을 현재 날짜로 설정하기
        self.currentDate = QDate.currentDate()
        self.dateEdit.setDate(self.currentDate)

        self.dateEdit.dateChanged.connect(self.dateFn)  #날짜에 변동이 생기면 dateFn 함수 실행
        self.lineEdit.textChanged.connect(self.lineFn)  #텍스트에 변동이 생기면 lineFn 함수 실행

    def gotoScreen4(self):  #Screen4로 연결
        screen4 = Screen4()
        widget.addWidget(screen4)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def gotoScreen5(self):
        global dataframe, con, fridge, sort     #전역변수

        current = datetime.now()    #현재 날짜
        date_to_compare = datetime.strptime("%d%d%d" % (self.year, self.month, self.day), "%Y%m%d") #입력 받은 년월일 (유통기한)
        self.date_diff = date_to_compare - current  #유통기한 - 현재날짜로 남은 일수 계산하여 저장

        #정보들을 리스트로 저장하고 변환하여 dataframe에 추가
        df_list = [[fridge, sort, self.food_name, self.year, self.month, self.day, self.date_diff.days + 1]]
        df_new = pd.DataFrame(df_list,
                              columns=['Fridge', 'Sort', 'FoodName', '유통기한_year', '유통기한_month', '유통기한_day', 'DateRemaining'])
        dataframe = dataframe.append(df_new, ignore_index=True)

        print(dataframe)
        dataframe.to_sql("TABLE_FOOD", con, if_exists="replace", index=False)

        #Screen5로 연결
        screen5 = Screen5()
        widget.addWidget(screen5)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def dateFn(self):   #유통기한 관련 정보 저장
        print(self.dateEdit.date())
        date = self.dateEdit.date()
        self.year = self.dateEdit.date().year()
        self.month = self.dateEdit.date().month()
        self.day = self.dateEdit.date().day()
        print(self.year, self.month, self.day)

    def lineFn(self):   #음식이름 저장
        self.food_name = self.lineEdit.text()
        print(self.food_name)


class Screen7(QMainWindow):
    def __init__(self): # 포장용기 유무를 묻는 Screen7 실행
        super(Screen7, self).__init__()
        loadUi("takeout.ui", self)
        self.pushButton.clicked.connect(self.gotoScreen14)
        self.pushButton_2.clicked.connect(self.gotoScreen2)

    def gotoScreen2(self):  # Screen2로 연결
        screen2 = Screen2()
        widget.addWidget(screen2)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def gotoScreen14(self):     # Screen14로 연결
        screen14 = Screen14()
        widget.addWidget(screen14)
        widget.setCurrentIndex(widget.currentIndex() + 1)


class Screen8(QMainWindow):
    def __init__(self):      # 버릴 품목을 선택하는 Screen8 실행
        global dataframe
        super(Screen8, self).__init__()
        loadUi("select.ui", self)

        self.deletedf = dataframe[['FoodName', 'DateRemaining']]    # 화면에 띄울 dataframe 정보들
        
        self.rowCount = 0
        self.rowCount = len(self.deletedf)
        
        print(self.rowCount)
        
        self.setup()
        self.pushButton_9.clicked.connect(self.gotoScreen2)     #Back 버튼 눌렀을 때 전 화면(Screen2)으로 연결
        self.menu.clicked.connect(self.gotoScreen7)     # Next 버튼 눌렀을 때 다음 화면 (Screen7)으로 연결

    def setup(self):
        self.index_number = 0
        column_headers = ['FoodName', 'DateRemaining']
        self.tableWidget.setHorizontalHeaderLabels(column_headers)
        self.tableWidget.setRowCount(self.rowCount)
        for i in range(self.rowCount):
            for j in range(2):
                data = QTableWidgetItem(str(self.deletedf.iloc[i,j]))
                print(i, j)
                self.tableWidget.setItem(i, j, data)
                print(str(self.deletedf.iloc[i, j]))

        self.lineEdit.textChanged.connect(self.lineFn)

    def lineFn(self):
        self.index_number = int(self.lineEdit.text())
        print(self.index_number)

    def gotoScreen2(self):  # Screen2와 연결
        screen2 = Screen2()
        widget.addWidget(screen2)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def gotoScreen7(self):   # Screen7과 연결
        global dataframe, Count
        
        print(self.index_number)
        
        dataframe.drop(self.index_number - 1, axis=0, inplace=True) #axis 0: row, 1: column
        dataframe.reset_index(drop=True, inplace=True)
        Count = Count - 1
        
        print(dataframe)
        
        dataframe.to_sql("TABLE_FOOD", con, if_exists="replace", index=False)
        
        screen7 = Screen7()
        widget.addWidget(screen7)
        widget.setCurrentIndex(widget.currentIndex() + 1)


class Screen11(QMainWindow):
    def __init__(self):      # 분리수거법을 알려주는 Screen11 실행
        super(Screen11, self).__init__()
        loadUi("recycleall1.ui", self)
        self.menu.clicked.connect(self.gotoScreen12)    # Next 버튼을 눌렀을 때 다음화면(Screen12)으로 연결

    def gotoScreen12(self):     # Screen12와 연결
        screen12 = Screen12()
        widget.addWidget(screen12)
        widget.setCurrentIndex(widget.currentIndex() + 1)


class Screen12(QMainWindow):
    def __init__(self):      # 분리수거법을 알려주는 Screen12 실행
        super(Screen12, self).__init__()
        loadUi("recycleall2.ui", self)
        self.menu.clicked.connect(self.gotoScreen2)     # Menu 버튼을 눌렀을 때 메뉴화면(Screen2)으로 연결

    def gotoScreen2(self):  # 메뉴판으로 연결
        screen2 = Screen2()
        widget.addWidget(screen2)
        widget.setCurrentIndex(widget.currentIndex() + 1)


class Screen14(QMainWindow):
    def __init__(self):      # 포장용기 분리수거법을 알려주는 Screen14 실행
        super(Screen14, self).__init__()
        loadUi("recyle1.ui", self)
        self.menu.clicked.connect(self.gotoScreen15)     # Next 버튼을 눌렀을 때 다음화면(Screen15)으로 연결

    def gotoScreen15(self):      # Screen15으로 연결
        screen15 = Screen15()
        widget.addWidget(screen15)
        widget.setCurrentIndex(widget.currentIndex() + 1)


class Screen15(QMainWindow):
    def __init__(self):      # 포장용기 분리수거법을 알려주는 Screen15 실행
        super(Screen15, self).__init__()
        loadUi("recyle2.ui", self)
        self.menu.clicked.connect(self.gotoScreen2)     # Menu 버튼을 눌렀을 때 초기메뉴(Screen2)으로 연결

    def gotoScreen2(self):   # Screen2으로 연결
        screen2 = Screen2()
        widget.addWidget(screen2)
        widget.setCurrentIndex(widget.currentIndex() + 1)

        
class Fridge3(QDialog):
    def __init__(self):      # 냉장고 냉동고 선택을 묻는 Fridge3 실행
        super(Fridge3, self).__init__()
        loadUi("fridge3.ui", self)
        self.pushButton_3.clicked.connect(self.gotoScreen2)
        self.pushButton_1.clicked.connect(self.gotoDay)     #냉동고
        self.pushButton_2.clicked.connect(self.gotoDay_2)   #냉장고

    def gotoScreen2(self):  # Screen2와 연결
        screen2 = Screen2()
        widget.addWidget(screen2)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def gotoDay(self):  # 냉동고 선택시
        global fridge
        fridge = 0
        day = Day()     # Day와 연결
        widget.addWidget(day)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def gotoDay_2(self):    # 냉장고 선택시
        global fridge
        fridge = 1
        day = Day()     # Day와 연결
        widget.addWidget(day)
        widget.setCurrentIndex(widget.currentIndex() + 1)


class Day(QMainWindow):
    def __init__(self): # 남은 유통기한 요일을 출력해주는 Day 실행
        global dataframe, fridge, freezer, rf
        super(Day, self).__init__()
        loadUi("day.ui", self)

        if fridge == 0: #냉동고
            self.is_freezer = dataframe['Fridge'] == 0
            freezer = dataframe.loc[self.is_freezer, ['FoodName', 'DateRemaining']]
            self.rowCount = 0
            self.rowCount = len(freezer)
        else:   #냉장고
            self.is_rf = dataframe['Fridge'] == 1
            rf = dataframe.loc[self.is_rf, ['FoodName', 'DateRemaining']]
            self.rowCount = 0
            self.rowCount = len(rf)

        print(self.rowCount)

        self.setup()
        self.menu.clicked.connect(self.gotoRecommend)   # Next 버튼을 눌렀을 때 다음화면(Recommend)으로 연결
        self.pushButton_9.clicked.connect(self.gotoFridge3)  # Back 버튼을 눌렀을 때 그 전 화면(Fridge3)으로 연결

    def setup(self):
        global fridge, freezer, rf
        column_headers = ['FoodName', 'DateRemaining']
        self.tableWidget.setHorizontalHeaderLabels(column_headers)
        self.tableWidget.setRowCount(self.rowCount)
        for i in range(self.rowCount):
            for j in range(2):
                if fridge == 0:
                    data = str(freezer.iloc[i,j])
                    print(i, j)
                    self.tableWidget.setItem(i,j,QTableWidgetItem(data))
                    print(str(freezer.iloc[i,j]))
                else:
                    data = str(rf.iloc[i,j])
                    print(i, j)
                    self.tableWidget.setItem(i,j,QTableWidgetItem(data))
                    print(str(rf.iloc[i,j]))
    
    def gotoRecommend(self):    # Recommend창 으로 연결
        recommend=Recommend()
        widget.addWidget(recommend)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def gotoFridge3(self):   # Fridge창으로 연결
        fridge3 = Fridge3()
        widget.addWidget(fridge3)
        widget.setCurrentIndex(widget.currentIndex() + 1)


class Recommend(QMainWindow):
    def __init__(self):     # 음식을 추천해주는 Recommend 실행
        global dataframe, fridge, freezer, rf
        super(Recommend, self).__init__()
        loadUi("recommend.ui", self)

        if fridge == 0:
            self.sequence()     #정렬
            self.list_from_fz = freezer.values.tolist()     #데이터프레임을 리스트로 변환
            print(self.list_from_fz)
            
            self.fz_queue = []
            for i in self.list_from_fz:     #리스트 큐에 넣음
                self.fz_queue.append(i)
            print(self.fz_queue)

            self.fz_list = []
            self.count = len(self.fz_queue)
            for i in range(self.count):
                state = 0
                pop = self.fz_queue.pop(0)
                if len(self.fz_list) == 0:
                    self.fz_list.append(pop)
                else:
                    for j in range(len(self.fz_list)):
                        if self.fz_list[j][0] == pop[0]:
                            state = 1
                    if state == 0:
                        self.fz_list.append(pop)
            print(self.fz_list)
                            
            column_headers = ['FoodName', 'DateRemaining']
            self.fz_df = pd.DataFrame(self.fz_list, columns = column_headers) #freezer recommend dataframe
            self.rowCount = 0
            self.rowCount = len(self.fz_df)
            print(self.fz_df)
            
        else:
            self.sequence_2()
            self.list_from_rf = rf.values.tolist()
            print(self.list_from_rf)
            
            self.rf_queue = []
            for i in self.list_from_rf:     #리스트 큐에 넣음
                self.rf_queue.append(i)
            print(self.rf_queue)

            self.rf_list = []
            self.count = len(self.rf_queue)
            for i in range(self.count):
                state = 0
                pop = self.rf_queue.pop(0)
                if len(self.rf_list) == 0:
                    self.rf_list.append(pop)
                else:
                    for j in range(len(self.rf_list)):
                        if self.rf_list[j][0] == pop[0]:
                            state = 1
                    if state == 0:
                        self.rf_list.append(pop)
            print(self.rf_list)
                            
            column_headers = ['FoodName', 'DateRemaining']
            self.rf_df = pd.DataFrame(self.rf_list, columns = column_headers) #refridgerator recommend dataframe
            self.rowCount = 0
            self.rowCount = len(self.rf_df)
            print(self.rf_df)

        print(self.rowCount)

        self.setup()        
        self.menu.clicked.connect(self.gotoScreen2) # Menu 버튼을 클릭했을 때 메뉴화면(Screen2)로 연결


    def sequence(self):  # 냉동고 선택시
        global fridge, freezer
        freezer.sort_values(by=['DateRemaining'],axis=0,inplace=True)
        freezer.reset_index(drop=True, inplace=True)
        print(freezer)

    def sequence_2(self):    # 냉장고 선택시
        global fridge, rf
        rf.sort_values(by=['DateRemaining'],axis=0,inplace=True)
        rf.reset_index(drop=True, inplace=True)
        print(rf)

    def setup(self):
        global fridge
        column_headers = ['FoodName', 'DateRemaining']
        self.tableWidget.setHorizontalHeaderLabels(column_headers)
        self.tableWidget.setRowCount(self.rowCount)
        for i in range(self.rowCount):
            for j in range(2):
                if fridge == 0:
                    data = str(self.fz_df.iloc[i,j])
                    print(i, j)
                    self.tableWidget.setItem(i,j,QTableWidgetItem(data))
                    print(str(self.fz_df.iloc[i,j]))
                else:
                    data = str(self.rf_df.iloc[i,j])
                    print(i, j)
                    self.tableWidget.setItem(i,j,QTableWidgetItem(data))
                    print(str(self.rf_df.iloc[i,j]))

    def gotoScreen2(self):   # Screen2로 연결
        screen2 = Screen2()
        widget.addWidget(screen2)
        widget.setCurrentIndex(widget.currentIndex() + 1)


## main code ## 

app = QApplication(sys.argv)
widget = QtWidgets.QStackedWidget() #메인 위젯 호출
mainwindow = MainWindow()           #메인 윈도우 호출
widget.addWidget(mainwindow)        #메인 윈도우라는 위젯을 추가
widget.setFixedHeight(430)          #높이 고정
widget.setFixedWidth(400)           #넓이 고정
widget.setWindowTitle("Eco-Fridge") #Window 맨 위의 프로그램 이름 설정
widget.show()                       #widget을 show

dataframe.to_sql("TABLE_FOOD", con, if_exists="replace", index=False) #dataframe을 db에 저장

try:
    sys.exit(app.exec_())   #프로그램을 이벤트 루프로 진입시킨다.
                            #프로그램을 무한루프 안에서 계속 실행시켜 주면서 프로그램에서 발생하는 이벤트를 처리해 준다.
except:
    print("Exiting")        #프로그램 종료
