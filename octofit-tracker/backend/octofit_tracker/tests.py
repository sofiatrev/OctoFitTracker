from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout

class UserModelTest(TestCase):
    def test_user_creation(self):
        user = User.objects.create(username="testuser", email="testuser@example.com", password="password123")
        self.assertEqual(user.username, "testuser")
        self.assertEqual(user.email, "testuser@example.com")

class TeamModelTest(TestCase):
    def test_team_creation(self):
        user = User.objects.create(username="teamuser", email="teamuser@example.com", password="password123")
        team = Team.objects.create(name="Team A")
        team.members.add(user)
        self.assertEqual(team.name, "Team A")
        self.assertIn(user, team.members.all())

class ActivityModelTest(TestCase):
    def test_activity_creation(self):
        user = User.objects.create(username="activityuser", email="activityuser@example.com", password="password123")
        activity = Activity.objects.create(user=user, activity_type="Running", duration="00:30:00")
        self.assertEqual(activity.activity_type, "Running")
        self.assertEqual(activity.user, user)

class LeaderboardModelTest(TestCase):
    def test_leaderboard_creation(self):
        user = User.objects.create(username="leaderboarduser", email="leaderboarduser@example.com", password="password123")
        leaderboard = Leaderboard.objects.create(user=user, score=100)
        self.assertEqual(leaderboard.score, 100)
        self.assertEqual(leaderboard.user, user)

class WorkoutModelTest(TestCase):
    def test_workout_creation(self):
        workout = Workout.objects.create(name="Workout A", description="A sample workout")
        self.assertEqual(workout.name, "Workout A")
        self.assertEqual(workout.description, "A sample workout")