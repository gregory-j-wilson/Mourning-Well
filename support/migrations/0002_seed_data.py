from django.db import migrations


def seed(apps, schema_editor):
    Prompt = apps.get_model("support", "Prompt")
    Resource = apps.get_model("support", "Resource")

    prompts = [
        ("What do you most need to hear right now?", "early"),
        ("Describe the last ordinary moment you shared. What made it feel like home?", "remembering"),
        ("What feeling has been hardest to name today?", "processing"),
        ("Write about a small kindness someone showed you recently.", "processing"),
        ("What would you want them to know about how you're carrying on?", "remembering"),
        ("What does grief feel like in your body today?", "early"),
        ("Name one thing you're allowing yourself not to do right now.", "early"),
        ("What memory makes you smile, even a little?", "remembering"),
        ("What has surprised you about grieving?", "processing"),
        ("What would 'gentle with yourself' look like tomorrow?", "moving_forward"),
        ("Who or what has felt like an anchor lately?", "moving_forward"),
        ("Write a short note to yourself six months from now.", "moving_forward"),
    ]
    for text, stage in prompts:
        Prompt.objects.create(text=text, stage=stage)

    resources = [
        ("988 Suicide & Crisis Lifeline", "hotline",
         "Free, confidential support 24/7 for anyone in emotional distress.",
         "https://988lifeline.org", "988"),
        ("Crisis Text Line", "hotline",
         "Text HOME to connect with a trained crisis counselor, 24/7.",
         "https://www.crisistextline.org", "Text HOME to 741741"),
        ("The Dougy Center", "organization",
         "Support for children, teens, and families who are grieving a death.",
         "https://www.dougy.org", ""),
        ("GriefShare", "organization",
         "Support groups that meet in communities around the world.",
         "https://www.griefshare.org", ""),
        ("It's OK That You're Not OK", "book",
         "Megan Devine on meeting grief in a culture that misunderstands it.",
         "", ""),
        ("The Year of Magical Thinking", "book",
         "Joan Didion's account of grief after sudden loss.",
         "", ""),
    ]
    for title, kind, desc, url, phone in resources:
        Resource.objects.create(
            title=title, kind=kind, description=desc, url=url, phone=phone
        )


def unseed(apps, schema_editor):
    apps.get_model("support", "Prompt").objects.all().delete()
    apps.get_model("support", "Resource").objects.all().delete()


class Migration(migrations.Migration):
    dependencies = [("support", "0001_initial")]
    operations = [migrations.RunPython(seed, unseed)]
