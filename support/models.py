from django.db import models


class Prompt(models.Model):
    """A guided reflection prompt to help someone process grief."""

    STAGE_CHOICES = [
        ("early", "Early days"),
        ("processing", "Processing"),
        ("remembering", "Remembering"),
        ("moving_forward", "Moving forward"),
    ]

    text = models.TextField(help_text="The reflection question or prompt.")
    stage = models.CharField(
        max_length=20, choices=STAGE_CHOICES, default="processing"
    )
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["stage", "id"]

    def __str__(self):
        return self.text[:60]


class Resource(models.Model):
    """A support resource: hotline, article, book, or organization."""

    KIND_CHOICES = [
        ("hotline", "Hotline"),
        ("article", "Article"),
        ("book", "Book"),
        ("organization", "Organization"),
    ]

    title = models.CharField(max_length=200)
    kind = models.CharField(max_length=20, choices=KIND_CHOICES)
    description = models.TextField(blank=True)
    url = models.URLField(blank=True)
    phone = models.CharField(max_length=40, blank=True)

    class Meta:
        ordering = ["kind", "title"]

    def __str__(self):
        return self.title


class JournalEntry(models.Model):
    """A private written response to a prompt, tied to a browser session."""

    prompt = models.ForeignKey(
        Prompt, on_delete=models.SET_NULL, null=True, blank=True,
        related_name="entries",
    )
    session_key = models.CharField(max_length=40, db_index=True)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created"]
        verbose_name_plural = "journal entries"

    def __str__(self):
        return f"Entry {self.pk} ({self.created:%Y-%m-%d})"
