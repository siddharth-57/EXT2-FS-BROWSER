from PyQt5 import QtCore  
from PyQt5.QtCore import Qt
from PyQt5 import QtGui
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QTableWidget, QVBoxLayout,QTableWidgetItem,QGridLayout, QButtonGroup, QHeaderView
import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow, QTabWidget, QWidget, QVBoxLayout, QScrollArea, QLabel, QHBoxLayout, QTreeView, QTextEdit
import random
from PyQt5.QtGui import QIcon, QStandardItemModel, QStandardItem
from pro import output
import math as m

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(924, 581)
        self.tabWidget = QtWidgets.QTabWidget(MainWindow)
        self.tabWidget.setGeometry(QtCore.QRect(20, 10, 1001, 781))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("taba")
        self.cur_group = 0
        self.no = int(input("Enter No. of Ext 2 Partitions To Be Shown : "))
        self.part = []
        for i in range(self.no):
            s = input(f"Enter Label of the Partition {i+1} : ")
            self.part.append(s)
        self.a = self.part[0]
        #scroll
        self.verticalLayout = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea = QtWidgets.QScrollArea(self.tab)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1218, 1218))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frame = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_4.addWidget(self.frame)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)

        self.part_buttons = []
        self.btn_grp_4 = QButtonGroup()
        self.btn_grp_4.setExclusive(True)
        self.btn_grp_4.buttonClicked.connect(self.on_click_grp_4)
        self.btn_grp_4.idClicked.connect(self.change_id_4)
                
        for i in range(self.no):
            self.pushButton = QtWidgets.QPushButton(self.tab,clicked=lambda:self.show_file_system())
            self.pushButton.setGeometry(QtCore.QRect(700+i*150, 50, 150, 100))        #(x,y,width,height)
            self.pushButton.setObjectName("pushButton")
            self.pushButton.setStyleSheet("background-color: #bdbcc4;")
            self.pushButton.setText(self.part[i]) 
            self.part_buttons.append(self.pushButton)
            self.btn_grp_4.addButton(self.pushButton,i)
                        
        #inode and file name input section
        #inode number and file name text labels
        self.label= QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(400, 650, 251, 51))
        font = QtGui.QFont()
        font.setFamily("Nimbus Mono PS [urw]")
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label.setStyleSheet("background-color: #bdbcc4;")

        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(400, 750, 251, 51))
        font = QtGui.QFont()
        font.setFamily("Nimbus Mono PS [urw]")
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_2.setStyleSheet("background-color: #bdbcc4;")

        #TEXT INPUT
        self.lineEdit = QtWidgets.QLineEdit(self.tab)
        self.lineEdit.setGeometry(QtCore.QRect(700, 650, 381, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lineEdit.setFont(font)
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setStyleSheet("background-color: #bdbcc4;")        
        
        self.lineEdit_2 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_2.setGeometry(QtCore.QRect(700, 750, 381, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lineEdit_2.setFont(font)
        self.lineEdit.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setStyleSheet("background-color: #bdbcc4;")        
        
        #ENTER BUTTONS
        self.pushButton_5 = QtWidgets.QPushButton(self.tab,clicked=lambda:self.show_inode_input())
        self.pushButton_5.setGeometry(QtCore.QRect(1100,650, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.setStyleSheet("background-color: #bdbcc4;")        

        self.pushButton_6 = QtWidgets.QPushButton(self.tab,clicked=lambda:self.show_file_input())
        self.pushButton_6.setGeometry(QtCore.QRect(1100,750, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_6.setStyleSheet("background-color: #bdbcc4;")
        
        self.tabWidget.addTab(self.tab, "")
        MainWindow.setCentralWidget(self.tabWidget)
        
        #menu bar
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 924, 20))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        
        #status bar
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        
        self.subSplitter = None
        self.subButtons = []
        self.cur = -1
        self.cur_2 = -1
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        #SETTING UP THE CLOSE BUTTON FOR TABS
        self.tabWidget.setTabsClosable(True)
        tabs = self.tabWidget

        #main window tab cannot be closed
        def close_tab(index):
            tab = tabs.widget(index)
            if tab.objectName() != "taba":
                tabs.removeTab(index)
        tabs.tabCloseRequested.connect(close_tab)
        
        #ADDING COLOUR TO THE UI
        self.tabWidget.setStyleSheet("background-color: #012169;")
        self.tabWidget.tabBar().setStyleSheet("color: #bdbcc4;font-weight: bold;")

    def show_inode_input(self):
        self.show_inode_structure(self.lineEdit.text())
    
    def show_file_input(self):
        out = output(self.a,str(self.cur_group),'6')
        l = out.split("\n")
        for i in range(len(l)):
            l[i] = l[i].split(" ")
            if(len(l[i]) > 3):
                j = 0
                while(len(l[i]) != 3):
                    l[i][j] = l[i][j] + " " + l[i][j+1]
                    l[i].remove(l[i][j+1])
        
        inode_no = ''
        for j in range(len(l)):
            if(len(l[j]) == 3):
                if self.lineEdit_2.text() == l[j][0]:
                    inode_no = l[j][1]
                    break

        if(inode_no == ''):
            return
        
        self.show_inode_structure(inode_no)

    def change_id_4(self, id):
        self.prev_2 = self.cur_2
        self.cur_2 = id
        self.a = self.part[id]
    
    def on_click_grp_4(self,btn):
        if(self.prev_2 != -1):
            self.btn_grp_4.button(self.prev_2).setStyleSheet("background-color: #bdbcc4;")
        self.btn_grp_4.button(self.cur_2).setStyleSheet("background-color: #ff571a;")
        if(self.prev_2 != self.cur_2 and self.cur != -1 and self.cur_1 != -1):
            self.btn_grp.button(self.cur).setStyleSheet("background-color: #bdbcc4;")
            self.btn_grp_3.button(self.cur_1).setStyleSheet("background-color: #bdbcc4;")
    
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "GUI FOR EXT2 FILE SYSTEM"))
        self.pushButton_5.setText(_translate("MainWindow", "ENTER"))
        self.pushButton_6.setText(_translate("MainWindow", "ENTER"))
        self.label.setText(_translate("MainWindow", "ENTER INODE NUMBER:"))
        self.label_2.setText(_translate("MainWindow", "ENTER FILE NAME:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "MAIN WINDOW"))

    def show_file_system(self):
            out = output(self.a,str(self.cur_group),'8')
            coun = int(out)
            a = min(coun,380)-1    
            if not self.subSplitter:
                #setting rest of the buttons to the white
                self.subSplitter = QtWidgets.QSplitter(self.frame)
                self.subSplitter.setOrientation(QtCore.Qt.Horizontal)
                self.subSplitter.setObjectName("subSplitter")
                self.subSplitter.setStyleSheet("background-color: #bdbcc4;")
                self.btn_grp = QButtonGroup()
                self.btn_grp.setExclusive(True)
                self.btn_grp.buttonClicked.connect(self.on_click_grp)
                self.btn_grp.idClicked.connect(self.change_id_2)
                subButton = QtWidgets.QPushButton(self.frame)
                subButton.setObjectName("BOOT SECTOR")
                subButton.setText("BOOT SECTOR")
                self.subButtons.append(subButton)

                a=0
                for i in range(min(coun,380)):
                    subButton = QtWidgets.QPushButton(self.subSplitter,clicked=lambda:self.show_block_group())
                    subButton.setObjectName("BLOCK GROUP {}".format(i))
                    subButton.setText("BLOCK GROUP {}".format(i))
                    self.btn_grp.addButton(subButton,i)
                    self.subButtons.append(subButton)
                    a+=1
                self.subSplitter.setGeometry(QtCore.QRect(100, 200, 150*a, 121))
            
            self.frame.setMinimumSize(QtCore.QSize(151*a, 800))
            self.subSplitter.show()

    def change_id_2(self, id):
        self.prev = self.cur
        self.cur = id
    
    def on_click_grp(self,btn):
        self.cur_group = self.btn_grp.id(btn)
        if self.prev != -1:
            self.btn_grp.button(self.prev).setStyleSheet("background-color: #bdbcc4;")
        self.btn_grp.button(self.cur).setStyleSheet("background-color: #ff571a;")
    
    def show_block_group(self):     
        self.subSplitter = QtWidgets.QSplitter(self.tab)
        self.subSplitter.setGeometry(QtCore.QRect(450, 450, 1000, 121))
        self.subSplitter.setOrientation(QtCore.Qt.Horizontal)
        self.subSplitter.setObjectName("subSplitter")
        self.subSplitter.setStyleSheet("background-color: #bdbcc4;")
        self.btn_grp_3 = QButtonGroup()
        self.btn_grp_3.setExclusive(True)
        self.btn_grp_3.buttonClicked.connect(self.on_click_grp_10)
        self.btn_grp_3.idClicked.connect(self.change_id_3)
        self.cur_1 = -1
        subButton = QtWidgets.QPushButton(self.subSplitter,clicked=lambda:self.show_super_block())
        subButton.setObjectName("SUPER BLOCK")
        subButton.setText("SUPER BLOCK")
        self.btn_grp_3.addButton(subButton,0)
        subButton = QtWidgets.QPushButton(self.subSplitter,clicked=lambda:self.show_block_group_desc())
        subButton.setObjectName("BLOCK GROUP DESCRIPTOR")
        subButton.setText("BLOCK GROUP DESCRIPTOR")
        self.btn_grp_3.addButton(subButton,1)
        subButton = QtWidgets.QPushButton(self.subSplitter,clicked=lambda:self.show_block_bitmap())
        subButton.setObjectName("BLOCK BIT MAP")
        subButton.setText("BLOCK BIT MAP")
        self.btn_grp_3.addButton(subButton,2)
        subButton = QtWidgets.QPushButton(self.subSplitter,clicked=lambda:self.show_inode_bitmap())
        subButton.setObjectName("INODE BITMAP")
        subButton.setText("INODE BITMAP")
        self.btn_grp_3.addButton(subButton,3)
        subButton = QtWidgets.QPushButton(self.subSplitter,clicked=lambda:self.show_inode_table())
        subButton.setObjectName("INODE TABLE")
        subButton.setText("INODE TABLE")
        self.btn_grp_3.addButton(subButton,4)
        subButton = QtWidgets.QPushButton(self.subSplitter,clicked=lambda:self.show_data_block())
        subButton.setObjectName("DATA BLOCKS")
        subButton.setText("DATA BLOCKS")
        self.btn_grp_3.addButton(subButton,5)
        self.subButtons.append(subButton)
        self.subSplitter.show()

    def change_id_3(self, id):
        self.prev_1 = self.cur_1
        self.cur_1 = id
    
    def on_click_grp_10(self,btn):
        if self.prev_1 != -1:
            self.btn_grp_3.button(self.prev_1).setStyleSheet("background-color: #bdbcc4;")
        self.btn_grp_3.button(self.cur_1).setStyleSheet("background-color: #ff571a;")
    
    def show_super_block(self):
        out = output(self.a,str(self.cur_group),'0')
        l = out.split("\n")
        self.tab_8 = QtWidgets.QWidget()
        self.tab_8.setObjectName("tab_8")
        table = QTableWidget()
        table.setColumnCount(2)
        table.setRowCount(11)
        table.setHorizontalHeaderLabels(['Field', 'Value'])
        table.verticalHeader().setVisible(False)
        table.horizontalHeader().setSectionResizeMode(0, QHeaderView.Stretch)
        table.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)
        table.setStyleSheet("background-color: #bdbcc4;")
        # Add the superblock fields to the table
        table.setItem(0, 0, QTableWidgetItem('Inodes count'))
        table.setItem(0, 1, QTableWidgetItem(l[0]))
        table.setItem(1, 0, QTableWidgetItem('Blocks count'))
        table.setItem(1, 1, QTableWidgetItem(l[1]))
        table.setItem(2, 0, QTableWidgetItem('Clusters Per Group'))
        table.setItem(2, 1, QTableWidgetItem(l[2]))
        table.setItem(3, 0, QTableWidgetItem('Free blocks count'))
        table.setItem(3, 1, QTableWidgetItem(l[3]))
        table.setItem(4, 0, QTableWidgetItem('Free inodes count'))
        table.setItem(4, 1, QTableWidgetItem(l[4]))
        table.setItem(5, 0, QTableWidgetItem('First Data Block'))
        table.setItem(5, 1, QTableWidgetItem(l[5]))
        table.setItem(6, 0, QTableWidgetItem('Block size'))
        table.setItem(6, 1, QTableWidgetItem(l[6]))
        table.setItem(7, 0, QTableWidgetItem('# Blocks per group'))
        table.setItem(7, 1, QTableWidgetItem(l[7]))
        table.setItem(8, 0, QTableWidgetItem('# Inodes per group'))
        table.setItem(8, 1, QTableWidgetItem(l[8]))
        table.setItem(9, 0, QTableWidgetItem('Inodes Size'))
        table.setItem(9, 1, QTableWidgetItem(l[9]))
        table.setItem(10, 0, QTableWidgetItem('Magic signature'))
        table.setItem(10, 1, QTableWidgetItem(l[10]))
        
        # Add the table to the window
        self.main_layout = QVBoxLayout()
        self.main_layout.addWidget(table)
        self.tab_8.setLayout(self.main_layout)
        self.tabWidget.addTab(self.tab_8, "SUPER BLOCK")
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        _translate = QtCore.QCoreApplication.translate
        self.tab_8.setWindowTitle(_translate("MainWindow", "MainWindow"))
        
    def show_inode_table(self):
        out = output(self.a,str(self.cur_group),'4')
        l = out.split("\n")
        for i in range(len(l)-1):
            l[i] = l[i].split(" ")
            l[i].insert(0,str(i+1))
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")

        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tab_3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.scrollArea = QtWidgets.QScrollArea(self.tab_3)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1218, 1218))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frame_2 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_4.addWidget(self.frame_2)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_2.addWidget(self.scrollArea)

        self.pushButton_ = {}

        b=1
        for a in range(1,2):   #number of inodes = 11-1=10
            for i in range(1,8):    #7 push buttons in each row 
                self.pushButton_[b] = QtWidgets.QPushButton(self.frame_2)
                self.pushButton_[b].setGeometry(QtCore.QRect(300+(i*160), 5+(a*60), 160, 50))    #x,y,width,height
                self.pushButton_[b].setObjectName("pushButton_" + str(b))
                if(i == 1):
                    self.pushButton_[b].setStyleSheet("background-color: #7CB9E8;")
                else:
                    self.pushButton_[b].setStyleSheet("background-color: #bdbcc4;")
                b+=1

        f=8
        self.btn_grp_1 = QButtonGroup()
        self.btn_grp_1.setExclusive(True)
        self.btn_grp_1.buttonClicked.connect(self.on_click_grp_1)
        for r in range(1,(len(l))):   #number of inodes=30
            for o in range(1,9):    #8 push buttons in each row 
                self.pushButton_[f] = QtWidgets.QPushButton(self.frame_2)
                self.pushButton_[f].setGeometry(QtCore.QRect(140+(o*160),65+(r*60),160,50))    #x,y,width,height
                self.pushButton_[f].setObjectName("pushButton_" + str(f))
                if(o == 2):
                    self.btn_grp_1.addButton(self.pushButton_[f],o)
                    self.pushButton_[f].setStyleSheet("background-color: #7CB9E8;")
                else:    
                    self.pushButton_[f].setStyleSheet("background-color: #bdbcc4;")
                f+=1
        
        self.frame_2.setMinimumSize(QtCore.QSize(10,f*8)) #dynamically allocating the window size based on the number of inodes

        self.tabWidget.addTab(self.tab_3, "INODE TABLE")
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        _translate = QtCore.QCoreApplication.translate
        self.tab_3.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_[1].setText(_translate("MainWindow", "inode no."))
        self.pushButton_[2].setText(_translate("MainWindow", "i_uid"))
        self.pushButton_[3].setText(_translate("MainWindow", "i_size"))
        self.pushButton_[4].setText(_translate("MainWindow", "i_gid"))
        self.pushButton_[5].setText(_translate("MainWindow", "i_links_count"))
        self.pushButton_[6].setText(_translate("MainWindow", "i_blocks"))
        self.pushButton_[7].setText(_translate("MainWindow", "i_flags"))
        n = -1
        # this for loop is the code for numbering the push buttons from 1-10 of first column
        if l[0] == '':
            pass
        else:
            for j in range(8, len(self.pushButton_)+1):
                if((j) % 8 == 0):
                    n += 1
                self.pushButton_[j].setText(l[n][(j)%8])

    def on_click_grp_1(self,btn):
        self.show_inode_structure(btn.text())

    def show_inode_structure(self,inode_no):
        out = output(self.a,str(self.cur_group),'5'+inode_no)
        self.l = out.split("\n")
        self.l[0] = self.l[0].split(" ")
        self.sz = int(self.l[0][len(self.l[0])-1])
        self.l[0].remove(str(self.sz))
        self.l.remove('')
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        button_layout = QHBoxLayout()
        self.show_buttons = []
        n = 1
        self.label_3 = QtWidgets.QLabel(self.tab_6)
        self.label_3.setGeometry(QtCore.QRect(200, 100, 1051, 51))
        font = QtGui.QFont()
        font.setFamily("Nimbus Mono PS [urw]")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_3.setStyleSheet("background-color: #bdbcc4;")
        s = ""
        a1 = ["inode no.: ","i_size: ","i_links_count: ","i_blocks: "]
        for k in range(len(self.l[0])):
            s += a1[k] + self.l[0][k] + "    "
        self.label_3.setText(s)
        for i in range(12):
            if(n < len(self.l)):
                show_button = QPushButton(self.l[n])
            else:
                show_button = QPushButton('-')
            show_button.setStyleSheet("background-color: #7CB9E8;")
            self.show_buttons.append(show_button)
            button_layout.addWidget(show_button)
            n += 1

        for i in range(3):
            if(i == 0):
                if(n < len(self.l)):
                    show_button = QPushButton(self.l[n])
                else:
                    show_button = QPushButton('-')
            elif(i == 1):
                if(14+self.sz < len(self.l)):
                    show_button = QPushButton(self.l[14+self.sz])
                else:
                    show_button = QPushButton('-')
            elif(i == 2):
                if(14+self.sz+self.sz+self.sz*self.sz < len(self.l)):
                    show_button = QPushButton(self.l[14+self.sz+self.sz+self.sz*self.sz])
                else:
                    show_button = QPushButton('-')
            show_button.clicked.connect(getattr(self, f'show_scrollable_area_{i+1}'))
            show_button.setStyleSheet("background-color: #7CB9E8;")
            self.show_buttons.append(show_button)
            button_layout.addWidget(show_button)
            n += 1

        # Create the horizontal layout for the scrollable areas
        scrollable_areas_layout = QHBoxLayout()
        self.scrollable_areas = []
        for i in range(3):
            scrollable_area = ScrollableArea(f'Scrollable Area {i+1}',self.sz)
            scrollable_area.setStyleSheet("background-color: #bdbcc4;")       #setting colour for scrollable areas change it later 
            setattr(self, f'scrollable_area_{i+1}', scrollable_area)
            self.scrollable_areas.append(scrollable_area)
            scrollable_areas_layout.addWidget(scrollable_area)

        # Add the button layout and scrollable areas layout to the main layout
        self.scrollable_areas[0].btn_grp.buttonClicked.connect(self.on_click_1)
        self.scrollable_areas[1].btn_grp.buttonClicked.connect(self.on_click_2)
        self.main_layout = QVBoxLayout()
        self.main_layout.addLayout(button_layout)
        self.main_layout.addLayout(scrollable_areas_layout)
        self.tab_6.setLayout(self.main_layout)
        self.tabWidget.addTab(self.tab_6, "INODE DATA")
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

    def show_scrollable_area_1(self):
        self.sel = 1
        self.show_scrollable_areas(1)
        if(len(self.l) < 14):
            return
        else:
            for i in range(self.sz):
                if(i+14 < len(self.l)):
                    self.edit_button_text(i,self.l[i+14])
                else:
                    self.edit_button_text(i,'-')
        
    def show_scrollable_area_2(self):
        self.sel = 2
        self.show_scrollable_areas(2)
        if(len(self.l) < (14+self.sz+1)):
            return
        else:
            for i in range(self.sz):
                if((i+(14+self.sz+1)+self.sz*i) < len(self.l)):
                    self.edit_button_text(i,self.l[i+(14+self.sz+1)+self.sz*i])
                else:
                    self.edit_button_text(i,'-')
        
        if(len(self.l) < (14+self.sz+2)):
            return
        else:
            for i in range(self.sz):
                if(i+14+self.sz+2 < len(self.l)):
                    self.edit_button_text(i+self.sz,self.l[i+14+self.sz+2])
                else:
                    self.edit_button_text(i+self.sz,'-')

    def show_scrollable_area_3(self):
        self.sel = 3
        self.show_scrollable_areas(3)
        if(len(self.l) < (14+self.sz+self.sz+self.sz*self.sz+1)):
            return
        else:
            for i in range(self.sz):
                if((i+14+self.sz+self.sz+self.sz*self.sz+1+self.sz*self.sz*i) < len(self.l)):
                    self.edit_button_text(i,self.l[i+14+self.sz+self.sz+self.sz*self.sz+1+self.sz*self.sz*i])
                else:
                    self.edit_button_text(i,'-')
        
        if(len(self.l) < (14+self.sz+self.sz*self.sz+self.sz+2)):
            return
        else:
            for i in range(self.sz):
                if(i+14+self.sz+self.sz*self.sz+self.sz+2+self.sz*i < len(self.l)):
                    self.edit_button_text(i+self.sz,self.l[i+14+self.sz+self.sz*self.sz+self.sz+2+self.sz*i])
                else:
                    self.edit_button_text(i+self.sz,'-')
        
        if(len(self.l) < (14+self.sz+self.sz*self.sz+self.sz+3)):
            return
        else:
            for i in range(self.sz):
                if(i+14+self.sz+self.sz*self.sz+self.sz+3 < len(self.l)):
                    self.edit_button_text(i+self.sz*2,self.l[i+14+self.sz+self.sz*self.sz+self.sz+3])
                else:
                    self.edit_button_text(i+self.sz*2,'-')

    def show_scrollable_areas(self, num_areas):
        for i in range(num_areas):
            self.scrollable_areas[i].setVisible(True)
        for i in range(num_areas, 3):
            self.scrollable_areas[i].setVisible(False)
    
    def edit_button_text(self, index, text):
        if 0 <= index < self.sz:
            self.scrollable_areas[0].btn_grp.button(index).setText(text)
        elif self.sz <= index < self.sz*2:
            self.scrollable_areas[1].btn_grp.button(index - self.sz).setText(text)
        elif self.sz*2 <= index < self.sz*3:
            self.scrollable_areas[2].btn_grp.button(index - self.sz*2).setText(text)

    def on_click_1(self, btn):  
        if(self.sel == 1):
            return 
        else:
            a1 = self.l.index(btn.text())
            if(len(self.l) < (a1+1)):
                return
            else:
                for i in range(self.sz):
                    if((i+a1+1) < len(self.l)):
                        self.edit_button_text(i+self.sz,self.l[i+a1+1])
                    else:
                        self.edit_button_text(i+self.sz,'-')
        
    def on_click_2(self, btn):
        if(self.sel == 3):
            a1 = self.l.index(btn.text())
            if(len(self.l) < (a1+1)):
                return
            else:
                for i in range(self.sz):
                    if((i+a1+1) < len(self.l)):
                        self.edit_button_text(i+self.sz,self.l[i+a1+1])
                    else:
                        self.edit_button_text(i+self.sz,'-') 
        else:
            return
    
    def show_block_group_desc(self):
        out = output(self.a,str(self.cur_group),'1')
        l = out.split("\n")
        for i in range(len(l)-1):
            l[i] = l[i].split(" ")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")

        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.scrollArea = QtWidgets.QScrollArea(self.tab_2)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1218, 1218))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frame_2 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_4.addWidget(self.frame_2)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_2.addWidget(self.scrollArea)
        
        
        self.pushButton_ = {}

        self.btn_grp_2 = QButtonGroup()
        self.btn_grp_2.setExclusive(True)
        self.btn_grp_2.buttonClicked.connect(self.on_click_bgdesc)
        self.btn_grp_2.idClicked.connect(self.change_id)
        b=1
        for a in range(1,len(l)):   #number of block group desc = 11-1=10
            self.label_4 = QtWidgets.QLabel(self.frame_2)
            self.label_4.setGeometry(QtCore.QRect(181+50,(a*120), 150, 91))
            self.label_4.setStyleSheet("background-color: #bdbcc4;")
            self.label_4.setText("Group "+str(a-1))
            font = QtGui.QFont()
            font.setFamily("Nimbus Mono PS [urw]")
            font.setPointSize(18)
            font.setWeight(1000)
            font.setBold(True)
            font.setItalic(False)
            font.setUnderline(False)
            font.setWeight(50)
            font.setStrikeOut(False)
            self.label_4.setFont(font)
            self.label_4.setAlignment(QtCore.Qt.AlignCenter)
            for i in range(1,7):    #6 push buttons in each block desc 
                self.pushButton_[b] = QtWidgets.QPushButton(self.frame_2)
                self.pushButton_[b].setGeometry(QtCore.QRect(200+(i*181),(a*120), 181, 91))    #x,y,width,height
                self.pushButton_[b].setObjectName("pushButton_" + str(b))
                if(i < 4):    
                    self.pushButton_[b].setStyleSheet("background-color: #7CB9E8;")
                else:
                    self.pushButton_[b].setStyleSheet("background-color: #bdbcc4;")
                self.btn_grp_2.addButton(self.pushButton_[b],b-1)
                b+=1
        self.frame_2.setMinimumSize(QtCore.QSize(1000, b*21))

        self.tabWidget.addTab(self.tab_2, "GROUP DESCRIPTORS")
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        labels = ["BLOCKS BITMAP", "INODES BITMAP", "INODES TABLE", "FREE BLOCKS COUNT", "FREE INODES COUNT", "DIRECTORIES COUNT"]  #index 0-5
        n = -1
        for j in range(1, len(self.pushButton_)+1):
            if((j-1) % 6 == 0):
                n += 1
            self.pushButton_[j].setText(labels[(j-1)%6]+":\n"+l[n][(j-1)%6])  
                
    def change_id(self, id):
        self.id = id

    def on_click_bgdesc(self, btn):
        txt = btn.text()
        self.cur_group = int(m.floor(self.id/6))
        #print(self.cur_group)
        if(txt[:6] == "BLOCKS"):
            self.show_block_bitmap()
        if(txt[:8] == "INODES B"):
            self.show_inode_bitmap()
        if(txt[:8] == "INODES T"):
            self.show_inode_table()
        if(txt[:6] == "DIRECT"):
            self.show_data_block()

    def show_block_bitmap(self):
        out = output(self.a,str(self.cur_group),'2')
        l1 = out.split()
        #print(l1)
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")

        # create a vertical layout for the tab widget
        self.verticalLayout = QtWidgets.QVBoxLayout(self.tab_4)
        self.verticalLayout.setObjectName("verticalLayout")

        # create a scroll area widget
        self.scrollArea = QtWidgets.QScrollArea(self.tab_4)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")

        # create a widget to hold the scrollable content
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1218, 1218))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")

        # create a vertical layout for the scrollable content
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_4.setObjectName("verticalLayout_4")

        # create a frame to hold the push buttons
        self.frame = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        # create a grid layout for the frame
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")

        self.pushButton_ = {}

        i = 1
        for l in range(1, 70): #for number of rows creating 30 rows
            for k in range(1, 140): #for number of columns creating 30 columns
                self.pushButton_[i] = QtWidgets.QPushButton(self.frame)
                self.pushButton_[i].setObjectName("pushButton_" + str(k*l))
                self.pushButton_[i].setStyleSheet("background-color: #bdbcc4;")
                self.gridLayout.addWidget(self.pushButton_[i], l-1, k-1, 1, 1)
                i += 1

        # add the frame to the vertical layout
        self.verticalLayout_4.addWidget(self.frame)

        # set the scrollable content widget for the scroll area
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        # add the scroll area to the vertical layout
        self.verticalLayout.addWidget(self.scrollArea)

        self.tabWidget.addTab(self.tab_4, "BLOCK BITMAP")
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_grp_6 = QButtonGroup()
        self.btn_grp_6.setExclusive(True)
        self.btn_grp_6.buttonClicked.connect(self.show_data_block)
        
        #numbering the push buttons
        for j in range(1,len(self.pushButton_)+1):
            self.pushButton_[j].setText(l1[j-1])
            if l1[j-1] == '1':
                self.pushButton_[j].setStyleSheet("background-color: #7CB9E8;")
                self.btn_grp_6.addButton(self.pushButton_[j],j-1)

    def show_inode_bitmap(self):
        out1 = output(self.a,str(self.cur_group),'3')
        l2 = out1.split()
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")

        # create a vertical layout for the tab widget
        self.verticalLayout = QtWidgets.QVBoxLayout(self.tab_5)
        self.verticalLayout.setObjectName("verticalLayout")

        # create a scroll area widget
        self.scrollArea = QtWidgets.QScrollArea(self.tab_5)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")

        # create a widget to hold the scrollable content
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1218, 1218))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")

        # create a vertical layout for the scrollable content
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_4.setObjectName("verticalLayout_4")

        # create a frame to hold the push buttons
        self.frame = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        # create a grid layout for the frame
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")

        self.pushButton_ = {}

        i = 1
        for l in range(1,70): #for number of rows creating 40 rows
            for k in range(1,140):    #for number of columns creating 40 clmns 
                self.pushButton_[i] = QtWidgets.QPushButton(self.frame)
                self.pushButton_[i].setObjectName("pushButton_" + str(k*l))
                self.pushButton_[i].setStyleSheet("background-color: #bdbcc4;")
                self.gridLayout.addWidget(self.pushButton_[i],l, k, 1, 1)
                i += 1

        # add the frame to the vertical layout
        self.verticalLayout_4.addWidget(self.frame)

        # set the scrollable content widget for the scroll area
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        # add the scroll area to the vertical layout
        self.verticalLayout.addWidget(self.scrollArea)

        self.tabWidget.addTab(self.tab_5, "INODE BITMAP")
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_grp_5 = QButtonGroup()
        self.btn_grp_5.setExclusive(True)
        self.btn_grp_5.buttonClicked.connect(self.show_inode_table)
        
        #numbering the push buttons
        for j in range(1,len(self.pushButton_)+1):
            self.pushButton_[j].setText(l2[j-1])
            if l2[j-1] == '1':
                self.pushButton_[j].setStyleSheet("background-color: #7CB9E8;")
                self.btn_grp_5.addButton(self.pushButton_[j],j-1)

    def show_data_block(self):
        out = output(self.a,str(self.cur_group),'6')
        l = out.split("\n")
        for i in range(len(l)):
            l[i] = l[i].split(" ")
            if(len(l[i]) > 3):
                j = 0
                while(len(l[i]) != 3):
                    l[i][j] = l[i][j] + " " + l[i][j+1]
                    l[i].remove(l[i][j+1])
            
        j = 0
        l1 = []
        l1.append('2')
        for i in l:
            if len(i) == 3:
                l1.append(i[1])
        
        #print(l)
        self.tab_7 = QtWidgets.QWidget()
        self.tab_7.setObjectName("tab_7")

        self.tree_view = QTreeView()
        self.tree_view.setHeaderHidden(True)
        self.tree_view.setRootIsDecorated(True)
        self.tree_view.setAnimated(True)

        # Set up the model
        self.model = QStandardItemModel()
        self.model.setColumnCount(3)
        self.tree_view.setHeaderHidden(False)
        self.model.setHorizontalHeaderLabels(['Name', 'Inode No.', 'File Type'])

        # Add the root directory to the model
        items = {}
        items[0] = QStandardItem('Root')

        self.model.appendRow([items[0], QStandardItem('2'), QStandardItem('2')])
        n = 1
        while(j < (len(l))):
            if(len(l[j]) == 1):
                x = l[j][0]
                j += 1
                while(j < (len(l)) and len(l[j]) != 1):
                    items[n] = QStandardItem(l[j][0])
                    items[l1.index(x)].appendRow([items[n], QStandardItem(l[j][1]), QStandardItem(l[j][2])])
                    j += 1
                    n += 1
        
        # Set the model for the tree view
        self.tree_view.setModel(self.model)
        self.tree_view.setStyleSheet("background-color: lightgray;")
        # Create a layout for the buttons
        button_layout = QHBoxLayout()
        self.show_button = QPushButton('Show')
        self.show_button.setStyleSheet("background-color: #bdbcc4;")
        self.show_button.clicked.connect(self.show_file)
        button_layout.addWidget(self.show_button)

        self.main_layout = QVBoxLayout()
        self.main_layout.addWidget(self.tree_view)
        self.main_layout.addLayout(button_layout)
        self.tab_7.setLayout(self.main_layout)
        # Add the tree view and button layout to the main layout

        self.tabWidget.addTab(self.tab_7, "DATA BLOCKS")
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
    
    def show_file(self):
        # Get the selected item from the tree view
        selected = self.tree_view.selectedIndexes()
        if len(selected) > 0:
            item1 = self.model.itemFromIndex(selected[0]) 
            item = self.model.itemFromIndex(selected[1])
            item2 = self.model.itemFromIndex(selected[2])
            if(item2.text() == '1'):
                self.display_file(item1.text(),item.text())
            else:
                pass
                    
    def display_file(self, title, inode):
        out = output(self.a,str(self.cur_group),'7'+inode)
        self.tab_8 = QtWidgets.QWidget()
        self.tab_8.setObjectName("tab_8")
        self.textbox = QTextEdit(self.tab_8)
        self.textbox.setStyleSheet("background-color: lightgray;")
        self.textbox.move(10, 10)
        self.textbox.resize(1500, 900)
        self.textbox.setText(out)
        self.tabWidget.addTab(self.tab_8, title)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

