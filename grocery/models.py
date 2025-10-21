from django.db import models
from django.contrib.auth.models import User

class grocery_item(models.Model):
	CATEGORY_SECTIONS = [
		('dry', 'Dry'),
		('frozen', 'Frozen'),
		('meat', 'Meat'),
		('dairy', 'Dairy'),
		('produce', 'Produce'),
		('bakery', 'Bakery'),
		('other', 'Other'),
	]

	name = models.CharField(max_length=50)
	quantity = models.CharField(max_length=50)
	section = models.CharField(max_length=15, choices=CATEGORY_SECTIONS)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	date_added = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ["date_added"]

	def __str__(self):
		return f"{self.name} ({self.quantity})"
