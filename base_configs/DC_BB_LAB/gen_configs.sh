#!/bin/bash

# Generate vEOS configs
for x in leaf spine
do
  for y in YAML/$x*
  do
    cf=eos-$(basename -s .yaml $y).conf
    ../template_gen.py TEMPLATES/${x}_template.j2 $y > CONFIGS/$cf
  done
done

# Then vmx
for y in YAML/vmx*
do
    cf=$(basename -s .yaml $y).conf
    ../template_gen.py TEMPLATES/vmx_template.j2 $y > CONFIGS/$cf
done
