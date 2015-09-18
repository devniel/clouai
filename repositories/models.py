from django.db import models
from authentication.models import User
from django.utils.translation import ugettext_lazy as _

# OAI Repository
class Repository(models.Model):
	owner = models.ForeignKey(User)
	name = models.CharField(max_length=40, unique=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __unicode__(self):
		return self.name

	class Meta:
		verbose_name = _("Repository")
		verbose_name_plural = _("Repositories")

# OAI Set
class Set(models.Model):
	repository = models.ForeignKey(Repository)
	name = models.CharField(max_length=40, unique=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __unicode__(self):
		return self.name + " :: " + self.repository.name

	class Meta:
		verbose_name = _("Set")
		verbose_name_plural = _("Sets")

# OAI Record
class Record(models.Model):
	repository = models.ForeignKey(Repository)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __unicode__(self):
		return str(self.id) + " :: " + self.repository.name

	class Meta:
		verbose_name = _("Record")
		verbose_name_plural = _("Records")

# OAI Property
class Property(models.Model):
	name = models.CharField(max_length=100, unique=True)
	created_at = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return self.name

	class Meta:
		verbose_name = _("Property")
		verbose_name_plural = _("Properties")

# OAI Record Property
class RecordProperty(models.Model):
	record = models.ForeignKey(Record)
	property = models.ForeignKey(Property)
	value = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return "Record " + str(self.record.id) + " | " + self.property.name + " = " + self.value

	class Meta:
		verbose_name = _("RecordProperty")
		verbose_name_plural = _("RecordProperties")

# OAI Record Set
class RecordSet(models.Model):
	record = models.ForeignKey(Record)
	set = models.ForeignKey(Set)
	created_at = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return "Record " + str(self.record.id) + " is part of Set " + self.set.id

	class Meta:
		verbose_name = _("RecordSet")
		verbose_name_plural = _("RecordSets")