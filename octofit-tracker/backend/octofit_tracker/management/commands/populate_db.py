from django.core.management.base import BaseCommand
from pymongo import MongoClient
from django.conf import settings

class Command(BaseCommand):
    help = 'Populate the database with test data for users, teams, activity, leaderboard, and workouts'

    def handle(self, *args, **kwargs):
        client = MongoClient(settings.MONGO_CLIENT_SETTINGS['host'], settings.MONGO_CLIENT_SETTINGS['port'])
        db = client[settings.MONGO_CLIENT_SETTINGS['db_name']]

        # Limpar coleções existentes
        db.users.drop()
        db.teams.drop()
        db.activity.drop()
        db.leaderboard.drop()
        db.workouts.drop()

        # Inserir dados de teste
        db.users.insert_many([
            {"_id": "1", "username": "thundergod", "email": "thundergod@mhigh.edu", "password": "thundergodpassword"},
            {"_id": "2", "username": "metalgeek", "email": "metalgeek@mhigh.edu", "password": "metalgeekpassword"},
            {"_id": "3", "username": "zerocool", "email": "zerocool@mhigh.edu", "password": "zerocoolpassword"},
            {"_id": "4", "username": "crashoverride", "email": "crashoverride@hmhigh.edu", "password": "crashoverridepassword"},
            {"_id": "5", "username": "sleeptoken", "email": "sleeptoken@mhigh.edu", "password": "sleeptokenpassword"},
        ])

        db.teams.insert_many([
            {"_id": "1", "name": "Blue Team", "members": ["1", "2", "3"]},
            {"_id": "2", "name": "Gold Team", "members": ["4", "5"]},
        ])

        db.activity.insert_many([
            {"_id": "1", "user": "1", "activity_type": "Cycling", "duration": "01:00:00"},
            {"_id": "2", "user": "2", "activity_type": "Crossfit", "duration": "02:00:00"},
            {"_id": "3", "user": "3", "activity_type": "Running", "duration": "01:30:00"},
            {"_id": "4", "user": "4", "activity_type": "Strength", "duration": "00:30:00"},
            {"_id": "5", "user": "5", "activity_type": "Swimming", "duration": "01:15:00"},
        ])

        db.leaderboard.insert_many([
            {"_id": "1", "user": "1", "score": 100},
            {"_id": "2", "user": "2", "score": 90},
            {"_id": "3", "user": "3", "score": 95},
            {"_id": "4", "user": "4", "score": 85},
            {"_id": "5", "user": "5", "score": 80},
        ])

        db.workouts.insert_many([
            {"_id": "1", "name": "Cycling Training", "description": "Training for a road cycling event"},
            {"_id": "2", "name": "Crossfit", "description": "Training for a crossfit competition"},
            {"_id": "3", "name": "Running Training", "description": "Training for a marathon"},
            {"_id": "4", "name": "Strength Training", "description": "Training for strength"},
            {"_id": "5", "name": "Swimming Training", "description": "Training for a swimming competition"},
        ])

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))
