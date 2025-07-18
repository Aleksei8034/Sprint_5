# Финальный проект 5 спринта  "UI-тестирование"

Автотесты для сервиса Stellar Burgers.

Файлы:
test/ - каталог с автотестами
test/test_constructor.py - файл с проверками раздела конструктор
test/test_login.py - файл с проверками авторизации
test/test_profile_page.py - файл с проверками личного кабинета
test/test_registration_page.py - файл с проверками регистрации
conftest.py - файл с фикстурами
data.py - данные для авторизации / регистрации
locators.py - файл с локаторами элементов в DOM
urls.py - файл с константами URL

Команда для запуска тестов:
pytest -v
