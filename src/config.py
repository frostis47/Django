# Импорт встроенной библиотеки для работы веб-сервера
from http.server import BaseHTTPRequestHandler, HTTPServer

# Для начала определим настройки запуска
hostName = "localhost"  # Адрес для доступа по сети
serverPort = 8080  # Порт для доступа по сети


class MyServer(BaseHTTPRequestHandler):
    """
        Специальный класс, который отвечает за
        обработку входящих запросов от клиентов
    """

    def do_GET(self):
        """ Метод для обработки входящих GET-запросов """

        path = self.path

        # Validate request path, and set type
        if path == "/css/bootstrap.min.css":
            path = "../css/bootstrap.min.css"
            type_header = "text/css"
        elif path == "/js/bootstrap.bundle.min.js":
            path = "../js/bootstrap.bundle.min.js"
            type_header = "text/javascript"

        else:
            # Wild-card/default
            self.path.replace("/", "")
            path = f"../html/contacts.html"
            type_header = "text/html"

        self.send_response(200)  # Отправка кода ответа
        self.send_header("Content-type", type_header)  # Отправка типа данных, который будет передаваться
        self.end_headers()  # Завершение формирования заголовков ответа
        with open(path, encoding="utf-8") as file:
            content = file.read()
            self.wfile.write(bytes(content, "utf-8"))  # Тело ответа

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)

        response = f"Received POST data: {post_data.decode('utf-8')}"
        print(response)


if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        # Cтарт веб-сервера
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass
    webServer.server_close()
    print("Server stopped.")
