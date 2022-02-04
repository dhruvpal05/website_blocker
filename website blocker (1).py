from PyQt5 import QtWidgets
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QTimeEdit, QWidget, QWidgetItem
import mysql.connector as c
data=c.connect(host="localhost",user="root",passwd="1234",database="test")
from datetime import datetime as d

cur=data.cursor()

app=QApplication([])
mWin=QMainWindow()
window=QWidget()
mWin.setFixedSize(900, 660)
mWin.setCentralWidget(window)

#Web Address Text Field-->
webAdd=QtWidgets.QLineEdit(window)
webAdd.setPlaceholderText("Web Address")
webAdd.setGeometry(QtCore.QRect(60, 270, 361, 31))

#Web Address Label-->
label = QtWidgets.QLabel(window)
label.setText("Wesbite Address:")
label.setGeometry(QtCore.QRect(60, 240, 150, 21))
font=QtGui.QFont()
font.setFamily("Tw Cen MT")
font.setPointSize(12)
font.setBold(True)
font.setWeight(75)
label.setFont(font)

logo = QtWidgets.QLabel(window)
logo.setGeometry(QtCore.QRect(0, 23, 900, 151))
logo.setText("")
logo.setPixmap(QtGui.QPixmap("C:/Users/Satya Pal/Desktop/2021-09-29 (2)"))
logo.setAlignment(QtCore.Qt.AlignCenter)
logo.setIndent(-1)

startDate = QtWidgets.QDateEdit(window)
startDate.setGeometry(QtCore.QRect(60, 350, 171, 31))
startDate.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)

endDate = QtWidgets.QDateEdit(window)
endDate.setGeometry(QtCore.QRect(250, 350, 171, 31))

label_3 = QtWidgets.QLabel(window)
label_3.setText("From Date:")
label_3.setGeometry(QtCore.QRect(60, 330, 93, 13))
font = QtGui.QFont()
font.setFamily("Tw Cen MT")
font.setPointSize(12)
font.setBold(True)
font.setWeight(75)
label_3.setFont(font)

def onTodayClicked():
    startDate.setDate(QtCore.QDate.currentDate())

btnToday=QtWidgets.QPushButton(window)
btnToday.setText("Today")
btnToday.setGeometry(QtCore.QRect(60, 385, 50, 24))
btnToday.clicked.connect(onTodayClicked)

label_4 = QtWidgets.QLabel(window)
label_4.setText("To Date:")
label_4.setGeometry(QtCore.QRect(250, 330, 70, 13))
font = QtGui.QFont()
font.setFamily("Tw Cen MT")
font.setPointSize(12)
font.setBold(True)
font.setWeight(75)
label_4.setFont(font)

label_5=QtWidgets.QLabel(window)
label_5.setText("Blocking Timings:")
label_5.setGeometry(QtCore.QRect(60, 427, 150, 21))
font = QtGui.QFont()
font.setFamily("Tw Cen MT")
font.setPointSize(12)
font.setBold(True)
font.setWeight(75)
label_5.setFont(font)

label_6=QtWidgets.QLabel(window)
label_6.setText("From Time:")
label_6.setGeometry(QtCore.QRect(60, 455, 150, 17))
label_6.setFont(font)

label_7=QtWidgets.QLabel(window)
label_7.setText("To Time:")
label_7.setGeometry(QtCore.QRect(250, 455, 150, 17))
label_7.setFont(font)

startTime=QtWidgets.QTimeEdit(window)
startTime.setGeometry(QtCore.QRect(60, 480, 171, 31))

endTime=QTimeEdit(window)
endTime.setGeometry(QtCore.QRect(250, 480, 171, 31))

def onNowClicked():
    startTime.setTime(QtCore.QTime.currentTime())

btnNow=QtWidgets.QPushButton(window)
btnNow.setText("Now")
btnNow.setGeometry(QtCore.QRect(60, 515, 50, 24))
btnNow.clicked.connect(onNowClicked)

webs=[]

def onClick():
    web=[webAdd.text(), startDate.date().toPyDate().strftime("%m/%d/%Y"), startTime.time().toPyTime().strftime("%H:%M:%S"), endDate.date().toPyDate().strftime("%m/%d/%Y"), endTime.time().toPyTime().strftime("%H:%M:%S")]
    webs.append(web)
    print(webs)
    updateTable()


#BLOCK button coding:
blockBtn = QtWidgets.QPushButton(window)
blockBtn.setText("BLOCK")
blockBtn.setGeometry(QtCore.QRect(170, 550, 151, 41))
font = QtGui.QFont()
font.setFamily("Tw Cen MT")
font.setPointSize(16)
font.setBold(True)
font.setWeight(75)
blockBtn.setFont(font)
blockBtn.clicked.connect(onClick)

#Blocked Websites table coding:
tableBlocked = QtWidgets.QTableWidget(window)
tableBlocked.setColumnCount(5)
tableBlocked.setGeometry(QtCore.QRect(485, 215, 365, 395))
tableBlocked.verticalScrollBarPolicy()
print(tableBlocked.rowCount())


def addTableRow(table, row_data):
        row = table.rowCount()
        table.setRowCount(row+1)
        col = 0
        for item in row_data:
            cell = QTableWidgetItem(str(item))
            table.setItem(row, col, cell)
            col += 1

def updateTable():
    cur.execute("select * from webblocker;")
    for row in cur.fetchall():
        addTableRow(tableBlocked, list(row))

updateTable()


mWin.setWindowTitle("Wesbite Blocker ~By Vishal Vishwajeet & Dhruv Pal")
mWin.show()
app.exec()




for i in webs:
    query="insert into webblocker values('{}','{}','{}','{}','{}');".format(i[0],i[1],i[2],i[3],i[4])
    cur.execute(query)
    data.commit()

host="C:\Windows\System32\drivers\etc\hosts"
localip="127.0.0.1"

for j in webs:
    (j[1])<d.now().date().strftime("%m/%d/%Y")<(j[3])
    with open(host,"r+") as file:
        content=file.read()
        file.write("        "+localip+"       "+j[0]+"\n")
        print("done")
        for website in j[0]:
            if website in content:
                pass
            else:
                file.write("        "+localip+"       "+website+"\n")
                print("done")











