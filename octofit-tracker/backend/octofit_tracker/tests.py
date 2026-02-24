from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class ModelTestCase(TestCase):
    def setUp(self):
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')
        user = User.objects.create(name='Iron Man', email='ironman@marvel.com', team=marvel)
        workout = Workout.objects.create(name='Test Workout', description='desc')
        workout.suggested_for.set([user])
        Activity.objects.create(user=user, type='Running', duration=30, date='2026-02-24')
        Leaderboard.objects.create(team=marvel, score=100, week='2026-W08')

    def test_user(self):
        self.assertEqual(User.objects.count(), 1)
    def test_team(self):
        self.assertEqual(Team.objects.count(), 2)
    def test_activity(self):
        self.assertEqual(Activity.objects.count(), 1)
    def test_workout(self):
        self.assertEqual(Workout.objects.count(), 1)
    def test_leaderboard(self):
        self.assertEqual(Leaderboard.objects.count(), 1)
