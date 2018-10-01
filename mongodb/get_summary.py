#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ =  'Felipe Fronchetti'
__contact__ = 'fronchetti@usp.br'

import os
import csv
import json
import numpy
import pymongo
import re
from datetime import timedelta
from datetime import datetime
from dateutil.relativedelta import relativedelta
from collections import Counter

class Summary():
	def __init__(self, repository, folder):
		self.folder = folder
		self.domains = {}

		with open('domains.csv', 'r') as file:
			reader = csv.DictReader(file)

			for row in reader:
				self.domains[row['name']] = row['domain']
	
	def create_id(self):
		about_file = json.load(open(self.folder + '/about.json', 'r'))
		name = about_file['name']
		owner = about_file['owner']['login']
		return re.sub('[^a-zA-Z]+', '', name) + '_' + re.sub('[^a-zA-Z]+', '', owner)

		return 
	def get_merged_pulls(self):
		pulls_file = json.load(open(self.folder + '/pull_requests.json', 'r'))
		merged_list = []

		for line in pulls_file:
			if line['merged_at'] != None:
			   merged_list.append(line)
				
		return merged_list

	def get_commits(self):
		contributions_file = open(self.folder + '/commits.txt', 'r')
		contributions_list = []

		about_file = json.load(open(self.folder + '/about.json', 'r'))
		created_at = datetime.strptime(about_file['created_at'], '%Y-%m-%dT%H:%M:%SZ') + relativedelta(months=6)

		for line in contributions_file:
			contribution_date = line.strip()

			if contribution_date:
				contribution_datetime = datetime.strptime(contribution_date, '%Y-%m-%d').date().replace(day=15)

				if contribution_datetime >= created_at.date():
					contributions_list.append(contribution_date)

		return contributions_list

	def get_stars(self):
		stars_file = json.load(open(self.folder + '/stars.json', 'r'))
		stars_list = []

		for line in stars_file:
			star_date = line['starred_at']

			if star_date:
				stars_list.append(star_date)

		return stars_list

	def get_forks(self):
		forks_file = json.load(open(self.folder + '/forks.json', 'r'))
		forks_list = []

		for line in forks_file:
			fork_date = line['created_at']

			if fork_date:
				forks_list.append(fork_date)

		return forks_list

	def get_used_languages(self):
		number_of_used_languages = json.load(open(self.folder + '/languages.json', 'r'))
		return number_of_used_languages

	def has_readme(self):
		if os.path.isfile(self.folder + '/repository/README.MD') or os.path.isfile(self.folder + '/repository/README.md') or os.path.isfile(self.folder + '/repository/README'):
			return True
		else:
			return False

	def has_contributing(self):
		if os.path.isfile(self.folder + '/repository/CONTRIBUTING.MD') or os.path.isfile(self.folder + '/repository/CONTRIBUTING.md') or os.path.isfile(self.folder + '/repository/CONTRIBUTING'):
			return True
		else:
			return False

	def get_domain(self):
		if repository['full_name'] in self.domains.keys():
			domain = self.domains[repository['full_name']]
		else:
			domain = 'Other'
		return domain

	def get_newcomers(self):
		first_commit_file = open(self.folder + '/first_commit.txt', 'r', encoding = 'ISO-8859-1')
		newcomers = []

		about_file = json.load(open(self.folder + '/about.json', 'r'))
		created_at = datetime.strptime(about_file['created_at'], '%Y-%m-%dT%H:%M:%SZ') + relativedelta(months=6)

		for line in first_commit_file:
			entry_date = line.rsplit(',', 1)[1].strip()

			if entry_date:
				entry_datetime = datetime.strptime(entry_date, '%Y-%m-%d').date()

				if entry_datetime >= created_at.date():
					newcomers.append(entry_date)

		return newcomers

	def get_contributors(self):
		first_commit_file = open(self.folder + '/first_commit.txt', 'r', encoding = 'ISO-8859-1')
		contributors = []

		for line in first_commit_file:
			contributor = line.rsplit(',', 1)[0].strip()
			contributors.append(contributor)
		
		return contributors

	def get_license(self):
		about_file = json.load(open(self.folder + '/about.json', 'r'))

		if 'license' in about_file:
			if about_file['license'] != None:
				return about_file['license']['name']
		return 'Other'

	def get_pull_merged_stats(self, pull_merged_total):
		comments = []
		lines_added = []
		lines_deleted = []
		lines_modified = []
		files_modified = []
		core_members = []
		time_for_merge = []
		time_for_first_review = []

		if len(pull_merged_total) > 0:
			for pull_request in pull_merged_total:
				data = {'pull_request': pull_request['_links']['html']['href'], 'comments': None, 'lines_added': None, 'lines_deleted': None, 'lines_modified': None, 'files_modified': None, 'core_members': None, 'time_for_merge': None, 'time_for_first_review': None}
				
				if 'comments' in pull_request:
					data['comments'] = pull_request['comments'] 
					comments.append(pull_request['comments'])
				if 'additions' in pull_request:
					data['lines_added'] = pull_request['additions'] 
					lines_added.append(pull_request['additions'])
				if 'deletions' in pull_request:
					data['lines_deleted'] = pull_request['deletions'] 
					lines_deleted.append(pull_request['deletions'])
				if 'additions' in pull_request and 'deletions' in pull_request:
					data['lines_modified'] = pull_request['additions'] + pull_request['deletions'] 
					lines_modified.append(pull_request['additions'] + pull_request['deletions'])
				if 'changed_files' in pull_request:
					data['files_modified'] = pull_request['changed_files']              
					files_modified.append(pull_request['changed_files'])

				if 'merged_by' in pull_request:
					if pull_request['merged_by'] != None:
						if 'login' in pull_request['merged_by']:
							data['core_members'] = pull_request['merged_by']['login']              
							if pull_request['merged_by']['login'] not in core_members:
								core_members.append(pull_request['merged_by']['login'])

				time_for_merge.append(abs(datetime.strptime(pull_request['merged_at'], '%Y-%m-%dT%H:%M:%SZ').date() - datetime.strptime(pull_request['created_at'], '%Y-%m-%dT%H:%M:%SZ').date()).days)
				data['time_for_merge'] = abs(datetime.strptime(pull_request['merged_at'], '%Y-%m-%dT%H:%M:%SZ').date() - datetime.strptime(pull_request['created_at'], '%Y-%m-%dT%H:%M:%SZ').date()).days

				if 'review_comments_list' in pull_request:
					if pull_request['review_comments_list'] != None:
						if len(pull_request['review_comments_list']) > 0:
							data['time_for_first_review'] = abs(datetime.strptime(pull_request['review_comments_list'][0]['created_at'], '%Y-%m-%dT%H:%M:%SZ').date() - datetime.strptime(pull_request['created_at'], '%Y-%m-%dT%H:%M:%SZ').date()).days
							time_for_first_review.append(abs(datetime.strptime(pull_request['review_comments_list'][0]['created_at'], '%Y-%m-%dT%H:%M:%SZ').date() - datetime.strptime(pull_request['created_at'], '%Y-%m-%dT%H:%M:%SZ').date()).days)
		else:
			comments = [0]
			lines_added = [0]
			lines_deleted = [0]
			lines_modified = [0]
			files_modified = [0]
			core_members = [0]
			time_for_merge = [0]
			time_for_first_review = [0]

		return {'comments': comments, 'lines_added': lines_added, 'lines_deleted': lines_deleted, 'lines_modified': lines_modified, 'files_modified': lines_modified, 'core_members': core_members, 'merge_time': time_for_merge, 'first_review_time': time_for_first_review}

