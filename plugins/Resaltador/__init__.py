
from PySide import QtCore, QtGui

class Highlighter(QtGui.QSyntaxHighlighter):
    def __init__(self, parent=None):
        super(Highlighter, self).__init__(parent)

        keywordFormat = QtGui.QTextCharFormat()
        keywordFormat.setForeground(QtCore.Qt.darkBlue)
        keywordFormat.setFontWeight(QtGui.QFont.Bold)

        keywordPatterns = [r'\bclass\b',r'\bdef\b',r'\bimport\b',r'\bprint\b',r'\bin\b',r'\bfor\b',
                           r'\bwhile\b',r'\bif\b',r'\belif\b',r'\belse\b' ]

        self.highlightingRules = [(QtCore.QRegExp(pattern), keywordFormat)
                for pattern in keywordPatterns]

        classFormat = QtGui.QTextCharFormat()
        classFormat.setFontWeight(QtGui.QFont.Bold)
        classFormat.setForeground(QtCore.Qt.darkMagenta)
        self.highlightingRules.append((QtCore.QRegExp(r"\bQ[A-Za-z][A-Za-z0-9_]*\b"),
                classFormat))

        singleLineCommentFormat = QtGui.QTextCharFormat()
        singleLineCommentFormat.setForeground(QtCore.Qt.red)
        self.highlightingRules.append((QtCore.QRegExp(r"\#[^\n]*"),
                singleLineCommentFormat))

        self.multiLineCommentFormat = QtGui.QTextCharFormat()
        self.multiLineCommentFormat.setForeground(QtCore.Qt.red)

        quotationFormat = QtGui.QTextCharFormat()
        quotationFormat.setForeground(QtCore.Qt.darkGreen)
        self.highlightingRules.append((QtCore.QRegExp("\".*\""),
                quotationFormat))

        functionFormat = QtGui.QTextCharFormat()
        functionFormat.setFontItalic(True)
        functionFormat.setForeground(QtCore.Qt.blue)
        self.highlightingRules.append((QtCore.QRegExp("\\b[A-Za-z0-9_]+(?=\\()"),
                functionFormat))

        self.commentStartExpression = QtCore.QRegExp("/\\*")
        self.commentEndExpression = QtCore.QRegExp("\\*/")

    def highlightBlock(self, text):
        for pattern, format in self.highlightingRules:
            expression = QtCore.QRegExp(pattern)
            index = expression.indexIn(text)
            while index >= 0:
                length = expression.matchedLength()
                self.setFormat(index, length, format)
                index = expression.indexIn(text, index + length)

        self.setCurrentBlockState(0)

        startIndex = 0
        if self.previousBlockState() != 1:
            startIndex = self.commentStartExpression.indexIn(text)

        while startIndex >= 0:
            endIndex = self.commentEndExpression.indexIn(text, startIndex)

            if endIndex == -1:
                self.setCurrentBlockState(1)
                commentLength = len(text) - startIndex
            else:
                commentLength = endIndex - startIndex + self.commentEndExpression.matchedLength()

            self.setFormat(startIndex, commentLength,
                    self.multiLineCommentFormat)
            startIndex = self.commentStartExpression.indexIn(text,
                    startIndex + commentLength);

        
class HighlighterWrapper(QtCore.QObject):
    
    def getHighlighter(self, doc):
        return Highlighter(doc)
        

def init(core):
    return HighlighterWrapper()
    

def alFinalizar(core, instancia):
    pass


contrato = {
    'nombre':'resaltador',
    'dependencias':['guiStarter','Ventana'],
    'librerias':['PySide'],
    'inicio':init,
    'al_finalizar_carga':alFinalizar,
    'prioridad':1.1,
}





