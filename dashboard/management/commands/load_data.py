from django.core.management.base import BaseCommand
import json
from dashboard.models import DataEntry

class Command(BaseCommand):
    help = 'Load data from a JSON file into the database'

    def handle(self, *args, **kwargs):
        try:
            with open('dashboard/jsondata.json', 'r', encoding='utf-8') as file:
                data = json.load(file)

            model_fields = {field.name for field in DataEntry._meta.fields}
            successful_entries = 0

            for item in data:
                # Filter the item to only include valid model fields
                filtered_item = {key: value for key, value in item.items() if key in model_fields}

                try:
                    DataEntry.objects.create(**filtered_item)
                    successful_entries += 1
                except Exception as e:
                    self.stderr.write(self.style.ERROR(f"Failed to insert item {filtered_item}: {e}"))

            self.stdout.write(self.style.SUCCESS(f'{successful_entries} entries loaded successfully'))

        except FileNotFoundError:
            self.stderr.write(self.style.ERROR("JSON file not found. Please make sure 'dashboard/jsondata.json' exists."))
        except json.JSONDecodeError as e:
            self.stderr.write(self.style.ERROR(f"Invalid JSON format: {e}"))
