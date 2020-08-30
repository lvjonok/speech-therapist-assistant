from PyQt5 import QtGui, QtCore, QtWidgets
import sys, os
import source.tools.Constants as Constants  # pylint: disable=import-error
import pickle


class Tab:
    def __init__(self, parent, tab_data, name):
        """
        Class creates one group of statements

        returns tab which we can insert to main window
        """
        self.tab_name = name

        self.layout_widget = QtWidgets.QWidget()
        self.layout_widget.setGeometry(QtCore.QRect(0, 0, 891, 701))

        self.layout = QtWidgets.QHBoxLayout(self.layout_widget)

        self.left_layout = QtWidgets.QVBoxLayout()
        self.right_layout = QtWidgets.QVBoxLayout()

        self.cores = []

        for data in tab_data:
            new_label = QtWidgets.QLabel(str(data))
            self.left_layout.addWidget(new_label)
            c = Statements(self.layout_widget, tab_data[data], data)
            self.cores.append(c)
            # self.right_layout.addLayout(c.layout)
            self.right_layout.addWidget(c.out)

        self.layout.addLayout(self.left_layout)
        self.layout.addLayout(self.right_layout)

        self.scroll = QtWidgets.QScrollArea()
        self.scroll.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scroll.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scroll.setWidgetResizable(True)

        self.scroll.setWidget(self.layout_widget)

        self.out = self.scroll

    def getData(self):
        return (
            self.tab_name + ":\n" + "; ".join([core.getData() for core in self.cores])
        )


class Statements:
    def __init__(self, parent, statements, name):
        """
        Class creates a group of checkboxes in horizontal layout

        returns horizontal layout we can insert to main window
        """

        self.layout_widget = QtWidgets.QWidget()
        self.layout = QtWidgets.QVBoxLayout(self.layout_widget)
        self.name = name
        self.core = []
        self.text = []

        for statement in statements:
            if statement == "LINE":
                editable_text = QtWidgets.QTextEdit("")
                self.core.append(editable_text)
                self.text.append("")
                editable_text.setMinimumSize(QtCore.QSize(300, 100))
                self.layout.addWidget(editable_text)
            else:
                new_button = QtWidgets.QCheckBox(str(statement))
                self.core.append(new_button)
                self.text.append(str(statement))
                self.layout.addWidget(new_button)

        editable_text = QtWidgets.QTextEdit("")
        self.core.append(editable_text)
        self.text.append("")
        editable_text.setMinimumSize(QtCore.QSize(300, 100))
        self.layout.addWidget(editable_text)

        self.scroll = QtWidgets.QScrollArea()
        self.scroll.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scroll.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scroll.setWidgetResizable(True)

        self.scroll.setWidget(self.layout_widget)
        self.out = self.scroll

    def getData(self):
        # print(self.name)
        # input()
        answer = self.name + ": " if self.name != "" else ""
        for i in range(len(self.core)):
            a = ""
            # print(self.core[i])
            # input()
            try:
                if self.core[i].isChecked():
                    a = self.core[i].text()
            except:
                a = self.core[i].toPlainText()
            answer += a + ", " if a != "" else ""
        return answer.rstrip(", ")
