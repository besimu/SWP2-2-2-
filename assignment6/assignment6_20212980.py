import pickle
import sys
from PyQt5.QtWidgets import (QWidget, QPushButton,
    QHBoxLayout, QVBoxLayout, QApplication, QLabel,
    QComboBox, QTextEdit, QLineEdit, QGridLayout)
from PyQt5.QtCore import Qt


class ScoreDB(QWidget):
    def __init__(self):

        super().__init__()

        self.name = QLineEdit()
        self.age = QLineEdit()
        self.score = QLineEdit()
        self.amount = QLineEdit()
        self.key = QComboBox()

        self.result = QTextEdit()

        self.key.addItem("Name", 1)
        self.key.addItem("Age", 2)
        self.key.addItem("Score", 3)

        self.dbfilename = 'assignment6.dat'
        self.scoredb = []
        self.readScoreDB()
        self.initUI()
        self.showScoreDB()

    def initUI(self):
        grid = QGridLayout()
        grid.setSpacing(10)

        name_label = QLabel("Name :", self)
        age_label = QLabel("Age :", self)
        score_label = QLabel("Score :", self)
        amount_label = QLabel("Amount :", self)
        key_label = QLabel("Key :", self)
        result_label = QLabel("Result :", self)

        add_button = QPushButton("Add")
        del_button = QPushButton("Del")
        find_button = QPushButton("Find")
        inc_button = QPushButton("Inc")
        show_button = QPushButton("Show")

        grid.addWidget(name_label, 1, 0)
        grid.addWidget(age_label, 1, 2)
        grid.addWidget(score_label, 1, 4)
        grid.addWidget(amount_label, 2, 2)
        grid.addWidget(key_label, 2, 4)
        grid.addWidget(result_label, 4, 0)

        grid.addWidget(self.name, 1, 1)
        grid.addWidget(self.age, 1, 3)
        grid.addWidget(self.score, 1, 5)
        grid.addWidget(self.amount, 2, 3)
        grid.addWidget(self.key, 2, 5)

        grid.addWidget(add_button, 3, 1)
        grid.addWidget(del_button, 3, 2)
        grid.addWidget(find_button, 3, 3)
        grid.addWidget(inc_button, 3, 4)
        grid.addWidget(show_button, 3, 5)

        grid.addWidget(self.result, 4, 1, 8, 5)

        self.setLayout(grid)

        add_button.clicked.connect(self.AddDB)
        del_button.clicked.connect(self.DelDB)
        find_button.clicked.connect(self.FindDB)
        inc_button.clicked.connect(self.IncDB)
        show_button.clicked.connect(self.showScoreDB)

        self.setGeometry(300, 300, 500, 250)
        self.setWindowTitle('Assignment6')
        self.show()

    def closeEvent(self, event):
        self.writeScoreDB()

    def readScoreDB(self):
        try:
            fH = open(self.dbfilename, 'rb')
        except FileNotFoundError as e:
            self.scoredb = []
            return

        try:
            self.scoredb =  pickle.load(fH)
        except:
            pass
        else:
            pass
        fH.close()


    # write the data into person db
    def writeScoreDB(self):
        fH = open(self.dbfilename, 'wb')
        pickle.dump(self.scoredb, fH)
        fH.close()

    def AddDB(self):
        name = self.name.text()
        age = int(self.age.text())
        score = int(self.score.text())
        self.scoredb.append({'Name': name,'Age': age,'Score':score})
        self.showScoreDB()


    def DelDB(self):
        name = self.name.text()
        copy = self.scoredb.copy()
        for i in copy:
            if i['Name'] == name:
                self.scoredb.remove(i)
        self.showScoreDB()

    def FindDB(self):
        name = self.name.text()
        for i in self.scoredb:
            if i['Name'] == name:
                self.showScoreDB(name)


    def IncDB(self):
        name = self.name.text()
        amount = int(self.amount.text())

        for i in self.scoredb:
            if i['Name'] == name:
                i['Score'] = int(i['Score']) + amount
        self.showScoreDB()



    def Show(self):
        text = ''
        keyname = self.key.currentText()
        self.result.setText("")
        if self.key == 'Name':
            self.scoredb.sort(key=lambda x: int(x[3]))
        elif self.key == 'Age':
            self.scoredb.sort(key=lambda x: int(x[1]))
        else:
            self.scoredb.sort(key=lambda x: int(x[5]))
        
        for p in sorted(self.scoredb, key=lambda person: person[keyname]):
            for attr in sorted(p):
                text += attr + "=" + str(p[attr]) + "\t"
            text += "\n"
        self.result.setText(text)

    def showScoreDB(self, name=None):
        text = ''
        keyname = self.key.currentText()
        for i in sorted(self.scoredb, key=lambda person: person[keyname]):
            if (name == None):
                for attr in sorted(i):
                    text += attr + "=" + str(i[attr]) + "\t"
                text += "\n"
            elif (name != None and name == i['Name']):
                for attr in sorted(i):
                    text += attr + "=" + str(i[attr]) + "\t"
                text += "\n"
            else:
                continue
            self.result.setText(text)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ScoreDB()
    sys.exit(app.exec_())
