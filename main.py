from flask import Flask

app = Flask(__name__) # En app se encuentra nuestro servidor web de Flask

if __name__ == '__main__':

    app.run(debug=True) # El debug=True hace que cada vez que reiniciemos el servidor o modifiquemos codigo, el servidor de Flask se reinicie solo