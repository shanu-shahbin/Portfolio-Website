from django.shortcuts import render
from .models import Person, Skill_0, Skill_1, Skill_2, Skill_3, Skill_4, Skill_5, Works

def Skills(request):
    return render(request, 'skills.html')

def home(request):
    # Retrieve the first Person object from the database
    person = Person.objects.first()
    skills = Skill_0.objects.first()
    skill_1 = Skill_1.objects.first()
    skill_2 = Skill_2.objects.first()
    skill_3 = Skill_3.objects.first()
    skill_4 = Skill_4.objects.first()
    skill_5 = Skill_5.objects.first()

    works = Works.objects.first()
    work1name = works.name
    work1description = works.description
    work1link = works.link
    work1image = works.image

    works_objects = Works.objects.all()
    second_work = works_objects[1]
    work2name = second_work.name
    work2description = second_work.description
    work2link = second_work.link
    work2image = second_work.image

    third_work = works_objects[2]
    work3name = third_work.name
    work3description = third_work.description
    work3link = third_work.link
    work3image = third_work.image






    # Extract information from the person instance
    image_url = person.image.url if person.image else None
    about = person.about
    email = person.email
    phone_number = person.phone_number
    instagram_link = person.instagram
    twitter_link = person.twitter
    linkedin_link = person.linkedin
    github_link = person.github
    datawars_link = person.datawars

    
    
    # Convert Skill_0 object to dictionary
    skills_dict = {
        'heading': skills.heading,
        'skill_01': skills.skill_01,
        'skill_02': skills.skill_02,
        'skill_03': skills.skill_03,
        'skill_04': skills.skill_04,
        'skill_05': skills.skill_05,
        'skill_06': skills.skill_06,
        'skill_07': skills.skill_07,
        'skill_08': skills.skill_08,
        
        
    }

    # Convert Skill_1 object to dictionary
    skills_dict_1 = {
        'heading_1':skill_1.heading_1,
        'skill_14': skill_1.skill_14,
        'skill_15': skill_1.skill_15,
        'skill_16': skill_1.skill_16,
        'skill_17': skill_1.skill_17,
        'skill_18': skill_1.skill_18,
        'skill_19': skill_1.skill_19,
        'skill_20': skill_1.skill_20,
        'skill_21': skill_1.skill_21,
        
    }

    skills_dict_2 = {
        'heading_2':skill_2.heading_2,
        'skill_27': skill_2.skill_27,
        'skill_28': skill_2.skill_28,
        'skill_29': skill_2.skill_29,
        'skill_30': skill_2.skill_30,
        'skill_31': skill_2.skill_31,
        'skill_32': skill_2.skill_32,
        'skill_33': skill_2.skill_33,
        'skill_34': skill_2.skill_34,
        
    }

    skills_dict_3 = {
        'heading_3': skill_3.heading_3, 
        'skill_40': skill_3.skill_40,
        'skill_41': skill_3.skill_41,
        'skill_42': skill_3.skill_42,
        'skill_43': skill_3.skill_43,
        'skill_44': skill_3.skill_44,
        'skill_45': skill_3.skill_45,
        'skill_46': skill_3.skill_46,
        
    }

    skills_dict_4 = {
        'heading_4': skill_4.heading_4,
        'skill_53': skill_4.skill_53,
        'skill_54': skill_4.skill_54,
        'skill_55': skill_4.skill_55,
        'skill_56': skill_4.skill_56,
        'skill_57': skill_4.skill_57,
        'skill_58': skill_4.skill_58,
        'skill_59': skill_4.skill_59,
        'skill_60': skill_4.skill_60,
        
    }

    skills_dict_5 = {
        'heading_5': skill_5.heading_5,
        'skill_66': skill_5.skill_66,
        'skill_67': skill_5.skill_67,
        'skill_68': skill_5.skill_68,
        'skill_69': skill_5.skill_69,
        'skill_70': skill_5.skill_70,
        'skill_71': skill_5.skill_71,
        'skill_72': skill_5.skill_72,
        'skill_73': skill_5.skill_73,

        }


    # Pass the information to the template
    return render(request, 'base.html', {
        'image_url': image_url,
        'about': about,
        'email': email,
        'phone_number': phone_number,
        'instagram_link': instagram_link,
        'twitter_link': twitter_link,
        'linkedin_link': linkedin_link,
        'github_link': github_link,
        'datawars_link': datawars_link,
        'skills': skills_dict,
        'skills_1': skills_dict_1,
        'skills_2': skills_dict_2,
        'skills_3': skills_dict_3,
        'skills_4': skills_dict_4,
        'skills_5': skills_dict_5,
        'work1name': work1name,
        'work1description': work1description,
        'work1link': work1link,
        'work1image': work1image,
        'work2name': work2name,
        'work2description': work2description,
        'work2link': work2link,
        'work2image': work2image,
        'work3name': work3name,
        'work3description': work3description,
        'work3link': work3link,
        'work3image': work3image,    

    })
