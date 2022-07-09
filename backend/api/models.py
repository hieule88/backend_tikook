from tkinter import CASCADE
from django.db import models
import mongoengine

from django.core.validators import MaxValueValidator, MinValueValidator


class MeasurementUnit(models.Model):
	MeasurementUnitID = models.AutoField(primary_key=True)


class ReviewImage(models.Model):
	ImageID = models.AutoField(primary_key=True)
	URL = models.CharField()
	Review = models.ForeignKey('Review', on_delete=CASCADE)

class User(models.Model):
	UserID = models.AutoField(primary_key=True)
	Name = models.CharField(max_length=20)
	FollowCount = models.IntegerField(max_length=10)
	FollowerCount = models.IntegerField(max_length=10)
	PFP = models.ForeignKey('ImageURL')


class Review(models.Model):
	ReviewID = models.AutoField(primary_key=True)
	Comment = models.CharField()
	Rating = models.IntegerField(validators=[MaxValueValidator(5), MinValueValidator(1)])
	User = models.ForeignKey('User')
	Recipe = models.ForeignKey('Recipe', on_delete=CASCADE)
	

class Saved(models.Model):
	SavedID = models.AutoField(primary_key=True)
	Recipe = models.ForeignKey('Recipe')
	User = models.ForeignKey('User')


class Ingredient(models.Model):
	IngredientID = models.AutoField(primary_key=True)
	Name = models.CharField(max_length=20)
	UrlNgon = models.CharField()
	Calories = models.IntegerField()
	Carbs = models.FloatField()
	Fat = models.FloatField()
	Protein = models.FloatField()


class IngredientRecipe(models.Model):
	IngredientID = models.Fore


class Recipe(models.Model):
	RecipeID = models.AutoField(primary_key=True)
	Title = models.CharField(max_length=200)
	Category = models.CharField(max_length=20)

	Rating = models.FloatField(max_length=5)
	RatingCount = models.IntegerField(max_length=10)
	SavedCount = models.IntegerField(max_length=10)

	EstimatedTime = models.IntegerField(max_length=3)
	Servings = models.IntegerField(max_length=3)

	User = models.ForeignKey('User')

	



