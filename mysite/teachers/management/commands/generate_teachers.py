from django.core.management.base import BaseCommand

from faker import Faker

from teachers.models import Teachers

faker = Faker()


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument("count", nargs="?", type=int, default=100)

    def handle(self, *args, **options):
        teachers_count = options["count"]
        for _ in range(teachers_count):
            Teachers.objects.create(
                first_name=faker.first_name(),
                last_name=faker.last_name(),
                subject=faker.random_element(
                    elements=["Math", "Biology", "English", "History"]
                ),
            )
        self.stdout.write(
            self.style.SUCCESS(f"Successfully created {teachers_count} teacher(s)")
        )
