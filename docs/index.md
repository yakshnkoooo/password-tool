## Документация password-tool
Это документация проекта password-tool.
Это утилита на Python для генерации паролей и оценки их надёжности.

## Установка (bash)
```
pip install -r requirements.txt
```

## Использование (python)
```
from password_tool import generate, strength, is_common

pwd = generate(16)
print(pwd)

print(strength("password"))  # Вернет 'weak', так как пароль популярный
print(is_common("123456"))   # Вернет True
```

## Тестирование
Проект использует GitHub Actions. При каждом пуше запускаются 15 тестов (unit и интеграционные).
