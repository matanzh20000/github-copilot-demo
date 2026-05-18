from django.db import models

# Users Collection
class User(models.Model):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255)

# Teams Collection
class Team(models.Model):
    name = models.CharField(max_length=255)
    members = models.ManyToManyField(User)

# Activity Collection
class Activity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    activity_type = models.CharField(max_length=255)
    duration = models.IntegerField()

# Leaderboard Collection
class Leaderboard(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField()

# Workouts Collection
class Workout(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()