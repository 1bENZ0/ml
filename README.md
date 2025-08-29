Датасет [iris](https://www.kaggle.com/datasets/uciml/iris)

Описание использованных алгоритмов:

RandomForestClassifier - это ансамблевый алгоритм,используется для задач классификации
LabelEncoder - метод предобработки данных для преобразования категориальных текстовых меток в числовые значения


Инструкция по запуску:

1.) Склонировать проект и перейти в папку с проектом
2.) Скачать и установить [uv](https://docs.astral.sh/uv/)
3.) Установить зависимости:
```bash
uv init
uv sync
```
4.) Запустить mlflow server локально:
```bash
mlflow server --host 127.0.0.1 --port 5000
```

5.) Делать эксперементы и радоваться!

Результаты эксперементов:
<img width="1354" height="369" alt="image" src="https://github.com/user-attachments/assets/372a14e4-5bf0-4ea1-a78e-deb389a05c3c" />

Результаты лучшего эксперемента:
<img width="1199" height="787" alt="image" src="https://github.com/user-attachments/assets/5fac9e37-5fad-476c-8602-69681d4e1c19" />

Вывод:
Получили несколько моделей с различными метриками, научились работать с mlflow, airflow, dvc для реализации mlops пайплайна!
