from django.db import models

class Person(models.Model):
    image = models.ImageField(upload_to='person_images', blank=True, null=True)
    about = models.TextField(blank=True)
    email = models.EmailField(max_length=254, blank=True)
    phone_number = models.CharField(max_length=20, blank=True)
    instagram = models.URLField(max_length=200, blank=True)
    twitter = models.URLField(max_length=200, blank=True)
    linkedin = models.URLField(max_length=200, blank=True)
    github = models.URLField(max_length=200, blank=True)
    datawars = models.URLField(max_length=200, blank=True)

    def __str__(self):
        return f'Person #{self.pk}'


class Works(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='works_images/')
    link = models.URLField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.name

class Skill_0(models.Model):
    heading = models.CharField(max_length=200)
    skill_01 = models.CharField(max_length=200, blank=True)
    skill_02 = models.CharField(max_length=200, blank=True)
    skill_03 = models.CharField(max_length=200, blank=True)
    skill_04 = models.CharField(max_length=200, blank=True)
    skill_05 = models.CharField(max_length=200, blank=True)
    skill_06 = models.CharField(max_length=200, blank=True)
    skill_07 = models.CharField(max_length=200, blank=True)
    skill_08 = models.CharField(max_length=200, blank=True)
    skill_09 = models.CharField(max_length=200, blank=True)
    skill_10 = models.CharField(max_length=200, blank=True)
    skill_11 = models.CharField(max_length=200, blank=True)
    skill_12 = models.CharField(max_length=200, blank=True)
    skill_13 = models.CharField(max_length=200, blank=True)
    

    def __str__(self):
        return self.heading


class Skill_1(models.Model):
    heading_1 = models.CharField(max_length=200, blank=True)
    skill_14 = models.CharField(max_length=200, blank=True)
    skill_15 = models.CharField(max_length=200, blank=True)
    skill_16 = models.CharField(max_length=200, blank=True)
    skill_17 = models.CharField(max_length=200, blank=True)
    skill_18 = models.CharField(max_length=200, blank=True)
    skill_19 = models.CharField(max_length=200, blank=True)
    skill_20 = models.CharField(max_length=200, blank=True)
    skill_21 = models.CharField(max_length=200, blank=True)
    skill_22 = models.CharField(max_length=200, blank=True)
    skill_23 = models.CharField(max_length=200, blank=True)
    skill_24 = models.CharField(max_length=200, blank=True)
    skill_25 = models.CharField(max_length=200, blank=True)
    skill_26 = models.CharField(max_length=200, blank=True)
    
    

    def __str__(self):
        return self.heading_1
        
class Skill_2(models.Model):
    heading_2 = models.CharField(max_length=200)  
    skill_27 = models.CharField(max_length=200, blank=True)
    skill_28 = models.CharField(max_length=200, blank=True)
    skill_29 = models.CharField(max_length=200, blank=True)
    skill_30 = models.CharField(max_length=200, blank=True)
    skill_31 = models.CharField(max_length=200, blank=True)
    skill_32 = models.CharField(max_length=200, blank=True)
    skill_33 = models.CharField(max_length=200, blank=True)
    skill_34 = models.CharField(max_length=200, blank=True)
    skill_35 = models.CharField(max_length=200, blank=True)
    skill_36 = models.CharField(max_length=200, blank=True)
    skill_37 = models.CharField(max_length=200, blank=True)
    skill_38 = models.CharField(max_length=200, blank=True)
    skill_39 = models.CharField(max_length=200, blank=True)
    

    def __str__(self):
        return self.heading_2
        
class Skill_3(models.Model):
    heading_3 = models.CharField(max_length=200)
    skill_40 = models.CharField(max_length=200, blank=True)
    skill_41 = models.CharField(max_length=200, blank=True)
    skill_42 = models.CharField(max_length=200, blank=True)
    skill_43 = models.CharField(max_length=200, blank=True)
    skill_44 = models.CharField(max_length=200, blank=True)
    skill_45 = models.CharField(max_length=200, blank=True)
    skill_46 = models.CharField(max_length=200, blank=True)
    skill_47 = models.CharField(max_length=200, blank=True)
    skill_48 = models.CharField(max_length=200, blank=True)
    skill_49 = models.CharField(max_length=200, blank=True)
    skill_50 = models.CharField(max_length=200, blank=True)
    skill_51 = models.CharField(max_length=200, blank=True)
    skill_52 = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.heading_3

class Skill_4(models.Model):
    heading_4 = models.CharField(max_length=200)
    skill_53 = models.CharField(max_length=200, blank=True)
    skill_54 = models.CharField(max_length=200, blank=True)
    skill_55 = models.CharField(max_length=200, blank=True)
    skill_56 = models.CharField(max_length=200, blank=True)
    skill_57 = models.CharField(max_length=200, blank=True)
    skill_58 = models.CharField(max_length=200, blank=True)
    skill_59 = models.CharField(max_length=200, blank=True)
    skill_60 = models.CharField(max_length=200, blank=True)
    skill_61 = models.CharField(max_length=200, blank=True)
    skill_62 = models.CharField(max_length=200, blank=True)
    skill_63 = models.CharField(max_length=200, blank=True)
    skill_64 = models.CharField(max_length=200, blank=True)
    skill_65 = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.heading_4

class Skill_5(models.Model):
    heading_5 = models.CharField(max_length=200)
    skill_66 = models.CharField(max_length=200, blank=True)
    skill_67 = models.CharField(max_length=200, blank=True)
    skill_68 = models.CharField(max_length=200, blank=True)
    skill_69 = models.CharField(max_length=200, blank=True)
    skill_70 = models.CharField(max_length=200, blank=True)
    skill_71 = models.CharField(max_length=200, blank=True)
    skill_72 = models.CharField(max_length=200, blank=True)
    skill_73 = models.CharField(max_length=200, blank=True)
    skill_74 = models.CharField(max_length=200, blank=True)
    skill_75 = models.CharField(max_length=200, blank=True)
    skill_76 = models.CharField(max_length=200, blank=True)
    skill_77 = models.CharField(max_length=200, blank=True)
    skill_78 = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.heading_5

