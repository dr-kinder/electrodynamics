Classical Electrodynamics
=========================

This is a code repository for a classical electrodynamics course.

If you are taking the course, you should ___fork___ this repository.  You will be able to edit the files in your own fork, but not the files in this repository.

Each week, there will be a new folder with Jupyter notebooks, data sets, and code samples.  Update your fork to bring the new content in each week.  Be sure to commit your work by the due date.

Week 1
------

The files in this directory are

```
week-01/
├── 01-visualizing-fields.ipynb
├── 02-multipoles.ipynb
└── slider-example.ipynb
```

`01-visualizing-fields.ipynb` introduces different plotting tools that can be used to visualize electromagnetic fields and potentials.

`02-multipoles.ipynb` illustrates different field patterns that emerge when multiple point charges are placed nearby.

`slider-example.ipynb` is an example of adding a slider to a plot in a Jupyter notebook, adapted with little modification from Zephyr's answer to a [query at StackOverflow](https://stackoverflow.com/questions/68698587/python-3d-gradient-plot-animation-with-control-slider).



Week 2
------

The files in this directory are

```
week-02
├── 03-vector-calculus.ipynb
├── 04-potentials-and-fields.ipynb
├── Electrodynamics.py
└── VectorCalculus.py
```

`03-vector-calculus.ipynb` provides a visual introduction to the calculus of scalar and vector fields.

`04-potentials-and-fields.ipynb` is a problem that requires the use of the tools developed in `03-vector-calculus.ipynb`.

`Electrodynamics.py` is a module of functions for creating fields and potentials of point charges and plotting these fields.

`VectorCalculus.py` is a collection of functions for carrying out vector calculus operations:
- gradient
- divergence
- curl
- line integrals
- surface integrals
- volume integrals

The functions are designed to be simple to read, use, and modify.
