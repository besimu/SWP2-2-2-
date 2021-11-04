import pickle
import sys
from PyQt5.QtWidgets import (QWidget, QPushButton, QApplication, QLabel,
                             QComboBox, QTextEdit, QLineEdit, QGridLayout)


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

        add = QPushButton("Add")
        delete = QPushButton("Delete")
        find = QPushButton("Find")
        inc = QPushButton("Increase")
        show = QPushButton("Show")

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

        grid.addWidget(add, 3, 1)
        grid.addWidget(delete, 3, 2)
        grid.addWidget(find, 3, 3)
        grid.addWidget(inc, 3, 4)
        grid.addWidget(show, 3, 5)

        grid.addWidget(self.result, 4, 1, 8, 5)

        self.setLayout(grid)

        add.clicked.connect(self.addDB)
        show.clicked.connect(self.showScoreDB)
        delete.clicked.connect(self.delDB)
        find.clicked.connect(self.findDB)
        inc.clicked.connect(self.incDB)

        self.setGeometry(300, 300, 300, 250)
        self.setWindowTitle('Assignment6 by 20171676')
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
            self.scoredb = pickle.load(fH)
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

    def showScoreDB(self):
        keyname = self.key.currentText()
        self.result.setText("")
        for p in sorted(self.scoredb, key=lambda person: person[keyname]):
            self.result.append(
                "Age = " + str(p['Age']) + "    Name = " + p['Name'] + "        Score = " + str(p['Score']))

    def addDB(self):
        if self.age.text().isdigit() and self.score.text().isdigit():
            record = {'Name': self.name.text(), 'Age': int(self.age.text()), 'Score': int(self.score.text())}
            self.scoredb += [record]
            self.showScoreDB()

    def delDB(self):
        for i in range(len(self.scoredb)):
            for p in self.scoredb:
                if p['Name'] == self.name.text():
                    self.scoredb.remove(p)
                    break
        self.showScoreDB()

    def findDB(self):
        self.result.setText("")
        for p in self.scoredb:
            if p['Name'] == self.name.text():
                self.result.append(
                    "Age = " + str(p['Age']) + "    Name = " + p['Name'] + "        Score = " + str(p['Score']))

    def incDB(self):
        if self.amount.text().isdigit():
            amount = int(self.amount.text())
            for i in self.scoredb:
                i['Score'] = int(i['Score'])
                if i['Name'] == self.name.text():
                    i['Score'] += amount
            self.showScoreDB()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ScoreDB()
    sys.exit(app.exec_())
