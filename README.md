
# # Sprint_n - Тестирование UI для Яндекс.Маршруты

Автотесты для UI https://qa-routes.education-services.ru/

## Описание проекта

Проект содержит тесты веб приложения Яндекс.Маршруты:

- Отрисовка маршрута
- Отрисовка блока с выбором маршрута
- Подготовка к заказу такси
- «Заказ тарифа Такси» + полный флоу

## Технологии

- **Python** 3.14.2
- **Pytest** 9.0.2
- **Allure** 2.38.1
- **Page Object Pattern**
- **Selenium** 4.41.0

#### Запуск всех тестов
pytest tests/ -v

#### Запуск конкретного теста
- pytest tests/test_create_order_taxi.py -v
- pytest tests/test_prepare_order_taxi.py -v
- pytest tests/test_route_check.py -v
- pytest tests/test_select_type.py -v

#### Открытие отчёта
allure open target/allure-report
