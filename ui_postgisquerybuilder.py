# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Z:\dev\postgisQueryBuilder\ui_postgisquerybuilder.ui'
#
# Created: Tue Sep 15 10:45:00 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_postgisQueryBuilder(object):
    def setupUi(self, postgisQueryBuilder):
        postgisQueryBuilder.setObjectName(_fromUtf8("postgisQueryBuilder"))
        postgisQueryBuilder.setEnabled(True)
        postgisQueryBuilder.resize(486, 796)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(postgisQueryBuilder.sizePolicy().hasHeightForWidth())
        postgisQueryBuilder.setSizePolicy(sizePolicy)
        self.verticalLayout_18 = QtGui.QVBoxLayout(postgisQueryBuilder)
        self.verticalLayout_18.setObjectName(_fromUtf8("verticalLayout_18"))
        self.tabWidget = QtGui.QToolBox(postgisQueryBuilder)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setMinimumSize(QtCore.QSize(200, 0))
        self.tabWidget.setFrameShape(QtGui.QFrame.NoFrame)
        self.tabWidget.setFrameShadow(QtGui.QFrame.Plain)
        self.tabWidget.setLineWidth(1)
        self.tabWidget.setMidLineWidth(0)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.ConnectionSlot = QtGui.QWidget()
        self.ConnectionSlot.setGeometry(QtCore.QRect(0, 0, 468, 619))
        self.ConnectionSlot.setObjectName(_fromUtf8("ConnectionSlot"))
        self.verticalLayout_19 = QtGui.QVBoxLayout(self.ConnectionSlot)
        self.verticalLayout_19.setContentsMargins(0, 3, 0, 3)
        self.verticalLayout_19.setObjectName(_fromUtf8("verticalLayout_19"))
        self.verticalLayout_6 = QtGui.QVBoxLayout()
        self.verticalLayout_6.setSpacing(2)
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setSpacing(3)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.PSQLConnectionLabel = QtGui.QLabel(self.ConnectionSlot)
        self.PSQLConnectionLabel.setObjectName(_fromUtf8("PSQLConnectionLabel"))
        self.verticalLayout_2.addWidget(self.PSQLConnectionLabel)
        self.PSQLConnection = QtGui.QComboBox(self.ConnectionSlot)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PSQLConnection.sizePolicy().hasHeightForWidth())
        self.PSQLConnection.setSizePolicy(sizePolicy)
        self.PSQLConnection.setObjectName(_fromUtf8("PSQLConnection"))
        self.verticalLayout_2.addWidget(self.PSQLConnection)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setSpacing(3)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.horizontalLayout_15 = QtGui.QHBoxLayout()
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName(_fromUtf8("horizontalLayout_15"))
        self.DBSchemaLabel = QtGui.QLabel(self.ConnectionSlot)
        self.DBSchemaLabel.setObjectName(_fromUtf8("DBSchemaLabel"))
        self.horizontalLayout_15.addWidget(self.DBSchemaLabel)
        self.schemaAdd = QtGui.QToolButton(self.ConnectionSlot)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.schemaAdd.sizePolicy().hasHeightForWidth())
        self.schemaAdd.setSizePolicy(sizePolicy)
        self.schemaAdd.setMinimumSize(QtCore.QSize(17, 17))
        self.schemaAdd.setMaximumSize(QtCore.QSize(17, 17))
        self.schemaAdd.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(6)
        self.schemaAdd.setFont(font)
        self.schemaAdd.setText(_fromUtf8("+"))
        self.schemaAdd.setObjectName(_fromUtf8("schemaAdd"))
        self.horizontalLayout_15.addWidget(self.schemaAdd)
        self.verticalLayout_3.addLayout(self.horizontalLayout_15)
        self.DBSchema = QtGui.QComboBox(self.ConnectionSlot)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.DBSchema.sizePolicy().hasHeightForWidth())
        self.DBSchema.setSizePolicy(sizePolicy)
        self.DBSchema.setObjectName(_fromUtf8("DBSchema"))
        self.verticalLayout_3.addWidget(self.DBSchema)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.verticalLayout_6.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.verticalLayout_9 = QtGui.QVBoxLayout()
        self.verticalLayout_9.setSpacing(3)
        self.verticalLayout_9.setObjectName(_fromUtf8("verticalLayout_9"))
        self.USERFIELDLabel = QtGui.QLabel(self.ConnectionSlot)
        self.USERFIELDLabel.setObjectName(_fromUtf8("USERFIELDLabel"))
        self.verticalLayout_9.addWidget(self.USERFIELDLabel)
        self.USERFIELD = QtGui.QLineEdit(self.ConnectionSlot)
        self.USERFIELD.setObjectName(_fromUtf8("USERFIELD"))
        self.verticalLayout_9.addWidget(self.USERFIELD)
        self.horizontalLayout_7.addLayout(self.verticalLayout_9)
        self.verticalLayout_10 = QtGui.QVBoxLayout()
        self.verticalLayout_10.setSpacing(3)
        self.verticalLayout_10.setObjectName(_fromUtf8("verticalLayout_10"))
        self.PASSWORDFIELDLabel = QtGui.QLabel(self.ConnectionSlot)
        self.PASSWORDFIELDLabel.setObjectName(_fromUtf8("PASSWORDFIELDLabel"))
        self.verticalLayout_10.addWidget(self.PASSWORDFIELDLabel)
        self.PASSWORDFIELD = QtGui.QLineEdit(self.ConnectionSlot)
        self.PASSWORDFIELD.setEchoMode(QtGui.QLineEdit.Password)
        self.PASSWORDFIELD.setObjectName(_fromUtf8("PASSWORDFIELD"))
        self.verticalLayout_10.addWidget(self.PASSWORDFIELD)
        self.horizontalLayout_7.addLayout(self.verticalLayout_10)
        self.verticalLayout_6.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setSpacing(3)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.KEYFIELDLabel = QtGui.QLabel(self.ConnectionSlot)
        self.KEYFIELDLabel.setMaximumSize(QtCore.QSize(140, 16777215))
        self.KEYFIELDLabel.setObjectName(_fromUtf8("KEYFIELDLabel"))
        self.verticalLayout_4.addWidget(self.KEYFIELDLabel)
        self.KEYFIELD = QtGui.QComboBox(self.ConnectionSlot)
        self.KEYFIELD.setEditable(True)
        self.KEYFIELD.setObjectName(_fromUtf8("KEYFIELD"))
        self.verticalLayout_4.addWidget(self.KEYFIELD)
        self.horizontalLayout_6.addLayout(self.verticalLayout_4)
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setSpacing(3)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.GEOMETRYFIELDLabel = QtGui.QLabel(self.ConnectionSlot)
        self.GEOMETRYFIELDLabel.setMaximumSize(QtCore.QSize(125, 16777215))
        self.GEOMETRYFIELDLabel.setObjectName(_fromUtf8("GEOMETRYFIELDLabel"))
        self.verticalLayout_5.addWidget(self.GEOMETRYFIELDLabel)
        self.GEOMETRYFIELD = QtGui.QComboBox(self.ConnectionSlot)
        self.GEOMETRYFIELD.setEditable(True)
        self.GEOMETRYFIELD.setObjectName(_fromUtf8("GEOMETRYFIELD"))
        self.verticalLayout_5.addWidget(self.GEOMETRYFIELD)
        self.horizontalLayout_6.addLayout(self.verticalLayout_5)
        self.verticalLayout_6.addLayout(self.horizontalLayout_6)
        self.label_2 = QtGui.QLabel(self.ConnectionSlot)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QtCore.QSize(0, 0))
        self.label_2.setMaximumSize(QtCore.QSize(10000, 16777215))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout_6.addWidget(self.label_2)
        self.label = QtGui.QLabel(self.ConnectionSlot)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout_6.addWidget(self.label)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.LayerList = QtGui.QListWidget(self.ConnectionSlot)
        self.LayerList.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.LayerList.setObjectName(_fromUtf8("LayerList"))
        self.horizontalLayout.addWidget(self.LayerList)
        self.verticalLayout_6.addLayout(self.horizontalLayout)
        self.verticalLayout_19.addLayout(self.verticalLayout_6)
        self.tabWidget.addItem(self.ConnectionSlot, _fromUtf8(""))
        self.queryDefinitionSlot = QtGui.QWidget()
        self.queryDefinitionSlot.setGeometry(QtCore.QRect(0, 0, 468, 619))
        self.queryDefinitionSlot.setObjectName(_fromUtf8("queryDefinitionSlot"))
        self.verticalLayout_17 = QtGui.QVBoxLayout(self.queryDefinitionSlot)
        self.verticalLayout_17.setSizeConstraint(QtGui.QLayout.SetMaximumSize)
        self.verticalLayout_17.setContentsMargins(0, 3, 0, 3)
        self.verticalLayout_17.setObjectName(_fromUtf8("verticalLayout_17"))
        self.verticalLayout_7 = QtGui.QVBoxLayout()
        self.verticalLayout_7.setSpacing(2)
        self.verticalLayout_7.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.QueryType = QtGui.QComboBox(self.queryDefinitionSlot)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.QueryType.sizePolicy().hasHeightForWidth())
        self.QueryType.setSizePolicy(sizePolicy)
        self.QueryType.setMaxVisibleItems(20)
        self.QueryType.setObjectName(_fromUtf8("QueryType"))
        self.horizontalLayout_8.addWidget(self.QueryType)
        self.ButtonHelp = QtGui.QPushButton(self.queryDefinitionSlot)
        self.ButtonHelp.setMinimumSize(QtCore.QSize(100, 0))
        self.ButtonHelp.setMaximumSize(QtCore.QSize(100, 16777215))
        self.ButtonHelp.setObjectName(_fromUtf8("ButtonHelp"))
        self.horizontalLayout_8.addWidget(self.ButtonHelp)
        self.verticalLayout_7.addLayout(self.horizontalLayout_8)
        self.summaryBox = QtGui.QGroupBox(self.queryDefinitionSlot)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.summaryBox.sizePolicy().hasHeightForWidth())
        self.summaryBox.setSizePolicy(sizePolicy)
        self.summaryBox.setObjectName(_fromUtf8("summaryBox"))
        self.verticalLayout_11 = QtGui.QVBoxLayout(self.summaryBox)
        self.verticalLayout_11.setSpacing(3)
        self.verticalLayout_11.setSizeConstraint(QtGui.QLayout.SetMinimumSize)
        self.verticalLayout_11.setContentsMargins(3, 0, 3, 3)
        self.verticalLayout_11.setObjectName(_fromUtf8("verticalLayout_11"))
        self.Helper = QtGui.QLabel(self.summaryBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Helper.sizePolicy().hasHeightForWidth())
        self.Helper.setSizePolicy(sizePolicy)
        self.Helper.setMinimumSize(QtCore.QSize(0, 0))
        self.Helper.setAutoFillBackground(False)
        self.Helper.setFrameShape(QtGui.QFrame.NoFrame)
        self.Helper.setText(_fromUtf8(""))
        self.Helper.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.Helper.setWordWrap(True)
        self.Helper.setObjectName(_fromUtf8("Helper"))
        self.verticalLayout_11.addWidget(self.Helper)
        self.DiagPanel = QtGui.QGraphicsView(self.summaryBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.DiagPanel.sizePolicy().hasHeightForWidth())
        self.DiagPanel.setSizePolicy(sizePolicy)
        self.DiagPanel.setMinimumSize(QtCore.QSize(0, 0))
        self.DiagPanel.setMaximumSize(QtCore.QSize(16777215, 100))
        self.DiagPanel.setAcceptDrops(False)
        self.DiagPanel.setStyleSheet(_fromUtf8("color: rgba(212, 208, 200, 0)"))
        self.DiagPanel.setFrameShape(QtGui.QFrame.NoFrame)
        self.DiagPanel.setFrameShadow(QtGui.QFrame.Raised)
        self.DiagPanel.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.DiagPanel.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        brush = QtGui.QBrush(QtGui.QColor(212, 208, 200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        self.DiagPanel.setBackgroundBrush(brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 170))
        brush.setStyle(QtCore.Qt.NoBrush)
        self.DiagPanel.setForegroundBrush(brush)
        self.DiagPanel.setInteractive(False)
        self.DiagPanel.setObjectName(_fromUtf8("DiagPanel"))
        self.verticalLayout_11.addWidget(self.DiagPanel)
        self.verticalLayout_7.addWidget(self.summaryBox)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(2)
        self.horizontalLayout_3.setSizeConstraint(QtGui.QLayout.SetMinimumSize)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.LAYERaLabel = QtGui.QLabel(self.queryDefinitionSlot)
        self.LAYERaLabel.setObjectName(_fromUtf8("LAYERaLabel"))
        self.horizontalLayout_3.addWidget(self.LAYERaLabel)
        self.LAYERa = QtGui.QComboBox(self.queryDefinitionSlot)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LAYERa.sizePolicy().hasHeightForWidth())
        self.LAYERa.setSizePolicy(sizePolicy)
        self.LAYERa.setMinimumSize(QtCore.QSize(150, 0))
        self.LAYERa.setObjectName(_fromUtf8("LAYERa"))
        self.horizontalLayout_3.addWidget(self.LAYERa)
        self.LAYERaAllFields = QtGui.QCheckBox(self.queryDefinitionSlot)
        self.LAYERaAllFields.setObjectName(_fromUtf8("LAYERaAllFields"))
        self.horizontalLayout_3.addWidget(self.LAYERaAllFields)
        self.verticalLayout_7.addLayout(self.horizontalLayout_3)
        self.fieldsListA = QtGui.QListWidget(self.queryDefinitionSlot)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(50)
        sizePolicy.setHeightForWidth(self.fieldsListA.sizePolicy().hasHeightForWidth())
        self.fieldsListA.setSizePolicy(sizePolicy)
        self.fieldsListA.setMinimumSize(QtCore.QSize(0, 40))
        self.fieldsListA.setMaximumSize(QtCore.QSize(16777215, 2000))
        self.fieldsListA.setObjectName(_fromUtf8("fieldsListA"))
        self.verticalLayout_7.addWidget(self.fieldsListA)
        self.horizontalLayout_10 = QtGui.QHBoxLayout()
        self.horizontalLayout_10.setSpacing(2)
        self.horizontalLayout_10.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.horizontalLayout_10.setObjectName(_fromUtf8("horizontalLayout_10"))
        self.LAYERbLabel = QtGui.QLabel(self.queryDefinitionSlot)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LAYERbLabel.sizePolicy().hasHeightForWidth())
        self.LAYERbLabel.setSizePolicy(sizePolicy)
        self.LAYERbLabel.setMinimumSize(QtCore.QSize(0, 20))
        self.LAYERbLabel.setObjectName(_fromUtf8("LAYERbLabel"))
        self.horizontalLayout_10.addWidget(self.LAYERbLabel)
        self.LAYERb = QtGui.QComboBox(self.queryDefinitionSlot)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LAYERb.sizePolicy().hasHeightForWidth())
        self.LAYERb.setSizePolicy(sizePolicy)
        self.LAYERb.setMinimumSize(QtCore.QSize(150, 0))
        self.LAYERb.setObjectName(_fromUtf8("LAYERb"))
        self.horizontalLayout_10.addWidget(self.LAYERb)
        self.verticalLayout_7.addLayout(self.horizontalLayout_10)
        self.fieldsListB = QtGui.QListWidget(self.queryDefinitionSlot)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fieldsListB.sizePolicy().hasHeightForWidth())
        self.fieldsListB.setSizePolicy(sizePolicy)
        self.fieldsListB.setMinimumSize(QtCore.QSize(0, 40))
        self.fieldsListB.setMaximumSize(QtCore.QSize(16777215, 60))
        self.fieldsListB.setObjectName(_fromUtf8("fieldsListB"))
        self.verticalLayout_7.addWidget(self.fieldsListB)
        self.verticalLayout_12 = QtGui.QVBoxLayout()
        self.verticalLayout_12.setSpacing(2)
        self.verticalLayout_12.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.verticalLayout_12.setObjectName(_fromUtf8("verticalLayout_12"))
        self.horizontalLayout_11 = QtGui.QHBoxLayout()
        self.horizontalLayout_11.setSpacing(3)
        self.horizontalLayout_11.setSizeConstraint(QtGui.QLayout.SetFixedSize)
        self.horizontalLayout_11.setObjectName(_fromUtf8("horizontalLayout_11"))
        self.BUFFERRADIUSLabel = QtGui.QLabel(self.queryDefinitionSlot)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BUFFERRADIUSLabel.sizePolicy().hasHeightForWidth())
        self.BUFFERRADIUSLabel.setSizePolicy(sizePolicy)
        self.BUFFERRADIUSLabel.setObjectName(_fromUtf8("BUFFERRADIUSLabel"))
        self.horizontalLayout_11.addWidget(self.BUFFERRADIUSLabel)
        self.BUFFERRADIUS = QtGui.QLineEdit(self.queryDefinitionSlot)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BUFFERRADIUS.sizePolicy().hasHeightForWidth())
        self.BUFFERRADIUS.setSizePolicy(sizePolicy)
        self.BUFFERRADIUS.setObjectName(_fromUtf8("BUFFERRADIUS"))
        self.horizontalLayout_11.addWidget(self.BUFFERRADIUS)
        self.verticalLayout_12.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_12 = QtGui.QHBoxLayout()
        self.horizontalLayout_12.setSpacing(3)
        self.horizontalLayout_12.setSizeConstraint(QtGui.QLayout.SetFixedSize)
        self.horizontalLayout_12.setObjectName(_fromUtf8("horizontalLayout_12"))
        self.SPATIALRELLabel = QtGui.QLabel(self.queryDefinitionSlot)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SPATIALRELLabel.sizePolicy().hasHeightForWidth())
        self.SPATIALRELLabel.setSizePolicy(sizePolicy)
        self.SPATIALRELLabel.setObjectName(_fromUtf8("SPATIALRELLabel"))
        self.horizontalLayout_12.addWidget(self.SPATIALRELLabel)
        self.SPATIALREL = QtGui.QComboBox(self.queryDefinitionSlot)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SPATIALREL.sizePolicy().hasHeightForWidth())
        self.SPATIALREL.setSizePolicy(sizePolicy)
        self.SPATIALREL.setObjectName(_fromUtf8("SPATIALREL"))
        self.horizontalLayout_12.addWidget(self.SPATIALREL)
        self.SPATIALRELNOT = QtGui.QCheckBox(self.queryDefinitionSlot)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(20)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SPATIALRELNOT.sizePolicy().hasHeightForWidth())
        self.SPATIALRELNOT.setSizePolicy(sizePolicy)
        self.SPATIALRELNOT.setMaximumSize(QtCore.QSize(50, 16777215))
        self.SPATIALRELNOT.setObjectName(_fromUtf8("SPATIALRELNOT"))
        self.horizontalLayout_12.addWidget(self.SPATIALRELNOT)
        self.verticalLayout_12.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_13 = QtGui.QHBoxLayout()
        self.horizontalLayout_13.setSpacing(3)
        self.horizontalLayout_13.setSizeConstraint(QtGui.QLayout.SetFixedSize)
        self.horizontalLayout_13.setObjectName(_fromUtf8("horizontalLayout_13"))
        self.FIELDLabel = QtGui.QLabel(self.queryDefinitionSlot)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.FIELDLabel.sizePolicy().hasHeightForWidth())
        self.FIELDLabel.setSizePolicy(sizePolicy)
        self.FIELDLabel.setMinimumSize(QtCore.QSize(65, 0))
        self.FIELDLabel.setObjectName(_fromUtf8("FIELDLabel"))
        self.horizontalLayout_13.addWidget(self.FIELDLabel)
        self.FIELD = QtGui.QComboBox(self.queryDefinitionSlot)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.FIELD.sizePolicy().hasHeightForWidth())
        self.FIELD.setSizePolicy(sizePolicy)
        self.FIELD.setObjectName(_fromUtf8("FIELD"))
        self.horizontalLayout_13.addWidget(self.FIELD)
        self.verticalLayout_12.addLayout(self.horizontalLayout_13)
        self.horizontalLayout_17 = QtGui.QHBoxLayout()
        self.horizontalLayout_17.setSpacing(3)
        self.horizontalLayout_17.setSizeConstraint(QtGui.QLayout.SetFixedSize)
        self.horizontalLayout_17.setObjectName(_fromUtf8("horizontalLayout_17"))
        self.JOINLabel = QtGui.QLabel(self.queryDefinitionSlot)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.JOINLabel.sizePolicy().hasHeightForWidth())
        self.JOINLabel.setSizePolicy(sizePolicy)
        self.JOINLabel.setMinimumSize(QtCore.QSize(65, 0))
        self.JOINLabel.setObjectName(_fromUtf8("JOINLabel"))
        self.horizontalLayout_17.addWidget(self.JOINLabel)
        self.JOIN = QtGui.QComboBox(self.queryDefinitionSlot)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.JOIN.sizePolicy().hasHeightForWidth())
        self.JOIN.setSizePolicy(sizePolicy)
        self.JOIN.setObjectName(_fromUtf8("JOIN"))
        self.horizontalLayout_17.addWidget(self.JOIN)
        self.verticalLayout_12.addLayout(self.horizontalLayout_17)
        self.horizontalLayout_19 = QtGui.QHBoxLayout()
        self.horizontalLayout_19.setSpacing(3)
        self.horizontalLayout_19.setSizeConstraint(QtGui.QLayout.SetFixedSize)
        self.horizontalLayout_19.setObjectName(_fromUtf8("horizontalLayout_19"))
        self.FIELDbLabel = QtGui.QLabel(self.queryDefinitionSlot)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.FIELDbLabel.sizePolicy().hasHeightForWidth())
        self.FIELDbLabel.setSizePolicy(sizePolicy)
        self.FIELDbLabel.setMinimumSize(QtCore.QSize(65, 0))
        self.FIELDbLabel.setObjectName(_fromUtf8("FIELDbLabel"))
        self.horizontalLayout_19.addWidget(self.FIELDbLabel)
        self.FIELDb = QtGui.QComboBox(self.queryDefinitionSlot)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.FIELDb.sizePolicy().hasHeightForWidth())
        self.FIELDb.setSizePolicy(sizePolicy)
        self.FIELDb.setObjectName(_fromUtf8("FIELDb"))
        self.horizontalLayout_19.addWidget(self.FIELDb)
        self.verticalLayout_12.addLayout(self.horizontalLayout_19)
        self.verticalLayout_7.addLayout(self.verticalLayout_12)
        spacerItem = QtGui.QSpacerItem(20, 0, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem)
        self.verticalLayout_17.addLayout(self.verticalLayout_7)
        self.tabWidget.addItem(self.queryDefinitionSlot, _fromUtf8(""))
        self.filterRecordSlot = QtGui.QWidget()
        self.filterRecordSlot.setGeometry(QtCore.QRect(0, 0, 468, 619))
        self.filterRecordSlot.setObjectName(_fromUtf8("filterRecordSlot"))
        self.verticalLayout_16 = QtGui.QVBoxLayout(self.filterRecordSlot)
        self.verticalLayout_16.setContentsMargins(0, 3, 0, 3)
        self.verticalLayout_16.setObjectName(_fromUtf8("verticalLayout_16"))
        self.filterTable = tableSet(self.filterRecordSlot)
        self.filterTable.setShowGrid(False)
        self.filterTable.setObjectName(_fromUtf8("filterTable"))
        self.filterTable.setColumnCount(0)
        self.filterTable.setRowCount(0)
        self.filterTable.horizontalHeader().setVisible(False)
        self.filterTable.verticalHeader().setVisible(False)
        self.verticalLayout_16.addWidget(self.filterTable)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.labelOrderby = QtGui.QLabel(self.filterRecordSlot)
        self.labelOrderby.setObjectName(_fromUtf8("labelOrderby"))
        self.horizontalLayout_4.addWidget(self.labelOrderby)
        self.orderBy = QtGui.QComboBox(self.filterRecordSlot)
        self.orderBy.setMinimumSize(QtCore.QSize(100, 0))
        self.orderBy.setObjectName(_fromUtf8("orderBy"))
        self.horizontalLayout_4.addWidget(self.orderBy)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.verticalLayout_16.addLayout(self.horizontalLayout_4)
        self.tabWidget.addItem(self.filterRecordSlot, _fromUtf8(""))
        self.SqlCodeSlot = QtGui.QWidget()
        self.SqlCodeSlot.setGeometry(QtCore.QRect(0, 0, 468, 619))
        self.SqlCodeSlot.setObjectName(_fromUtf8("SqlCodeSlot"))
        self.verticalLayout_15 = QtGui.QVBoxLayout(self.SqlCodeSlot)
        self.verticalLayout_15.setContentsMargins(0, 3, 0, 3)
        self.verticalLayout_15.setObjectName(_fromUtf8("verticalLayout_15"))
        self.verticalLayout_8 = QtGui.QVBoxLayout()
        self.verticalLayout_8.setObjectName(_fromUtf8("verticalLayout_8"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setSpacing(3)
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.checkCreateView = QtGui.QCheckBox(self.SqlCodeSlot)
        self.checkCreateView.setObjectName(_fromUtf8("checkCreateView"))
        self.horizontalLayout_5.addWidget(self.checkCreateView)
        self.checkMaterialized = QtGui.QCheckBox(self.SqlCodeSlot)
        self.checkMaterialized.setObjectName(_fromUtf8("checkMaterialized"))
        self.horizontalLayout_5.addWidget(self.checkMaterialized)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem2)
        self.checkAutoCompiled = QtGui.QCheckBox(self.SqlCodeSlot)
        self.checkAutoCompiled.setObjectName(_fromUtf8("checkAutoCompiled"))
        self.horizontalLayout_5.addWidget(self.checkAutoCompiled)
        self.verticalLayout_8.addLayout(self.horizontalLayout_5)
        self.QueryName = QtGui.QLineEdit(self.SqlCodeSlot)
        self.QueryName.setMaximumSize(QtCore.QSize(16777215, 20))
        self.QueryName.setObjectName(_fromUtf8("QueryName"))
        self.verticalLayout_8.addWidget(self.QueryName)
        self.QueryResult = QtGui.QTextEdit(self.SqlCodeSlot)
        self.QueryResult.setObjectName(_fromUtf8("QueryResult"))
        self.verticalLayout_8.addWidget(self.QueryResult)
        self.verticalLayout_15.addLayout(self.verticalLayout_8)
        self.tabWidget.addItem(self.SqlCodeSlot, _fromUtf8(""))
        self.tableResultSlot = QtGui.QWidget()
        self.tableResultSlot.setGeometry(QtCore.QRect(0, 0, 468, 619))
        self.tableResultSlot.setObjectName(_fromUtf8("tableResultSlot"))
        self.verticalLayout_14 = QtGui.QVBoxLayout(self.tableResultSlot)
        self.verticalLayout_14.setContentsMargins(0, 3, 0, 3)
        self.verticalLayout_14.setObjectName(_fromUtf8("verticalLayout_14"))
        self.verticalLayout_13 = QtGui.QVBoxLayout()
        self.verticalLayout_13.setSpacing(2)
        self.verticalLayout_13.setObjectName(_fromUtf8("verticalLayout_13"))
        self.labelRowsNumber = QtGui.QLabel(self.tableResultSlot)
        self.labelRowsNumber.setText(_fromUtf8(""))
        self.labelRowsNumber.setObjectName(_fromUtf8("labelRowsNumber"))
        self.verticalLayout_13.addWidget(self.labelRowsNumber)
        self.TableResult = QtGui.QTableWidget(self.tableResultSlot)
        self.TableResult.setObjectName(_fromUtf8("TableResult"))
        self.TableResult.setColumnCount(0)
        self.TableResult.setRowCount(0)
        self.TableResult.horizontalHeader().setMinimumSectionSize(25)
        self.TableResult.verticalHeader().setDefaultSectionSize(25)
        self.verticalLayout_13.addWidget(self.TableResult)
        self.verticalLayout_14.addLayout(self.verticalLayout_13)
        self.tabWidget.addItem(self.tableResultSlot, _fromUtf8(""))
        self.historySlot = QtGui.QWidget()
        self.historySlot.setGeometry(QtCore.QRect(0, 0, 468, 619))
        self.historySlot.setObjectName(_fromUtf8("historySlot"))
        self.verticalLayout_21 = QtGui.QVBoxLayout(self.historySlot)
        self.verticalLayout_21.setContentsMargins(0, 3, 0, 3)
        self.verticalLayout_21.setObjectName(_fromUtf8("verticalLayout_21"))
        self.historyLog = QtGui.QPlainTextEdit(self.historySlot)
        self.historyLog.setReadOnly(True)
        self.historyLog.setObjectName(_fromUtf8("historyLog"))
        self.verticalLayout_21.addWidget(self.historyLog)
        self.tabWidget.addItem(self.historySlot, _fromUtf8(""))
        self.verticalLayout_18.addWidget(self.tabWidget)
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        self.ButtonRun = QtGui.QPushButton(postgisQueryBuilder)
        self.ButtonRun.setMaximumSize(QtCore.QSize(100, 16777215))
        self.ButtonRun.setObjectName(_fromUtf8("ButtonRun"))
        self.horizontalLayout_9.addWidget(self.ButtonRun)
        self.AddToMap = QtGui.QCheckBox(postgisQueryBuilder)
        self.AddToMap.setChecked(True)
        self.AddToMap.setObjectName(_fromUtf8("AddToMap"))
        self.horizontalLayout_9.addWidget(self.AddToMap)
        spacerItem3 = QtGui.QSpacerItem(100, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem3)
        self.ButtonReset = QtGui.QPushButton(postgisQueryBuilder)
        self.ButtonReset.setMaximumSize(QtCore.QSize(100, 16777215))
        self.ButtonReset.setObjectName(_fromUtf8("ButtonReset"))
        self.horizontalLayout_9.addWidget(self.ButtonReset)
        self.HelpLink = QtGui.QPushButton(postgisQueryBuilder)
        self.HelpLink.setMaximumSize(QtCore.QSize(100, 16777215))
        self.HelpLink.setObjectName(_fromUtf8("HelpLink"))
        self.horizontalLayout_9.addWidget(self.HelpLink)
        self.verticalLayout_18.addLayout(self.horizontalLayout_9)

        self.retranslateUi(postgisQueryBuilder)
        self.tabWidget.setCurrentIndex(3)
        self.tabWidget.layout().setSpacing(0)
        QtCore.QMetaObject.connectSlotsByName(postgisQueryBuilder)

    def retranslateUi(self, postgisQueryBuilder):
        postgisQueryBuilder.setWindowTitle(_translate("postgisQueryBuilder", "postgisQueryBuilder", None))
        self.PSQLConnectionLabel.setText(_translate("postgisQueryBuilder", "Postgresql connection", None))
        self.PSQLConnection.setToolTip(_translate("postgisQueryBuilder", "select working postgres connection", None))
        self.DBSchemaLabel.setText(_translate("postgisQueryBuilder", "Schema", None))
        self.schemaAdd.setToolTip(_translate("postgisQueryBuilder", "add new schema", None))
        self.DBSchema.setToolTip(_translate("postgisQueryBuilder", "select working schema", None))
        self.USERFIELDLabel.setText(_translate("postgisQueryBuilder", "User:", None))
        self.PASSWORDFIELDLabel.setText(_translate("postgisQueryBuilder", "Password:", None))
        self.KEYFIELDLabel.setText(_translate("postgisQueryBuilder", "default primary key field:", None))
        self.GEOMETRYFIELDLabel.setText(_translate("postgisQueryBuilder", "default geometry field:", None))
        self.label_2.setText(_translate("postgisQueryBuilder", "Available DB objects list (T:table V:view M:materialized view)", None))
        self.label.setText(_translate("postgisQueryBuilder", "right click for contextual menu - double click for query", None))
        self.tabWidget.setItemText(self.tabWidget.indexOf(self.ConnectionSlot), _translate("postgisQueryBuilder", "CONNECTION", None))
        self.ButtonHelp.setText(_translate("postgisQueryBuilder", "Help ", None))
        self.summaryBox.setTitle(_translate("postgisQueryBuilder", "Summary", None))
        self.LAYERaLabel.setText(_translate("postgisQueryBuilder", "Layer A", None))
        self.LAYERaAllFields.setText(_translate("postgisQueryBuilder", "Select all fields", None))
        self.LAYERbLabel.setText(_translate("postgisQueryBuilder", "Layer B", None))
        self.BUFFERRADIUSLabel.setText(_translate("postgisQueryBuilder", "Buffer radius", None))
        self.SPATIALRELLabel.setText(_translate("postgisQueryBuilder", "Relationship between A and B", None))
        self.SPATIALRELNOT.setText(_translate("postgisQueryBuilder", "NOT", None))
        self.FIELDLabel.setText(_translate("postgisQueryBuilder", "Join field of A", None))
        self.JOINLabel.setText(_translate("postgisQueryBuilder", "Join type", None))
        self.FIELDbLabel.setText(_translate("postgisQueryBuilder", "Join field of B", None))
        self.tabWidget.setItemText(self.tabWidget.indexOf(self.queryDefinitionSlot), _translate("postgisQueryBuilder", "QUERY", None))
        self.labelOrderby.setText(_translate("postgisQueryBuilder", "Order by:", None))
        self.tabWidget.setItemText(self.tabWidget.indexOf(self.filterRecordSlot), _translate("postgisQueryBuilder", "FILTER", None))
        self.checkCreateView.setText(_translate("postgisQueryBuilder", "As view", None))
        self.checkMaterialized.setText(_translate("postgisQueryBuilder", "Materialized", None))
        self.checkAutoCompiled.setText(_translate("postgisQueryBuilder", "Autocompiled", None))
        self.tabWidget.setItemText(self.tabWidget.indexOf(self.SqlCodeSlot), _translate("postgisQueryBuilder", "SQL", None))
        self.TableResult.setSortingEnabled(True)
        self.tabWidget.setItemText(self.tabWidget.indexOf(self.tableResultSlot), _translate("postgisQueryBuilder", "TABLE", None))
        self.tabWidget.setItemText(self.tabWidget.indexOf(self.historySlot), _translate("postgisQueryBuilder", "HISTORY", None))
        self.ButtonRun.setText(_translate("postgisQueryBuilder", "Run query", None))
        self.AddToMap.setText(_translate("postgisQueryBuilder", "Add to map", None))
        self.ButtonReset.setText(_translate("postgisQueryBuilder", "reset form", None))
        self.HelpLink.setText(_translate("postgisQueryBuilder", "Help", None))

from TableSet import tableSet
