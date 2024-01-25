import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout,\
    QPushButton, QTextEdit, QMessageBox, QFileDialog

from OCR import give_orc


def ejra():
    # ایجاد یک برنامه
    app = QApplication(sys.argv)

    # ایجاد یک پنجره
    window = QWidget()
    window.setWindowTitle('کپی متن')

    # ایجاد یک لایه عمودی برای قرار دادن ورودی عکس و دکمه
    layout = QVBoxLayout()

    def selectimage():
        filename, _ = QFileDialog.getOpenFileName(
            window, 'انتخاب عکس', '', 'تصاویر (*.png *.jpg *.jpeg *.bmp)'
        )
        if filename:
            return give_orc(filename)

    select_button = QPushButton('انتخاب عکس', window)
    select_button.clicked.connect(selectimage)
    layout.addWidget(select_button)

    # ایجاد یک ورودی متن
    text_edit = QTextEdit(window)
    text_edit.setText(selectimage())
    layout.addWidget(text_edit)

    # ایجاد یک دکمه برای کپی کردن متن و عکس
    def copytext():
        text = text_edit.toPlainText()
        clipboard = QApplication.clipboard()
        clipboard.setText(text)

        QMessageBox.information(
            window, 'اعلام نتیجه', 'متن با موفقیت کپی شد!'
        )

    copy_button = QPushButton('کپی', window)

    copy_button.clicked.connect(copytext)
    layout.addWidget(copy_button)

    # قرار دادن لایه در پنجره
    window.setLayout(layout)

    # نمایش پنجره
    window.show()

    # اجرای برنامه
    sys.exit(app.exec_())


if __name__ == '__main__':
    ejra()
