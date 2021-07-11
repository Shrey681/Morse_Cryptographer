from PyQt5 import QtCore, QtGui, QtWidgets

import speech_recognition as s_r 

MORSE_CODE_DICT = {'A': '.-', 'B': '-...',
                   'C': '-.-.', 'D': '-..', 'E': '.',
                   'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-',
                   'L': '.-..', 'M': '--', 'N': '-.',
                   'O': '---', 'P': '.--.', 'Q': '--.-',
                   'R': '.-.', 'S': '...', 'T': '-',
                   'U': '..-', 'V': '...-', 'W': '.--',
                   'X': '-..-', 'Y': '-.--', 'Z': '--..',
                   '1': '.----', '2': '..---', '3': '...--',
                   '4': '....-', '5': '.....', '6': '-....',
                   '7': '--...', '8': '---..', '9': '----.',
                   '0': '-----', ', ': '--..--', '.': '.-.-.-',
                   '?': '..--..', '/': '-..-.', '-': '-....-',
                   '(': '-.--.', ')': '-.--.-',' ':'/'
                   }

def audio_to_morse():
    r = s_r.Recognizer()
    my_mic = s_r.Microphone(device_index=None)  # my device index is 1, you have to put your device index
    with my_mic as source:
        print("Say now!!!!")
        r.adjust_for_ambient_noise(source) 
        audio = r.listen(source)  # take voice input from the microphone
    audio_text = r.recognize_google(audio).upper()
    print(r.recognize_google(audio))  # to print voice into text
    output = text_to_morse(audio_text)
    return output

def morse_to_text(message):
    lst = message.split()
    message += ' '
    decipher = ''
    for item in range(len(lst)):
        decipher += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT.values()).index(lst[item])]
        #decipher += ''
    return decipher

def text_to_morse(mesg):
    inp = mesg.upper()
    cipher = ''
    for letter in inp:
        cipher += MORSE_CODE_DICT[letter] + ' '
    return cipher

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(789, 919)
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        MainWindow.setStyleSheet("background-color: rgb(7, 55, 74);")

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.title_frame = QtWidgets.QFrame(self.centralwidget)
        self.title_frame.setGeometry(QtCore.QRect(0, 0, 791, 101))
        self.title_frame.setMaximumSize(QtCore.QSize(791, 16777215))
        self.title_frame.setStyleSheet("background-color: rgb(37, 183, 159);")
        self.title_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.title_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.title_frame.setObjectName("title_frame")
        
        self.title = QtWidgets.QLabel(self.title_frame)
        self.title.setEnabled(True)
        self.title.setGeometry(QtCore.QRect(260, 40, 261, 21))
        
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        
        self.title.setFont(font)
        self.title.setObjectName("title")
        
        self.about_the_project_frame = QtWidgets.QFrame(self.centralwidget)
        self.about_the_project_frame.setGeometry(QtCore.QRect(0, 110, 791, 201))
        self.about_the_project_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.about_the_project_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.about_the_project_frame.setObjectName("about_the_project_frame")
        self.about_the_project_label = QtWidgets.QLabel(self.about_the_project_frame)
        self.about_the_project_label.setGeometry(QtCore.QRect(90, 50, 251, 101))
        
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(15)
        
        self.about_the_project_label.setFont(font)
        self.about_the_project_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.about_the_project_label.setObjectName("about_the_project_label")
        
        self.about_the_project_details_label = QtWidgets.QLabel(self.about_the_project_frame)
        self.about_the_project_details_label.setGeometry(QtCore.QRect(450, -10, 341, 221))
        self.about_the_project_details_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.about_the_project_details_label.setObjectName("about_the_project_details_label")
        
        self.textmorse_groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.textmorse_groupBox.setGeometry(QtCore.QRect(10, 330, 751, 251))
        self.textmorse_groupBox.setStyleSheet("color: rgb(255, 255, 255);")
        self.textmorse_groupBox.setObjectName("textmorse_groupBox")
        
        self.TxtInp_label = QtWidgets.QLabel(self.textmorse_groupBox)
        self.TxtInp_label.setGeometry(QtCore.QRect(30, 40, 71, 16))
        
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        
        self.TxtInp_label.setFont(font)
        self.TxtInp_label.setObjectName("TxtInp_label")
        self.TxtInp_plainTextEdit = QtWidgets.QPlainTextEdit(self.textmorse_groupBox)
        self.TxtInp_plainTextEdit.setGeometry(QtCore.QRect(140, 30, 601, 41))
        self.TxtInp_plainTextEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 12pt \"MS Sans Serif\";\n"
