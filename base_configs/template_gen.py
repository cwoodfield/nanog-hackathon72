#!/usr/bin/env python2.7
 
import os
import sys
from jinja2 import Environment, FileSystemLoader
import yaml
 
TEMPLATE_ENVIRONMENT = Environment(
  autoescape=False,
  loader=FileSystemLoader('./'),
  trim_blocks=False)

def render_template(template_filename, context):
  return TEMPLATE_ENVIRONMENT.get_template(template_filename).render(context)

def generate_template(template_file, data_file):
  with open(data_file) as f:
    try:
      context = yaml.load(f)
      print render_template(template_file, context)
    except yaml.YAMLError as exc:
      print(exc)

def main():
  template_file = sys.argv[1]
  data_file = sys.argv[2]
  generate_template(template_file, data_file)

if __name__ == "__main__":
    main()
