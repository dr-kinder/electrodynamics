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


Week 3
------

The files in this directory are

```
week-03/
├── 05-equations-of-motion.ipynb
└── 06-finite-element-method.ipynb
```

`05-equations-of-motion.ipynb` introduces methods for solving ordinary differential equations and computing the trajectories of charged particles using the Lorentz force law.

`06-finite-element-method.ipynb` illustrates the use of [Gmsh](https://gmsh.info/), [FEniCSx](https://fenicsproject.org/), and [Multiphenicsx](https://github.com/multiphenics/multiphenicsx) to solve a problem in electrostatics via finite element analysis.  This notebook was written to run in CoLab.  It will install these three packages and dependencies within a CoLab session using the protocol described at [FEM on CoLab](https://fem-on-colab.github.io/index.html). It can be run in other Jupyter notebook environments, but the packages should be installed locally first.

Notebook #6 was adapted from ["Solving the Poisson Equation"](https://jorgensd.github.io/dolfinx-tutorial/chapter1/fundamentals.html) in the FEniCSx tutorial.  Portions of the code (plotting and mesh generation) were also adapted from the [Multiphenicsx tutorials](https://github.com/multiphenics/multiphenicsx/tree/main/tutorials).


Week 4
------

The files in this directory are

```
week-04/
├── 07-laplace-equation.ipynb
└── 08-magnetic-fields.ipynb
```

Both notebooks illustrates the use of [Gmsh](https://gmsh.info/), [FEniCSx](https://fenicsproject.org/), and [Multiphenicsx](https://github.com/multiphenics/multiphenicsx) to solve problems in electrostatics and magnetostatics via finite element analysis.  The notebook are written to run in CoLab.  They will install these three packages and dependencies within a CoLab session using the protocol described at [FEM on CoLab](https://fem-on-colab.github.io/index.html). The notebooks can be run in other Jupyter notebook environments, but the packages should be installed locally first.

`07-laplace-equation.ipynb` explores the effects of boundary conditions on the solution of Laplace's equation for a rectangular domain.

`08-magnetic-fields.ipynb` explores the vector potential and magnetic fields in a coaxial cable with an iron ring.

Notebook #8 was adapted from ["Electromagnetics example"](https://jorgensd.github.io/dolfinx-tutorial/chapter3/em.html#electromagnetics-example).
