from django.core.management.base import BaseCommand

from incidents.models import Category


class Command(BaseCommand):
    help = "Create the default incident categories."

    def handle(self, *args, **options):
        names = ["Accident", "Fighting", "Rioting", "Theft", "Fire", "Other"]
        for name in names:
            Category.objects.get_or_create(name=name)
        self.stdout.write(self.style.SUCCESS("Default categories are ready."))
