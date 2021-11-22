# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'worker.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
import re
from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
import stringprep

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(541, 600)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(157, 155, 159))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(147, 147, 147))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(157, 155, 159))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        MainWindow.setPalette(palette)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 61, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 40, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 80, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 120, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 160, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")

        #To define the inName widget
        self.inName = QtWidgets.QLineEdit(self.centralwidget)
        self.inName.setGeometry(QtCore.QRect(70, 0, 461, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.inName.setFont(font)
        self.inName.setObjectName("inName")

        # To define the inID widget
        self.inID = QtWidgets.QLineEdit(self.centralwidget)
        self.inID.setGeometry(QtCore.QRect(90, 40, 441, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.inID.setFont(font)
        self.inID.setObjectName("inID")

        # To define the inAdd widget
        self.inAdd = QtWidgets.QLineEdit(self.centralwidget)
        self.inAdd.setGeometry(QtCore.QRect(90, 80, 441, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.inAdd.setFont(font)
        self.inAdd.setObjectName("inAdd")

        # To define the inPhone widget
        self.inPhone = QtWidgets.QLineEdit(self.centralwidget)
        self.inPhone.setGeometry(QtCore.QRect(140, 120, 391, 31))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.inPhone.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.inPhone.setFont(font)
        self.inPhone.setObjectName("inPhone")

        # To define the inMail widget
        self.inMail = QtWidgets.QLineEdit(self.centralwidget)
        self.inMail.setGeometry(QtCore.QRect(70, 160, 461, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.inMail.setFont(font)
        self.inMail.setObjectName("inMail")

        # To define the Add button
        self.btnAdd = QtWidgets.QPushButton(self.centralwidget,  clicked = lambda:self.add_it())
        self.btnAdd.setGeometry(QtCore.QRect(10, 210, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btnAdd.setFont(font)
        self.btnAdd.setObjectName("btnAdd")

        # To define the Edit button
        self.btnEdit = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.edit_it())
        self.btnEdit.setGeometry(QtCore.QRect(100, 210, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btnEdit.setFont(font)
        self.btnEdit.setObjectName("btnEdit")

        # To define the Modify button
        self.btnModify = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.modify_it())
        self.btnModify.setGeometry(QtCore.QRect(190, 210, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btnModify.setFont(font)
        self.btnModify.setObjectName("btnModify")

        # To define the Delete button
        self.btnDelete = QtWidgets.QPushButton(self.centralwidget, clicked= lambda : self.delete_it())
        self.btnDelete.setGeometry(QtCore.QRect(280, 210, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btnDelete.setFont(font)
        self.btnDelete.setObjectName("btnDelete")


        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(10, 250, 141, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")


        self.lsWorkers = QtWidgets.QListWidget(self.centralwidget)
        self.lsWorkers.setGeometry(QtCore.QRect(10, 280, 521, 291))
        self.lsWorkers.setFrameShape(QtWidgets.QFrame.Box)
        self.lsWorkers.setObjectName("lsWorkers")


        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 541, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def show_it(self):

        try:
            conn = sqlite3.connect("worker_book.db")
            c = conn.cursor()
            c.execute("SELECT * from workers")

            #get all the records fromt the DB in a list of tuples:

            records=c.fetchall()

            #transform it to a list of strings
            ls=[]
            for i in records:
                tmp=''
                for j in i:
                    tmp+=' '+str(j)

                tmp=tmp[1:]
                ls.append(tmp)
            try:
                #print the strings into the workers list
                self.lsWorkers.addItems(ls)

            except Exception as e:
                print("adding the items in the workers list is stopped :  ", e)
            else:
                print("adding the items in the workers list is done ")

        except Exception as err:

            print("Error while transferring Data from database to the workers list", err)

        else:
            print("transfer completed")
            conn.commit()

        finally:

            # c.execute("SELECT * from workers")
            # print(c.fetchall())
            c.close()
            conn.close()

    def delete_it(self):

        # Grab the selected row or current row
        clicked = self.lsWorkers.currentRow()

        #grab the elements of each row

        name, id, post_address, phone, address =self.lsWorkers.currentItem().text().split(' ')

        #Delete the item from the database :
        conn = sqlite3.connect("worker_book.db")
        c = conn.cursor()
        try:
            #delete the row where you find the same id
            tmp=(id,'')
            c.execute(f"DELETE FROM workers WHERE id in {tmp}")

        except Exception as err:
            print("deletion not completed : ",err)
        else:
            print("deletion completed")
            conn.commit()
        finally:
            c.close()
            conn.close()



        #Delete the item from the worker list:
        self.lsWorkers.takeItem(clicked)

    def modify_add_it(self,name,id,post_address,phone,address):

        # Forming the row
        ch = name + ' ' + id + ' ' + post_address + ' ' + phone + ' ' + address

        # creating the email pattern :
        pattern_email = "[a-zA-Z0-9]+[@][a-zA-Z]+[.][a-zA-Z]+"

        # creating the phone pattern:
        pattern_phone = "[+][0-9]{1,3}[0-9]"

        # handling the exceptions
        if not (re.findall(pattern_email, address)) or not (re.findall(pattern_phone, phone)):
            if not (re.findall(pattern_email, address)):  # if EmailAddressFormatException :

                # change the color of the text to red!

                self.inMail.clear()
                self.inMail.setStyleSheet("color: rgb(255, 0, 0);")
                self.inMail.setText(address)

            if not (re.findall(pattern_phone, phone)):  # if PhoneNumberFormatException :

                # change the color of the text to red!

                self.inPhone.clear()
                self.inPhone.setStyleSheet("color: rgb(255, 0, 0);")
                self.inPhone.setText(phone)
        else:  # if all the items are in the right format

            # add the line into the lsWorkers
            self.lsWorkers.addItem(ch)

            # reset the widgets
            self.inMail.clear()
            self.inMail.setStyleSheet("color: rgb(0, 0, 0);")
            self.inPhone.clear()
            self.inPhone.setStyleSheet("color: rgb(0, 0, 0);")
            self.inAdd.clear()
            self.inName.clear()
            self.inID.clear()




    def modify_it(self):

        try:

            if self.lsWorkers.currentRow() != -1: #if an item is selected in the workers list and not modified yet
                # Grab the selected row or current row
                c = self.lsWorkers.currentRow()

                #form the items
                name, id, post_address, phone, address =self.lsWorkers.currentItem().text().split(' ')

                #put back the items to their corresponsing widgets

                self.inName.setText(str(name))
                self.inID.setText(str(id))
                self.inPhone.setText(str(phone))
                self.inAdd.setText(str(post_address))
                self.inMail.setText(str(address))

                #remove the item from the list
                self.lsWorkers.takeItem(self.lsWorkers.currentRow())


            else:
                #if an item is modified and to be returned to the listbox

                # Grab the Item from the widgets:
                name = self.inName.text()
                id = self.inID.text()
                post_address = self.inAdd.text()
                address = self.inMail.text()
                phone = self.inPhone.text()
                print(phone)

                #add them to the workers list box:
                self.modify_add_it(name,id,post_address,str(phone),address)


            # reset the current row to -1
            self.lsWorkers.setCurrentRow(-1)


        except Exception as err :
            print("the action was not completed: ",err)
        else:
            print("Action successfully completed")


    def edit_it(self):

        try:

            if self.lsWorkers.currentRow() != -1:  # if an item is selected in the workers list and not modified yet
                # Grab the selected row or current row
                c = self.lsWorkers.currentRow()

                # form the items
                name, id, post_address, phone, address = self.lsWorkers.currentItem().text().split(' ')

                # put back the items to their corresponding widgets

                self.inName.setText(str(name))
                self.inID.setText(str(id))
                self.inPhone.setText(str(phone))
                self.inAdd.setText(str(post_address))
                self.inMail.setText(str(address))

                # remove the item from the list
                self.lsWorkers.takeItem(self.lsWorkers.currentRow())

                #remove the row from the database:
                conn = sqlite3.connect("worker_book.db")
                c = conn.cursor()
                try:
                    # delete the row where you find the same id
                    tmp = (id, '')
                    c.execute(f"DELETE FROM workers WHERE id in {tmp}")

                except Exception as err:
                    print("removing from the DB not completed : ", err)
                else:
                    print("removing completed")
                    conn.commit()
                finally:
                    c.close()
                    conn.close()


            else:
                # if an item is modified and to be returned to the listbox

                # Grab the Item from the widgets:
                name = self.inName.text()
                id = self.inID.text()
                post_address = self.inAdd.text()
                address = self.inMail.text()
                phone = self.inPhone.text()

                # add them to the workers list box:
                self.modify_add_it(name, id, post_address, phone, address)

                #save it in the database
                try:
                    conn = sqlite3.connect("worker_book.db")
                    c = conn.cursor()
                    c.execute("INSERT INTO workers VALUES(?,?,?,?,?)",(name,id,post_address,str(phone),address))

                except Exception as err:

                    print("Error while inserting Data",err)

                else:
                    print("insert completed")
                    conn.commit()
                finally:

                    # c.execute("SELECT * from workers")
                    # print(c.fetchall())
                    c.close()
                    conn.close()


            # reset the current row to -1
            self.lsWorkers.setCurrentRow(-1)


        except Exception as err:
            print("the action was not completed: ", err)
        else:
            print("Action successfully completed")






    def add_it(self):

       # Grab the Items from the text Boxes:
       name = self.inName.text()
       id= self.inID.text()
       post_address=self.inAdd.text()
       address= self.inMail.text()
       phone=self.inPhone.text()

       self.modify_add_it(name,id,post_address,str(phone),address)

       #add the row to the database:
       try:
           conn = sqlite3.connect("worker_book.db")
           c = conn.cursor()

           c.execute("INSERT INTO workers VALUES(?,?,?,?,?)", (name, id, post_address, str(phone), address))



       except Exception as err:

           print("Error while inserting Data",err)

       else:
           print("insert completed")
           conn.commit()

       finally:

           # c.execute("SELECT * from workers")
           # print(c.fetchall())
           c.close()
           conn.close()



    def retranslateUi(self, MainWindow):

        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Workers"))
        self.label.setText(_translate("MainWindow", "Name:"))
        self.label_2.setText(_translate("MainWindow", "ID code:"))
        self.label_3.setText(_translate("MainWindow", "Address:"))
        self.label_4.setText(_translate("MainWindow", "Phone number:"))
        self.label_5.setText(_translate("MainWindow", "Email:"))
        self.inPhone.setText(_translate("MainWindow", "+36301234567"))
        self.btnAdd.setText(_translate("MainWindow", "Add"))
        self.btnEdit.setText(_translate("MainWindow", "Edit"))
        self.btnModify.setText(_translate("MainWindow", "Modify"))
        self.btnDelete.setText(_translate("MainWindow", "Delete"))
        self.label_6.setText(_translate("MainWindow", "List of persons:"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    #create a database
    conn = sqlite3.connect("worker_book.db")
    c=conn.cursor()

    # create a table inside the database
    c.execute("""CREATE TABLE workers(
                 Name text,
                 id text,
                 Postal text,
                 phone_num text,
                 Email text)""")

    #saving and closing the database
    conn.commit()
    conn.close()



    MainWindow.show()
    ui.show_it()

    sys.exit(app.exec_())
    ui.show_it()

