# management/commands/import_pets.py
import pandas as pd
from django.core.management.base import BaseCommand
from parseExcel.models import Pet  

class Command(BaseCommand):
    help = 'Import pets from an Excel file'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help='The path to the Excel file')

    def handle(self, *args, **kwargs):
        file_path = kwargs['file_path']
        data = pd.read_excel(file_path)

        # Print out the column names to debug
        print("Columns in the Excel file:")
        print(data.columns)

        # Print out the first few rows to see the data
        print("\nSample data:")
        print(data.head())

        for index, row in data.iterrows():
            # Print the row to debug any issues
            print(f"\nRow {index}:")
            print(row)

            pet = Pet(
                timestamp=row.get('Отметка времени'),
                shelter_name=row.get('Название приюта'),
                animal_type=row.get('Какое животное?'),
                pet_name=row.get('Имя питомца'),
                breed=row.get('Порода (если неизвестна оставьте -)'),
                photo=row.get('Фотография (если есть)'),
                gender=row.get('Пол питомца'),
                age=row.get('Возраст'),
                size=row.get('Размер питомца'),
                shelter_duration=row.get('Как долго питомец находился в приюте?'),
                medical_conditions=row.get('Есть ли медицинские особенности или хронические заболевания?'),
                vaccines=row.get('Какие вакцины были сделаны и когда последний раз была обработка от блох и глистов?'),
                character=row.get('Описать характер питомца'),
                behavior=row.get('Есть ли какие-то особенности поведения (например, страхи, привычки)?'),
                commands=row.get('Какие команды знает питомец (если речь о собаке)?'),
                relation_to_people=row.get('Отношение к людям (включая детей)'),
                relation_to_animals=row.get('Отношение к другим животным'),
                availability=row.get('Есть ли питомец в настоящее время в приюте или он доступен для усыновления?')
            )
            pet.save()