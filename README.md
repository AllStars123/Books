<h1>Test</h1>

Тестовое задание. 
<br>Микросервис.

<h2>Микросервис</h2>

CRUD был сделан на основе книжного магазина.

<ul>
<li>'books/' - Получение всех книг(GET)</li>
<li>'addbooks/' - Добавление книг в базу данных(POST)</li>
<li>'updatebook/<int:book_id>' - Обновление книги в базе данных(PUT)</li>
<li>'deletebook/<int:book_id>' - Удаление книги(DELETE)</li>
</ul>


<h2>Tests</h2>
В приложении написано 5 тестов.

`python3 manage.py test`

Команды для запуска
<br>`python3 manage.py makemigrations`
<br>`python3 manage.py migrate`
<br>`python3 manage.py runserver`

<h2>Как использовать</h2>
"http://127.0.0.1:9000/books/?title=Finansist" - поиск по названию
"http://127.0.0.1:9000/book/1" - получение деталей
<h2>Автор</h2>

<li>Пурнов Никита Олегович</li>

