microfluidic-cad
================

Currently just some tests of different CAD tools

## ImplicitCAD usage
`extopenscad -o test.stl implicitCAD/tobacco_mesophyll_protoplast_fusion_device.escad -r 1`
where:
* `extopenscad`
  * is the ImplicitCAD program that parses "extended" OpenSCAD syntax... see [OpenSCAD syntax](https://www.openscad.org/cheatsheet/) docs for complex examples
* `-o test.stl`
  * the output file ImplicitCAD will produce
* `implicitCAD/tobacco_mesophyll_protoplast_fusion_device.escad`
  * the path to the input CAD script, writted in ESCAD syntax
* `-r 1`
  * the 'resolution' argument, a lower number means more resolution in the output file