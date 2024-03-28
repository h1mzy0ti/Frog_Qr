
# Frog QR

Frog qr is a web-based tool designed to create QR codes dynamically based on user input, typically a URL or text provided by the user. This application is developed using Flask, a micro web framework written in Python, making it lightweight, easy to deploy, and suitable for a wide range of web applications. The tool's primary functionality allows users to generate a QR code that can be downloaded and used in various contexts, such as business cards, websites, advertisements, and informational resources.


## Features
User Input: Upon visiting the application, users are presented with a form where they can input the text or URL they wish to encode in a QR code.

QR Code Generation: After submitting the form, the backend Flask application processes the input using the pyqrcode library to generate a QR code.

Display and Download: The generated QR code is then displayed on the webpage, and users are given the option to download it as a PNG file for their use.
## Acknowledgements

 - [Flask](https://pypi.org/project/PyQRCode/)
 - [pyqrcode](https://flask.palletsprojects.com/en/3.0.x/)