client = pymongo.MongoClient('mongodb://localhost:27017/')
database = client.openuniverse
database.projects.drop()
projects = database.projects

if __name__ == '__main__':
	if os.path.isfile('projects.json'):
		with open('projects.json', 'r') as file:
			dictionary = json.load(file)

	for language in dictionary.keys():
		repositories = dictionary[language]['items']

		for repository in repositories:
			if repository['name'] != 'linux':
				dataset_folder = 'Dataset' + '/' + language + '/' + repository['name']
				project = Summary(repository, dataset_folder)

				pull_merged_total = project.get_merged_pulls()
				pull_merged_stats = project.get_pull_merged_stats(pull_merged_total)
				commit_total = project.get_commits()
				star_total = project.get_stars()
				fork_total = project.get_forks()
				open_issues = repository['open_issues_count']
				used_languages = project.get_used_languages()
				owner_type = repository['owner']['type']
				main_language = repository['language']
				age = 2018 - int(datetime.strptime(repository['created_at'], '%Y-%m-%dT%H:%M:%SZ').date().year)
				domain = project.get_domain()
				license = project.get_license()
				newcomers = project.get_newcomers()
				contributors = project.get_contributors()
				comments = pull_merged_stats['comments']
				lines_added = pull_merged_stats['lines_added']
				lines_deleted = pull_merged_stats['lines_deleted']
				lines_modified = pull_merged_stats['lines_modified']
				files_modified = pull_merged_stats['files_modified']
				core_members = pull_merged_stats['core_members']
				time_for_merge = pull_merged_stats['merge_time']
				time_for_first_review = pull_merged_stats['first_review_time']

				has_contributing = project.has_contributing()
				has_readme = project.has_readme()
				has_wiki = repository['has_wiki']
				has_issue_tracker = repository['has_issues']

				data = {'project_id': project.create_id(),
						'name': repository['name'],
						'owner': repository['owner']['login'],
						'owner_type': owner_type,
						'domain': domain,
						'license': license,
						'age': age,
						'main_language': main_language,
						'github_url': repository['html_url'],
						'statistics': {'pulls_merged_total': len(numpy.nan_to_num(pull_merged_total)),
									   'newcomers_total': len(numpy.nan_to_num(newcomers)),
									   'open_issues_total': open_issues,
									   'used_languages_total': len(used_languages),
									   'forks_total': len(numpy.nan_to_num(fork_total)),
									   'stars_total': len(numpy.nan_to_num(star_total)),
									   'commits_total': len(numpy.nan_to_num(commit_total)),
									   'contributors_total': len(contributors),
									   'core_members_total': len(core_members),
									   'comments_median': int(numpy.nan_to_num(numpy.median(comments))),
									   'lines_modified_median': int(numpy.nan_to_num(numpy.median(lines_modified))),
									   'files_modified_median': int(numpy.nan_to_num(numpy.median(files_modified))),
									   'time_for_merge_median': int(numpy.nan_to_num(numpy.median(time_for_merge))),
									   'time_for_first_review_median': int(numpy.nan_to_num(numpy.median(time_for_first_review)))
									   },
						'time_series': {'newcomers_ts': Counter(newcomers),
										'pulls_merged_ts': Counter([pull_request['merged_at'] for pull_request in pull_merged_total]),
										'forks_ts': Counter(fork_total),
										'stars_ts': Counter(star_total),
										'commits_ts': Counter(commit_total)
										},
						'features': {'has_contributing': has_contributing,
									 'has_readme': has_readme,
									 'has_wiki': has_wiki,
									 'has_issue_tracker': has_issue_tracker
									}
						}

				projects.insert_one(data)
