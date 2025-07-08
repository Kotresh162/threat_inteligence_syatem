import csv
from django.utils.text import slugify
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'threat_inteligence_system.settings')
django.setup()

from threats.models import Threat

with open('Cybersecurity_Dataset.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        Threat.objects.create(
            threat_category=row['Threat Category'].strip(),
            iocs=row['IOCs (Indicators of Compromise)'].strip(),
            threat_actor=row['Threat Actor'].strip(),
            attack_vector=row['Attack Vector'].strip(),
            geo_location=row['Geographical Location'].strip(),
            forum_sentiment=row['Sentiment in Forums'].strip(),
            severity_score=int(row['Severity Score']),
            predicted_category=row['Predicted Threat Category'].strip(),
            suggested_defense=row['Suggested Defense Mechanism'].strip(),
            risk_level=row['Risk Level Prediction'].strip(),
            cleaned_description=row['Cleaned Threat Description'].strip(),
            keywords=row['Keyword Extraction'].strip(),
            named_entities=row['Named Entities (NER)'].strip(),
            topic_labels=row['Topic Modeling Labels'].strip(),
            word_count=int(row['Word Count'])
        )
print("Data ingestion completed successfully.")
