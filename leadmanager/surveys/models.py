from django.db import models
from django import forms
from multiselectfield import MultiSelectField

# Create your models here.


class Survey(models.Model):
    JOB_CHOICES = (
        ('company', 'Company'),
        ('home', 'Home'),
        ('teach', 'Teach'),
        ('army', 'Army'),
        ('none', 'None'),
    )

    HAVEJOB_CHOICES = (
        ('yes', 'Yes'),
        ('no', 'No'),
    )

    TERMJOB_CHOICES = (
        ('twoless', 'Twoless'),
        ('twomore', 'Twomore'),
        ('many', 'Many')
    )

    MANAGEJOB_CHOICES = (
        ('yes', 'Yes'),
        ('no', 'No'),
    )

    STUDENT_CHOICES = (
        ('yes', 'Yes'),
        ('no', 'No'),
    )

    HAVELESSON_CHOICES = (
        ('degree', 'Degree'),
        ('lifetime', 'Lifetime'),
        ('language', 'Language'),
    )

    LIVE_CHOICES = (
        ('solo', 'Solo'),
        ('duo', 'Duo'),
        ('family', 'Family'),
        ('school', 'School'),
        ('bunker', 'Bunker'),
    )

    # 다중 문항
    LEISURE_CHOICES = (
        ('movie', 'Movie'),
        ('club', 'Club'),
        ('perform', 'Perform'),
        ('concert', 'Concert'),
        ('museum', 'Museum'),
        ('park', 'Park'),
        ('camping', 'Camping'),
        ('beach', 'Beach'),
        ('sports', 'Sports'),
        ('house', 'House'),
        ('bar', 'Bar'),
        ('cafe', 'Cafe'),
        ('game', 'Game'),
        ('poll', 'Poll'),
        ('chess', 'Chess'),
        ('sns', 'Sns'),
        ('message', 'Message'),
        ('study', 'Study'),
        ('news', 'News'),
        ('cook', 'Cook'),
        ('drive', 'Drive'),
        ('spa', 'Spa'),
        ('job', 'Job'),
        ('service', 'Service'),
    )

    HOBBY_CHOICES = (
        ('book', 'Book'),
        ('music', 'Music'),
        ('play', 'Play'),
        ('sing', 'Sing'),
        ('dance', 'Dance'),
        ('write', 'Write'),
        ('drawing', 'Drawing'),
        ('cook', 'Cook'),
        ('animal', 'Animal'),
        ('stock', 'Stock'),
        ('news', 'News'),
        ('magazine', 'Magazine'),
        ('photo', 'Photo'),
    )

    SPORTS_CHOICES = (
        ('basketball', 'Basketball'),
        ('baseball', 'Baseball'),
        ('soccer', 'Soccer'),
        ('football', 'Football'),
        ('hockey', 'Hockey'),
        ('cricket', 'Cricket'),
        ('golf', 'Golf'),
        ('volleyball', 'Volleyball'),
        ('tennis', 'Tennis'),
        ('badminton', 'Badminton'),
        ('pingpong', 'Pingpong'),
        ('swimming', 'Swimming'),
        ('bicycle', 'Bicycle'),
        ('ski', 'Ski'),
        ('skate', 'Skate'),
        ('jogging', 'Jogging'),
        ('walking', 'Walking'),
        ('yoga', 'Yoga'),
        ('hiking', 'Hiking'),
        ('fishing', 'Fishing'),
        ('health', 'Health'),
        ('taekwondo', 'Taekwondo'),
        ('lesson', 'Lesson'),
        ('none', 'None'),
    )

    REST_CHOICES = (
        ('inbusiness', 'Inbusiness'),
        ('outbusiness', 'Outbusiness'),
        ('home', 'Home'),
        ('intravle', 'Intravle'),
        ('outtravle', 'Outtravle'),
    )

    job = models.CharField(max_length=100,
                           choices=JOB_CHOICES, null=True)
    haveJob = models.CharField(max_length=100,
                               choices=HAVEJOB_CHOICES, null=True)
    TermJob = models.CharField(max_length=100,
                               choices=TERMJOB_CHOICES, null=True)
    ManageJob = models.CharField(max_length=100,
                                 choices=MANAGEJOB_CHOICES, null=True)
    Student = models.CharField(max_length=100,
                               choices=STUDENT_CHOICES, null=True)
    HaveLesson = models.CharField(max_length=100,
                                  choices=HAVELESSON_CHOICES, null=True)
    Live = models.CharField(max_length=100,
                            choices=LIVE_CHOICES, null=True)
    Leisure = MultiSelectField(choices=LEISURE_CHOICES, null=True)
    Hobby = MultiSelectField(choices=HOBBY_CHOICES, null=True)
    Sports = MultiSelectField(choices=SPORTS_CHOICES, null=True)
    Rest = MultiSelectField(choices=REST_CHOICES, null=True)
