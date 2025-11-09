from flask import Flask

app = Flask(__name__)

def read_html_file():
    """Читает HTML файл и возвращает его содержимое"""
    try:
        with open('contacts.html', 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        return "<h1>Файл contacts.html не найден</h1>"

@app.route('/', methods=['GET'])
@app.route('/<path:any_path>', methods=['GET'])
def contacts_page(any_path=None):
    """
    Обрабатывает любой GET-запрос и возвращает страницу "Контакты"
    """
    html_content = read_html_file()
    return html_content, 200, {'Content-Type': 'text/html; charset=utf-8'}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)