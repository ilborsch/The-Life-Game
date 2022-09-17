Stepik "Web-фреймворк Flask: введение" course project.
Link - https://stepik.org/lesson/535659/step/6?unit=528765

The "Conway's Game of Life".
Inspired by - https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life

Запуск проекта
Устанавливаем зависимости из requirements.txt:
$ pip install -r requirements.txt Для Unix-систем вместо pip потребуется pip3.
вводим команду:
$ flask run

альтернативный вариант для Unix-систем - установите gunicorn pip3 install gunicorn и введите команду
$ gunicorn --bind 127.0.0.1:5000 app:app

в данном случае приложение будет доступно в локальной сети. Альтернативный вариант для Windows - установите waitress
$ pip install waitress
и введите команду
$ waitress-serve --listen=127.0.0.1:5000 app:app

Приятного обзора!