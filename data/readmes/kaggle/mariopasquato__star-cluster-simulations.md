# Star Cluster Simulations

Direct N-body simulation of a star cluster: Position and velocities of stars

# Context 

Stars mostly form in clusters and associations rather than in isolation. Milky Way star clusters are easily observable with small telescopes, and in some cases even with the naked eye. Depending on a variety of conditions, star clusters may dissolve quickly or be very long lived.
The dynamical evolution of star clusters is a topic of very active research in astrophysics. Some popular models of star clusters are the so-called direct N-body simulations [1, 2], where every star is represented by a point particle that interacts gravitationally with every other particle. This kind of simulation is computationally expensive, as it scales as O(N^2) where N is the number of particles in the simulated cluster. In the following, the words "particle" and "star" are used interchangeably.

# Content

This dataset contains the positions and velocities of simulated stars (particles) in a direct N-body simulation of a star cluster. In the cluster there are initially 64000 stars distributed in position-velocity space according to a King model [3]. Each .csv file named c_xxxx.csv corresponds to a snapshot of the simulation at time t = xxxx. For example, c_0000.csv contains the initial conditions (positions and velocities of stars at time t=0). Times are measured in standard N-body units [4]. This is a system of units where G = M = −4E = 1 (G is the gravitational constant, M the total mass of the cluster, and E its total energy).

**x, y, z**
Columns 1, 2, and 3 of each file are the x, y, z positions of the stars. They are also expressed in standard N-body units [4]. You can switch to units of the median radius of the cluster by finding the cluster center and calculating the median distance of stars from it, and then dividing x, y, and z by this number. In general, the median radius changes in time. The initial conditions are approximately spherically symmetric (you can check) so there is no particular physical meaning attached to the choice of x, y, and z. 

**vx, vy, vz**
Columns 4, 5, and 6 contain the x, y, and z velocity, also in N-body units. A scale velocity for the stars can be obtained by taking the standard deviation of velocity along one direction (e.g. z). You may check that the ratio between the typical radius (see above) and the typical velocity is of order unity.

**m**
Column 7 is the mass of each star. For this simulation this is identically 1.5625e-05, i.e. 1/64000. The total mass of the cluster is initially 1. More realistic simulations (coming soon) have a spectrum of different masses and live stelar evolution, that results in changes in the mass of stars. This simulation is a pure N-body problem instead.

**Star id number**
The id numbers of each particle are listed in the last column (8) of the files under the header "id". The ids are unique and can be used to trace the position and velocity of a star across all files. There are initially 64000 particles. At end of the simulation there are 63970. This is because some particles escape the cluster.

# Acknowledgements

This simulation was run on a Center for Galaxy Evolution Research (CGER) workstation at Yonsei University (Seoul, Korea), using the NBODY6 software (https://www.ast.cam.ac.uk/~sverre/web/pages/nbody.htm).


# Inspiration

Some stars hover around the center of the cluster, while some other get kicked out to the cluster outskirts or even leave the cluster altogether. Can we predict where a star will be at any given time based on its initial position and velocity? Can we predict its velocity?

How correlated are the motions of stars? Can we predict the velocity of a given star based on the velocity of its neighbours?

The size of the cluster can be measured by defining a center (see below) and finding the median distance of stars from it. This is called the three-dimensional effective radius. Can we predict how it evolves over time? What are its properties as a time series? What can we say about other quantiles of the radius?

How to define the cluster center? Just as the mode of a KDE of the distribution of stars? How does it move over time and how to quantify the properties of its fluctuations? Is the cluster symmetric around this center?

Some stars leave the cluster: over time they exchange energy in close encounters with other stars and reach the escape velocity. This can be seen by comparing later snapshots with the initial one: some IDs are missing and there is overall a lower number of stars. Can we predict which stars are more likely to escape? When will a given star escape?

# References
[1] Heggie, D., Hut, P. 2003, The Gravitational Million-Body Problem: A Multidisciplinary Approach to Star Cluster Dynamics ~ Cambridge University Press, 2003

[2] Aarseth, S.~J. 2003, Gravitational N-Body Simulations - Cambridge University Press, 2003

[3] King, I. 1966, AJ, 71, 64

[4] Heggie, D. C., Mathieu, R. D. 1986, Lecture Notes in Physics, Vol. 267, The Use of Supercomputers in Stellar Dynamics, Berlin, Springer

출처: Kaggle (mariopasquato/star-cluster-simulations)
태그: earth and nature, astronomy, physics
라이선스: CC0: Public Domain
수정일: 2017-01-07T06:59:40.707Z
