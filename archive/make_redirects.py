"""generate the redirect collection from tumblr_archive.json"""

import json
import os

orig_domain = 'http://monthlymusichackathon.org'

def make_frontmatter(permalink):
	return """---
permalink: '{0}'
layout: redirect
---
""".format(permalink)

with open('tumblr_archive.json') as data_file:    
	data = json.load(data_file)
	posts = data['response']['posts']
	for post in posts:
		permalink = post['post_url'].split(orig_domain)[1]
		txt = make_frontmatter(permalink)
		f = open( '../_redirects/{0}.md'.format(str(post['id'])), 'w+')
		f.write(txt)
		f.close()
