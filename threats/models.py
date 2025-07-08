from django.db import models

class Threat(models.Model):
    threat_category = models.CharField(max_length=100)
    iocs = models.TextField(verbose_name="IOCs (Indicators of Compromise)")
    threat_actor = models.CharField(max_length=200)
    attack_vector = models.CharField(max_length=200)
    geo_location = models.CharField(max_length=100)
    forum_sentiment = models.CharField(max_length=50)
    severity_score = models.IntegerField()
    predicted_category = models.CharField(max_length=100)
    suggested_defense = models.TextField()
    risk_level = models.CharField(max_length=50)
    cleaned_description = models.TextField()
    keywords = models.TextField()
    named_entities = models.TextField()
    topic_labels = models.TextField()
    word_count = models.IntegerField()

    def __str__(self):
        return f"{self.threat_category} ({self.severity_score})"