"border-color: rgb(255, 255, 255);\n""color: #000;\n"
"")
        self.TxtInp_plainTextEdit.setObjectName("TxtInp_plainTextEdit")

        self.submit_pushButton = QtWidgets.QPushButton(self.textmorse_groupBox)
        self.submit_pushButton.setGeometry(QtCore.QRect(260, 100, 121, 31))
        self.submit_pushButton.setStyleSheet("background-color: rgb(37, 183, 159);\n"
"border-color: rgb(255, 255, 255);\n"
"padding: 5px;")
        self.submit_pushButton.setObjectName("submit_pushButton")
        self.submit_pushButton.clicked.connect(self.t_to_m)

        self.audioInp_pushButton_3 = QtWidgets.QPushButton(self.textmorse_groupBox)
        self.audioInp_pushButton_3.setGeometry(QtCore.QRect(430, 100, 121, 31))
        self.audioInp_pushButton_3.setStyleSheet("background-color: rgb(37, 183, 159);\n"
"border-color: rgb(255, 255, 255);\n"
"padding: 5px;")
        self.audioInp_pushButton_3.setObjectName("audioInp_pushButton_3")
        self.audioInp_pushButton_3.clicked.connect(self.a_to_m)

        self.output_label = QtWidgets.QLabel(self.textmorse_groupBox)
        self.output_label.setGeometry(QtCore.QRect(40, 170, 51, 16))
        
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        
        self.output_label.setFont(font)
        self.output_label.setObjectName("output_label")
        
        self.morseoutput_frame = QtWidgets.QFrame(self.textmorse_groupBox)
        self.morseoutput_frame.setGeometry(QtCore.QRect(140, 160, 601, 41))
        self.morseoutput_frame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.morseoutput_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.morseoutput_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.morseoutput_frame.setObjectName("morseoutput_frame")
        self.morseoutput_frame.raise_()
        
        self.TxtInp_label.raise_()
        self.TxtInp_plainTextEdit.raise_()
        
        self.submit_pushButton.raise_()
        self.audioInp_pushButton_3.raise_()
        self.output_label.raise_()
        
        self.morsetext_groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.morsetext_groupBox.setGeometry(QtCore.QRect(10, 610, 751, 251))
        self.morsetext_groupBox.setStyleSheet("color: rgb(255, 255, 255);")
        self.morsetext_groupBox.setObjectName("morsetext_groupBox")
        
        self.MorseInp_label = QtWidgets.QLabel(self.morsetext_groupBox)
        self.MorseInp_label.setGeometry(QtCore.QRect(30, 40, 91, 16))
        
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        
        self.MorseInp_label.setFont(font)
        self.MorseInp_label.setObjectName("MorseInp_label")
        
        self.TxtInp_plainTextEdit_2 = QtWidgets.QPlainTextEdit(self.morsetext_groupBox)
        self.TxtInp_plainTextEdit_2.setGeometry(QtCore.QRect(140, 30, 601, 41))
        self.TxtInp_plainTextEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 14pt \"MS Sans Serif\";\n"
"border-color: rgb(255, 255, 255);\n""color: #000;\n"
"")
        self.TxtInp_plainTextEdit_2.setObjectName("TxtInp_plainTextEdit_2")
        
        self.submit_pushButton_2 = QtWidgets.QPushButton(self.morsetext_groupBox)
        self.submit_pushButton_2.setGeometry(QtCore.QRect(350, 100, 121, 31))
        self.submit_pushButton_2.setStyleSheet("background-color: rgb(37, 183, 159);\n"
"border-color: rgb(255, 255, 255);\n"
"padding: 5px;")
        self.submit_pushButton_2.setObjectName("submit_pushButton_2")
        self.submit_pushButton_2.clicked.connect(self.m_to_t)

        self.output_label_2 = QtWidgets.QLabel(self.morsetext_groupBox)
        self.output_label_2.setGeometry(QtCore.QRect(40, 170, 51, 16))
        
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        
        self.output_label_2.setFont(font)
        self.output_label_2.setObjectName("output_label_2")
        
        self.textoutput_frame = QtWidgets.QFrame(self.morsetext_groupBox)
        self.textoutput_frame.setGeometry(QtCore.QRect(140, 160, 601, 41))
        self.textoutput_frame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textoutput_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.textoutput_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.textoutput_frame.setObjectName("textoutput_frame")

        self.outputText_label = QtWidgets.QLabel(self.textmorse_groupBox)
        self.outputText_label.setGeometry(QtCore.QRect(140, 160, 601, 41))
        self.outputText_label.setStyleSheet("color: #000000;background-color: #fff; font-size: 14pt")
        self.outputText_label.setText("")
        self.outputText_label.raise_()

        self.outputText_label_2 = QtWidgets.QLabel(self.morsetext_groupBox)
        self.outputText_label_2.setGeometry(QtCore.QRect(140, 160, 601, 41))
        self.outputText_label_2.setStyleSheet("color: #000000;background-color: #fff; font-size: 12pt")
        self.outputText_label_2.setText("")
        self.outputText_label_2.raise_()
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.title.setText(_translate("MainWindow", "MORSE CRYPTOGRAPHER"))
        self.about_the_project_label.setText(_translate("MainWindow", "About the Project"))
        self.about_the_project_details_label.setText(_translate("MainWindow", "This project is to better understand morse code.\n"
"\n"
"Features:\n"
"Encoding Text to Morse Code\n"
"Decoding Morse Code to Text\n"
"\n"
"Encoding Audio Text to Morse Code"))
        self.textmorse_groupBox.setTitle(_translate("MainWindow", "Text to Morse"))
        self.TxtInp_label.setText(_translate("MainWindow", "Text Input"))
        self.submit_pushButton.setText(_translate("MainWindow", "SUBMIT"))
        self.audioInp_pushButton_3.setText(_translate("MainWindow", "AUDIO"))
        self.output_label.setText(_translate("MainWindow", "Output"))
        self.morsetext_groupBox.setTitle(_translate("MainWindow", "Morse to Text"))
        self.MorseInp_label.setText(_translate("MainWindow", "Morse Input"))
        self.submit_pushButton_2.setText(_translate("MainWindow", "SUBMIT"))
        self.output_label_2.setText(_translate("MainWindow", "Output"))

    def a_to_m(self):
        self.outputText_label.setText(audio_to_morse())
        self.outputText_label.adjustSize()
    def t_to_m(self):
        self.outputText_label.setText(text_to_morse(self.TxtInp_plainTextEdit.toPlainText()))
        self.outputText_label.adjustSize()
    def m_to_t(self):
        self.outputText_label_2.setText(morse_to_text(self.TxtInp_plainTextEdit_2.toPlainText()))
        self.outputText_label_2.adjustSize()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())