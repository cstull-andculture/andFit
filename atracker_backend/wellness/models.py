from django.db import models
from django.core.exceptions import ValidationError
from django.db.models.functions import Now

# Create your models here.


# Validators
def validate_birth_sex(birthAssignedSex):
    validBirthSexes = ["male", "female", "other"]
    if not validBirthSexes.contains(birthAssignedSex.lower()):
        raise ValidationError(
            "Invalid birth sex entered. Must be Male, Female, or Other.",
            params={'birthAssignedSex', birthAssignedSex}
        )


def validate_resistance_type(resistanceType):
    validResistanceTypes = ["body weight", "free weight", "cables", "machine"]
    if not validResistanceTypes.contains(resistanceType.lower()):
        raise ValidationError(
            "Invalid resistance type. Must be one of 'body weight', 'free weight', 'cables', or 'machine'",
            params={'resistanceType': resistanceType}
        )


# Models
class User(models.Model):
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=50)
    emailAddress = models.EmailField(unique=True)
    age = models.IntegerField()
    gender = models.CharField(max_length=20)
    birthAssignedSex = models.CharField(max_length=10, validators=[validate_birth_sex])
    currentSex = models.CharField(max_length=20)


class MuscleGroup(models.Model):
    name = models.CharField(max_length=30)


class Workout(models.Model):
    datetime = models.DateTimeField(null=False, default=Now())
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=40, default="")


class Lift(models.Model):
    name = models.CharField(max_length=40)
    resistanceType = models.CharField(max_length=20, validators=[validate_resistance_type])
    weight = models.FloatField()
    repsPerSet = models.IntegerField()
    primaryMuscleId = models.ForeignKey(MuscleGroup, on_delete=models.DO_NOTHING, related_name="primaryMuscle")
    compound = models.BooleanField(default=False)
    secondaryMuscleId = models.ForeignKey(MuscleGroup, on_delete=models.DO_NOTHING, related_name="secondaryMuscle")
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE)


class Cardio(models.Model):
    name = models.CharField(max_length=100)
    resistanceType = models.CharField(max_length=20, validators=[validate_resistance_type])
    distance = models.FloatField(null=True)
    duration = models.FloatField(null=True)
    reps = models.IntegerField(null=True)


