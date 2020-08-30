from PyQt5 import QtGui, QtCore, QtWidgets
import sys, os
import source.tools.Constants as Constants

class Tab:
    def __init__(self, parent, tab_data):
        """
        Class creates one group of statements
        
        returns tab which we can insert to main window
        """
        # self.scroll.setWidget(self.layout_widget)

        self.layout_widget = QtWidgets.QWidget()
        self.layout_widget.setGeometry(QtCore.QRect(0, 0, 891, 701))
        
        self.layout = QtWidgets.QHBoxLayout(self.layout_widget)

        self.left_layout = QtWidgets.QVBoxLayout()
        self.right_layout = QtWidgets.QVBoxLayout()

        for data in tab_data:
            new_label = QtWidgets.QLabel(str(data))
            self.left_layout.addWidget(new_label)
            c = Statements(self.layout_widget, tab_data[data])
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

class Statements:
    def __init__(self, parent, statements):
        """ 
        Class creates a group of checkboxes in horizontal layout

        returns horizontal layout we can insert to main window
        """

        self.layout_widget = QtWidgets.QWidget()
        self.layout = QtWidgets.QVBoxLayout(self.layout_widget)

        for statement in statements:
            new_button = QtWidgets.QCheckBox(str(statement))
            new_button.adjustSize()
            self.layout.addWidget(new_button)

        editable_text = QtWidgets.QTextEdit("можно изменять")
        editable_text.setMinimumSize(QtCore.QSize(300, 100))
        self.layout.addWidget(editable_text)

        self.scroll = QtWidgets.QScrollArea()
        self.scroll.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scroll.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scroll.setWidgetResizable(True)

        self.scroll.setWidget(self.layout_widget)
        self.out = self.scroll
