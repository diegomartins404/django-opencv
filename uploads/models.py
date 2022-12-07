from django.db import models

# Create your models here.
from .utils import NovaImagem
from PIL import Image
import numpy as np
from io import BytesIO
from django.core.files.base import ContentFile
# Create your models here.
class Upload(models.Model):
    image = models.ImageField(upload_to='images')
    
    def __str__(self):
        return str(self.id)
    
    def save(self, *args, **kwargs):
        pil_img = Image.open(self.image)
        cv_img = np.array(pil_img)
        img = NovaImagem(cv_img)
        
        im_pil = Image.fromarray(img)
        
        buffer = BytesIO()
        
        im_pil.save(buffer, format='png')
        
        image_png = buffer.getvalue()
        
        self.image.save(str(self.image), ContentFile(image_png), save=False)
        super().save(*args, **kwargs)