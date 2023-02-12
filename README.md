
Данный репозиторий содержит файлы с автоматизированными тестами, составленными на основе паттерна `Page Object`.

<br>

Набор тестов проверяет страницы регистрации, авторизации и восстановления пароля Личного кабинета сайта "Ростелеком ID" `https://b2c.passport.rt.ru`.

<br>

Тестирование проводилось в браузере `MS Edge v.108` на базе `Win10` с использованием `Pytest` и `Selenium`.
<br>
<br>

<div id="content" align="center">
<h3>Содержание файлов:</h3>
</div>
       
- [conftest.py](SF_Final_Project_28/conftest.py) - фикстура для открытия браузера и запуска веб-драйвера

- [config.py](SF_Final_Project_28/config.py) - переменные, содержащие данные для тестов и параметризации

- [base.py](SF_Final_Project_28/base.py) - базовый клаас с функциямии и используемыми методами

- [rt_passport_reg.py](SF_Final_Project_28/rt_passport_reg.py), [rt_passport_auth.py](SF_Final_Project_28/rt_passport_auth.py), [rt_passport_pass_rec.py](SF_Final_Project_28/rt_passport_pass_rec.py) - локаторы и порядок действий, оформленный в функции, соответственно для страниц регистрации, авторизации и восстановления пароля

- [test_rt_reg.py](SF_Final_Project_28/test_rt_reg.py), [test_rt_auth.py](SF_Final_Project_28/test_rt_auth.py), [test_rt_pass_rec.py](SF_Final_Project_28/test_rt_pass_rec.py) - тесты, представленные в виде последовательных команд и проверки ожиданий, соответственно для страниц регистрации, авторизации и восстановления пароля

- [requirements.txt](SF_Final_Project_28/requirements.txt) - список используемых библиотек Python

- [edgedriver.exe](SF_Final_Project_28/edgedriver.exe) - Selenium WebDriver для браузера MS Edge v.108

- [Test cases._Bug reports.xlsx](SF_Final_Project_28/Test cases._Bug reports.xlsx) - набор тестовых сценариев и проверок, а также отчеты по обнаруженным дефектам и недочетам

- [Requirements_testing.docx](SF_Final_Project_28/Requirements_testing.docx) - сравнение и сопоставление ожидаемых условий с реальным фактическим результатом, а также качества функционала

- папка `screenshots` - директория для сохранения скриншотов по итогам каждого теста (указана в пути при создании файлов)
<br>
  
<br>
<div id="starttest" align="center">
<h3>Для запуска и проверки тестов необходимо:</h3>
</div>

1. Скачать репозиторий к себе на компьютер.

2. В IDE (по умолчанию PyCharm) создать проект и поместить в него все извлеченные файлы и папки.

3. Установить все используемые библиотеки Python, введя команду:
```
pip install -r requirements.txt
```

4. Запуск тестов осуществляется в PyCharm по отдельности через кнопки запуска тестов либо всем файлом при вводе в терминале нижеперечисленных соответствующих команд:
       
```
python -m pytest -v --driver Edge --driver-path edgedriver.exe test_rt_reg.py
```
```
python -m pytest -v --driver Edge --driver-path edgedriver.exe test_rt_auth.py
```
```
python -m pytest -v --driver Edge --driver-path edgedriver.exe test_rt_pass_rec.py
```
