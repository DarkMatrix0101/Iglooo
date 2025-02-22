import os
import random
from PyQt5 import QtWidgets, QtCore

def corrupt_file(file_path):
    
    with open(file_path, 'rb+') as file:
        file_size = os.path.getsize(file_path)
        num_corruptions = random.randint(1, int(file_size / 10))
        
        for _ in range(num_corruptions):
            corrupt_pos = random.randint(0, file_size - 1)
            file.seek(corrupt_pos)
            byte = file.read(1)
            new_byte = bytes([random.randint(0, 255)])
            file.seek(corrupt_pos)
            file.write(new_byte)

def select_file():
    global file_path
    file_path, _ = QtWidgets.QFileDialog.getOpenFileName()
    if file_path:
        corrupt_button.setEnabled(True)
        status_label.setText("Ready to corrupt.")

def exit_program():
    app.quit()


app = QtWidgets.QApplication([])


window = QtWidgets.QWidget()
window.setWindowTitle("IglooCorruptor")
window.setFixedSize(400, 200)  

select_button = QtWidgets.QPushButton("Select File", window)
select_button.clicked.connect(select_file)

corrupt_button = QtWidgets.QPushButton("Corrupt", window)
corrupt_button.clicked.connect(lambda: corrupt_file(file_path))
corrupt_button.setEnabled(False)  


exit_button = QtWidgets.QPushButton("Exit", window)
exit_button.clicked.connect(exit_program)


status_label = QtWidgets.QLabel("", window)


layout = QtWidgets.QVBoxLayout(window)
layout.addWidget(select_button)
layout.addWidget(corrupt_button)
layout.addWidget(exit_button)
layout.addWidget(status_label)


window.setLayout(layout)


window.show()


app.exec_()