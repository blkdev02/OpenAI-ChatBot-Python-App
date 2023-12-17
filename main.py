from PyQt6.QtWidgets import QApplication, QMainWindow, QTextEdit, QLineEdit, QPushButton
import sys

from backend import ChatBot
import threading


class ChatBoxWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setMinimumSize(700, 600)
        self.chatbot = ChatBot()

        # Add chat area widget
        self.chat_area = QTextEdit(self)
        self.chat_area.setGeometry(10, 10, 500, 400)
        self.chat_area.setReadOnly(True)

        # Add the input field widget
        self.input_field = QLineEdit(self)
        self.input_field.setGeometry(10, 450, 500, 50)
        self.input_field.returnPressed.connect(self.send_message)

        
        # Add the button
        self.button = QPushButton("Send", self)
        self.button.setGeometry(550, 450, 90, 50)
        self.button.clicked.connect(self.send_message)

        self.show()
    

    def send_message(self):
        user_input = self.input_field.text().strip()
        self.chat_area.append(f"<p style='color:#333333'>Me: {user_input}</p>")
        self.input_field.clear()

        # Created a thread
        thread = threading.Thread(target=self.get_bot_response, args=(user_input,))
        thread.start()

    def get_bot_response(self, user_input):
        # Create a ChatBot instance
        chatbot_response = self.chatbot.get_response(user_input)
        self.chat_area.append(f"<p style='color:#333333; background-color: #E9E9E9'>Bot: {chatbot_response}</p>")






app = QApplication(sys.argv)
main_window = ChatBoxWindow()
sys.exit(app.exec())
