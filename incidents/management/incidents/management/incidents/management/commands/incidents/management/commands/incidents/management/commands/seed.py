from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from incidents.models import Category, Incident

class Command(BaseCommand):
    help = 'Seed database with default data'

    def handle(self, *args, **kwargs):
        # Create admin user
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
            self.stdout.write(self.style.SUCCESS('Created admin user'))

        # Create categories
        categories = ['Accident', 'Fighting', 'Rioting', 'Theft', 'Fire', 'Other']
        for name in categories:
            Category.objects.get_or_create(name=name)
            self.stdout.write(self.style.SUCCESS(f'Created category: {name}'))

        # Create demo incidents
        if not Incident.objects.exists():
            admin = User.objects.get(username='admin')
            accident = Category.objects.get(name='Accident')
            fighting = Category.objects.get(name='Fighting')
            
            Incident.objects.create(
                reporter=admin,
                category=accident,
                title='Car Accident on Main Street',
                description='A serious car accident occurred at the intersection. Two vehicles involved.',
                latitude='6.5244',
                longitude='3.3792'
            )
            
            Incident.objects.create(
                reporter=admin,
                category=fighting,
                title='Street Fight Near Market',
                description='Physical altercation between two groups reported near the central market area.',
                latitude='6.5123',
                longitude='3.3845'
            )
            
            self.stdout.write(self.style.SUCCESS('Created demo incidents'))

        self.stdout.write(self.style.SUCCESS('Database seeded successfully!'))
