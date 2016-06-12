#!/usr/bin/env python
import os
import sys
import json

def show_help():
	print 'see docs in README.md'
	sys.exit( 0 )

verbose = '-v' in sys.argv
if '--help' in sys.argv:
	show_help()

def error(msg):
	sys.stderr.write(msg + '\n')
	sys.exit( -1 )

CONFIG_FILE = 'grouper.json'
cur_dir = os.getcwd()
json_file = os.path.join(cur_dir, CONFIG_FILE)

def get_file_content(path):
	fileio = open( path )
	content = fileio.read()
	fileio.close()
	return content

def save_to_file(content, path):
	fileio = open(path, 'w')
	fileio.write( content )
	fileio.close()

def generate_files( config_dict ):
	print 'building'
	_content_dict = {}
	for key in config_dict.keys():
		if key != 'outputs':
			if not _content_dict.has_key(key):
				_content_dict[ key ] = ''
			for file_name in config_dict[ key ]:
				print key + '+', file_name
				_path = os.path.join(cur_dir, file_name)
				if not os.path.isfile( _path ):
					error('Error: file %s not found' % (file_name))
				_content_dict[ key ] += get_file_content( _path )
	for i in config_dict['outputs']:
		if type(i) is dict:
			template_path = os.path.join(cur_dir, i.keys()[ 0 ] )
			output_path = os.path.join(cur_dir, i[ i.keys()[0] ] )
			final_content = get_file_content(template_path) % _content_dict
			save_to_file(final_content, output_path)
		else:
			error('Wrong "outputs" key')

def build():
	config = None
	try:
		config = json.loads( get_file_content( CONFIG_FILE ) )
	except ValueError, e:
		error('grouper.js in wrong format ' + e)
	if not config.has_key('outputs'):
		error('You must set the "outputs" key in grouper.json')
	generate_files( config )

if os.path.isfile( json_file ):
	build()
else:
	error('You must create a grouper.json file')