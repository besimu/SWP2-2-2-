import pickle
import sys
from PyQt5.QtWidgets import (QWidget, QPushButton,
    QHBoxLayout, QVBoxLayout, QApplication, QLabel,
    QComboBox, QTextEdit, QLineEdit)
from PyQt5.QtCore import Qt


class ScoreDB(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
        self.dbfilename = 'assignment6.dat'
        self.scoredb = []
        self.readScoreDB()
        self.showScoreDB()

    def initUI(self):
        name = QLabel('Name:')
        age = QLabel('Age:')
        score = QLabel('Score:')
        amount = QLabel('Amount:')
        key = QLabel('Key:')
        result = QLabel('Result:')

        self.nameEdit = QLineEdit()
        self.ageEdit = QLineEdit()
        self.scoreEdit = QLineEdit()
        self.amountEdit = QLineEdit()
        self.keyEdit = QComboBox()
        self.resultEdit = QTextEdit()

        self.keyEdit.addItem('Name')
        self.keyEdit.addItem('Age')
        self.keyEdit.addItem('Score')

        addButton = QPushButton('Add')
        delButton = QPushButton('Del')
        findButton = QPushButton('Find')
        incButton = QPushButton('Inc')
        showButton = QPushButton('show')

        hbox1 = QHBoxLayout()
        hbox1.addStretch(1)
        hbox1.addWidget(name)
        hbox1.addWidget(self.nameEdit)
        hbox1.addWidget(age)
        hbox1.addWidget(self.ageEdit)
        hbox1.addWidget(score)
        hbox1.addWidget(self.scoreEdit)

        hbox2 = QHBoxLayout()
        hbox2.addStretch(1)
        hbox2.addWidget(amount)
        hbox2.addWidget(self.amountEdit)
        hbox2.addWidget(key)
        hbox2.addWidget(self.keyEdit)

        hbox3 = QHBoxLayout()
        hbox3.addStretch(1)
        hbox3.addWidget(addButton)
        hbox3.addWidget(delButton)
        hbox3.addWidget(findButton)
        hbox3.addWidget(incButton)
        hbox3.addWidget(showButton)

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)
        vbox.addLayout(hbox3)
        vbox.addWidget(result)
        vbox.addWidget(self.resultEdit)

        addButton.clicked.connect(self.addButtonClicked)
        delButton.clicked.connect(self.delButtonClicked)
        findButton.clicked.connect(self.findButtonClicked)
        incButton.clicked.connect(self.incButtonClicked)
        showButton.clicked.connect(self.showButtonClicked)

        self.setLayout(vbox)

        self.setGeometry(300, 300, 500, 250)
        self.setWindowTitle('Assignment6')
        self.show()

    def addButtonClicked(self):
        nameText = self.nameEdit.text()
        ageText = int(self.ageEdit.text())
        scoreText = int(self.scoreEdit.text())
        self.scoredb.append({'Name':nameText, 'Age':ageText, 'Score':scoreText})
        self.showScoreDB()

    def delButtonClicked(self):
        nameText = self.nameEdit.text()
        copy_scdb = self.scoredb.copy()
        for p in copy_scdb:
            if p['Name'] == nameText:
                self.scoredb.remove(p)
        self.showScoreDB()

    def findButtonClicked(self):
        nameText = self.nameEdit.text()
        for p in self.scoredb:
            if p['Name'] == nameText:
                self.showScoreDB(nameText)

    def incButtonClicked(self):
        nameText = self.nameEdit.text()
        amountText = int(self.amountEdit.text())
        for p in self.scoredb:
            if p['Name'] == nameText:
                p['Score'] = str(int(p['Score']) + int(amountText))
        self.showScoreDB()

    def showButtonClicked(self):
        text = ''
        keyname = self.keyEdit.currentText()
        for p in sorted(self.scoredb, key=lambda person: person[keyname]):
            for attr in sorted(p):
                text += attr + "=" + str(p[attr]) + "\t"
            text += "\n"
        self.resultEdit.setText(text)

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

    def showScoreDB(self, name=None):
        text = ''
        keyname = self.keyEdit.currentText()
        for p in sorted(self.scoredb, key=lambda person: person[keyname]):
            if (name == None):
                for attr in sorted(p):
                    text += attr + "=" + str(p[attr]) + "\t"
                text += "\n"
            elif (name != None and name == p['Name']):
                for attr in sorted(p):
                    text += attr + "=" + str(p[attr]) + "\t"
                text += "\n"
            else:
                continue
        self.resultEdit.setText(text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ScoreDB()
    sys.exit(app.exec_())