class ScrollableArea(QWidget):
    def __init__(self, name, sz):
        super().__init__()
        self.setWindowTitle(name)
        self.setGeometry(100, 100, 300, 300)
        self.sz = sz
        self.initUI()
        
    def initUI(self):
        # Create the vertical layout for the buttons
        button_layout = QVBoxLayout()
        button = {}
        self.btn_grp = QButtonGroup()
        self.btn_grp.setExclusive(True)
        self.btn_grp.buttonClicked.connect(self.on_click)

        # Add 100 rectangular buttons to the layout
        for i in range(self.sz):
            button[i] = QPushButton(f'{i}', self)
            self.btn_grp.addButton(button[i],i)
            button_layout.addWidget(button[i],i)

        # Create the scrollable area
        scrollable_area = QScrollArea()
        scrollable_area.setWidgetResizable(True)
        scrollable_area.setMaximumWidth(200)
        scrollable_area.setMaximumHeight(500)
        # Add the button layout to the scrollable area
        scrollable_widget = QWidget()
        scrollable_widget.setLayout(button_layout)
        scrollable_area.setWidget(scrollable_widget)

        # Add the scrollable area to the main layout
        self.main_layout = QVBoxLayout()
        self.main_layout.addWidget(scrollable_area)
        self.setLayout(self.main_layout)

    def on_click(self,btn):
        pass
    
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
