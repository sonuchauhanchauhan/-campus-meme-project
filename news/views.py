import random
import os
from groq import Groq
from django.shortcuts import render
from .models import Student, News


client = Groq(api_key=os.getenv("GROQ_API_KEY"))



fallback_memes = [
    "BREAKING: Rahul ko library me padhte dekha gaya, campus shock me",
    "Ganesh coding me zero aur LinkedIn pe AI engineer likh raha",
    "Vaibhav ka attendance kam hai par canteen me permanent seat hai",
    "Yash ka project itna confusing hai ki ChatGPT bhi resign kare",
    "Alok startup founder banna chahta hai par assignment pending",
    "Rahul aur Ganesh group project me sirf seen karte hain",
]

def generate_savage_roast(s1, s2):

    memes = [

        f"BREAKING: {s1} ko assignment submit karte dekha gaya, professor shock me",

        f"{s1} coding kar raha tha, compiler ne therapy book kar li",

        f"{s2} ko library me padhte dekha gaya, campus investigation chal rahi",

        f"{s1} ne assignment khud likha, Turnitin emotional ho gaya",

        f"{s2} class me time par aaya, professor suspicious ho gaye",

        f"{s1} group project me sirf 'seen' karta hai",

        f"{s2} ka attendance itna rare hai professor usko myth bolte",

        f"{s1} coding kar raha tha, laptop ne restart maang liya",

        f"{s2} ne ek line code likha, pura batch celebration kar raha",

        f"{s1} ko padhte dekha gaya, students shock me",

        f"{s2} ka project dekh ke ChatGPT bhi confuse ho gaya",

        f"{s1} assignment likh raha tha, doston ne emergency meeting bulayi",

        f"{s2} coding kar raha tha, Google search history leak ho gayi",

        f"{s1} ka attendance kam hai par canteen me permanent seat hai",

        f"{s2} ne class attend ki, campus me breaking news ban gayi",

        f"{s1} coding karte pakda gaya, keyboard bhi nervous ho gaya",

        f"{s2} ne assignment submit kiya, professor ko doubt ho gaya",

        f"{s1} ko padhte dekha gaya, CCTV footage verify ho rahi",

        f"{s2} coding kar raha tha, compiler ne error nahi diya",

        f"{s1} class me focus kar raha tha, doston ko tension ho gaya",

    ]

    return random.choice(memes)

def home(request):

    students = list(Student.objects.all())

    if len(students) >= 2:

        random.shuffle(students)

        s1 = students[0].name
        s2 = students[1].name

        headline = generate_savage_roast(s1, s2)

        News.objects.create(headline=headline)

    all_news = News.objects.order_by("-created_at")[:10]

    context = {
        "all_news": all_news,
        "live_readers": random.randint(80, 200),
    }

    return render(request, "news/index.html", context)