# Feeder Weight Prediction

## Описание
Проект предназначен для прогнозирования производительности питателей с использованием модели линейной регрессии.

## Данные
Используется датасет:
- feders_weight_with_moving_averages.xlsx

## Модель
- Linear Regression
- Обучена на признаках:
  - Feeder1_Percent
  - Feeder2_Percent
  - Feeder3_Percent

## Результаты
- prediction_results.xlsx содержит предсказания модели

## Запуск

### Установка зависимостей
pip install -m pip install -r requirements.txt

### Обучение
python src/train.py

### Предсказание
python src/predict.py

### Запуск приложения
python -m streamlit run app/app.py
