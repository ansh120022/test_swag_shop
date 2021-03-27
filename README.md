
# Автотесты для интернет-магазина 

[![Build Status](https://ansh.beta.teamcity.com/app/rest/builds/buildType:(id:TestSwagShop_Build)/statusIcon)](https://ansh.beta.teamcity.com/viewType.html?buildTypeId=TestSwagShop_Build&guest=1)


В рамках этого проекта автоматизированы основные сценарии пользователей [магазина](http://automationpractice.com) : авторизация, работа с корзиной, оформление заказа и сопутствующие процессы.

# Запуск

Запустить Selenuim WebDriver для Chrome:

```bash
docker run -d --name selenium -p 4444:4444 selenium/standalone-chrome
```
Создать виртуальное окружение:

```bash
python -m venv env && source env/bin/activate
```

Установить зависимости:
```bash
cd test_swag_shop && pip install -r requirements.txt
```
Запустить тесты
```bash
pytest --testrail --tr-config=testrail.cfg --alluredir=reports
```
Построить отчёт по результататам:

```bash
allure serve reports
```
Allure уже должен быть установлен локально, для этого следуйте [инструкции](https://docs.qameta.io/allure/ "инструкции")

Если требуется запуск под конкретным пользователем, можно использовать параметры
 ```bash
--username=''   --password=''
```
