from django.db import models
from .utils import process_document  # You will define this function
import os
from django.conf import settings

class Document(models.Model):
    file = models.FileField(upload_to='documents/')
    name = models.CharField(max_length=255)
    uploaded_at = models.DateTimeField(auto_now_add=True)


    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        try:
            # Trigger processing after saving the file
            file_path = os.path.join(settings.MEDIA_ROOT, str(self.file))
            print(f"Processing document: {self.name} at path: {file_path}")
            
            # Check if file exists
            if not os.path.exists(file_path):
                print(f"Error: File does not exist at {file_path}")
                return
                
            process_document(file_path, self.name)
            print(f"Document processing completed for: {self.name}")
            
        except Exception as e:
            print(f"Error in Document.save() for {self.name}: {str(e)}")
            # Don't raise the exception to prevent the save from failing
