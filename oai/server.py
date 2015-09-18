from oaipmh.interfaces import IOAI
from oaipmh.common import Identify, Header, Metadata
from datetime import datetime
from repositories.models import Record,  Repository
from repositories.serializers import RecordSerializer
import random
from pprint import pprint
from oaipmh.error import *

from collections import defaultdict

class CLOUAI(IOAI):
	def __init__(self, repository_pk):
		repository = Repository.objects.get(pk=repository_pk)
		self.repository = repository

	def getRecord(self, metadataPrefix, identifier):
		"""Get a record for a metadataPrefix and identifier.
		metadataPrefix - identifies metadata set to retrieve
		identifier - repository-unique identifier of record
		
		Should raise error.CannotDisseminateFormatError if
		metadataPrefix is unknown or not supported by identifier.
		
		Should raise error.IdDoesNotExistError if identifier is
		unknown or illegal.
		Returns a header, metadata, about tuple describing the record.
		"""

		if metadataPrefix != 'oai_dc':
			raise CannotDisseminateFormatError

		try:
			record  = Record.objects.get(pk=identifier)	
			_record = RecordSerializer(record)
			properties = defaultdict(list)

			for property in _record.data.get('properties'):
				if not property.get('name') in properties:
					properties[property.get('name')] = list()
				properties[property.get('name')].append(property.get('value'))

			id = _record.data.get('id')

			data = (
				Header(id, id, datetime.now(), '', False), 
				Metadata(id, properties),
	            None
	        )
	        
			return data

		except Record.DoesNotExist:
			raise IdDoesNotExistError


	def identify(self):
		"""Retrieve information about the repository.
		Returns an Identify object describing the repository.
		"""

		return Identify(
            repositoryName=self.repository.name,
            baseURL='http://' + self.repository.name + '.clouai.org/oai',
            protocolVersion="2.0",
            adminEmails=[self.repository.owner.email],
            earliestDatestamp=datetime(2015, 07, 04),
            deletedRecord='transient',
            granularity='YYYY-MM-DDThh:mm:ssZ',
            compression=['identity']
        )


	def listIdentifiers(self, metadataPrefix, set=None, from_=None, until=None):
		"""Get a list of header information on records.
		metadataPrefix - identifies metadata set to retrieve
		set - set identifier; only return headers in set (optional)
		from_ - only retrieve headers from from_ date forward (optional)
		until - only retrieve headers with dates up to and including
				until date (optional)
		Should raise error.CannotDisseminateFormatError if metadataPrefix
		is not supported by the repository.
		Should raise error.NoSetHierarchyError if the repository does not
		support sets.
		
		Returns an iterable of headers.
		"""

		if set is not None:
			raise NoSetHierarchyError
		
	def listMetadataFormats(self, identifier=None):
		"""List metadata formats supported by repository or record.
		identifier - identify record for which we want to know all
					 supported metadata formats. if absent, list all metadata
					 formats supported by repository. (optional)
		Should raise error.IdDoesNotExistError if record with
		identifier does not exist.
		
		Should raise error.NoMetadataFormatsError if no formats are
		available for the indicated record.
		Returns an iterable of metadataPrefix, schema, metadataNamespace
		tuples (each entry in the tuple is a string).
		"""

		try:
			if identifier is not None:
				record  = Record.objects.get(pk=identifier)	
				_record = RecordSerializer(record)
				properties = defaultdict(list)

				for property in _record.data.get('properties'):
					if not property.get('name') in properties:
						properties[property.get('name')] = list()
					properties[property.get('name')].append(property.get('value'))

				id = _record.data.get('id')

			data = [
				('oai_dc',
				'http://www.openarchives.org/OAI/2.0/oai_dc.xsd',
				'http://www.openarchives.org/OAI/2.0/oai_dc/'
				)
	        ]

			return data

		except Record.DoesNotExist:
			raise IdDoesNotExistError
		
	def listRecords(self, metadataPrefix, set=None, from_=None, until=None):
		"""Get a list of header, metadata and about information on records.
		metadataPrefix - identifies metadata set to retrieve
		set - set identifier; only return records in set (optional)
		from_ - only retrieve records from from_ date forward (optional)
		until - only retrieve records with dates up to and including
				until date (optional)
		Should raise error.CannotDisseminateFormatError if metadataPrefix
		is not supported by the repository.
		Should raise error.NoSetHierarchyError if the repository does not
		support sets.
		Returns an iterable of header, metadata, about tuples.
		"""

		if metadataPrefix != 'oai_dc':
			raise CannotDisseminateFormatError

		if set is not None:
			raise NoSetHierarchyError

		records = Record.objects.filter(repository=self.repository)

		data = []

		for record in records:
			_record = RecordSerializer(record)
			properties = defaultdict(list)

			print 'REPOSITORY =====> ' + str(self.repository.id)

			for property in _record.data.get('properties'):
				if not property.get('name') in properties:
					properties[property.get('name')] = list()
				properties[property.get('name')].append(property.get('value'))

			id = _record.data.get('id')

			data.append((
				Header(id, id, datetime.now(), '', False), 
				Metadata(id, properties),
	            None
	        ))
        
		return data


	def listSets(self):
		"""Get a list of sets in the repository.
		Should raise error.NoSetHierarchyError if the repository does not
		support sets.
		Returns an iterable of setSpec, setName tuples (strings).
		"""

		if set is not None:
			raise NoSetHierarchyError
