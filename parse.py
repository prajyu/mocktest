import xml.etree.ElementTree as ET
import html

# Input questions and answers as a list of tuples (question_text, options, correct_option)
questions1_answers = [
      (r"If \(n\) cells each of emf \(E\) are connected in parallel, the emf of the combination is", ["$$\\frac{E}{n}$$", "$$\\frac{n}{E}$$", "$$n\\times nE$$", "$$E$$", "$$\\frac{n}{E}$$"], "D"),
    (r"A boat having a length of 3 m and breadth 2 m is floating on a lake. The boat Sinks by one cm when a material is put on it. The mass of material is", ["$$30$$kg", "$$600$$kg", "$$60$$kg", "$$540$$kg", "$$120$$kg"], "C"),
    (r"If two soap bubbles of radii \(r_1\) and \(r_2\) (\(r_2 > r_1\)) are in contact, the radius of their common interface is", ["$$r_1+r_2$$", "$$(r_1+r_2)^2$$", "$$\\frac{r_1 r_2}{r_2-r_1}$$", "$$\\sqrt{r_1r_2}$$", "$$(r_1-r_2)^2$$"], "C"),
    (r"A body weight 4N in air and 3N when immersed in a liquid. The buoyant force on the body is", ["$$1$$N", "$$2$$N", "$$3$$N", "$$4$$N", "$$5$$N"], "A"),
    (r"What will be the phase difference between virtual voltage and virtual current, when the current in the circuit is wattless?", ["$$90$$°", "$$45$$°", "$$180$$°", "$$60$$°", "$$270$$°"], "A"),
    (r"The expression for the distance travelled during the nth second is:", ["$$S=un+\\frac{1}{2}an^2$$", "$$S=u+\\frac{1}{2}an^2$$", "$$S=u+\\frac{1}{2}(2n+1)$$", "$$S=u+\\frac{1}{2}(2n-1)$$", "none of these"], "A"),
    (r"If the error in the measurement of radius of a sphere is 1%, the error in the measurement of volume is:", ["1%", "3%", "6%", "9/4", "5/4"], "B"),
    (r"An electron and a Proton are moving in the same direction with the same kinetic energy. The ratio of the de Broglie wavelength associated with these particles.", ["$$m_e/m_p$$", "$$m_p/m_e$$", "$$m_e\\times m_p$$", "$$\\sqrt{m_e/m_p}$$", "$$\\sqrt{m_p/m_e}$$"], "E"),
    (r"The Fahrenheit and Kelvin scales in temperature will give same reading at:", ["-40", "313", "574.25", "732.75", "273"], "A"),
    (r"Work function of a metal is 4ev. The wavelength of incident radiation required just to emit the electrons from the surface is", ["2700 Angstrom", "1700 Angstrom", "5900 Angstrom", "3100 Angstrom", "2500 Angstrom"], "C"),
     (r"The expression for the distance travelled during the nth second is:", ["$$S=un+\\frac{1}{2}an^2$$", "$$S=u+\\frac{1}{2}an^2$$", "$$S=u+\\frac{1}{2}(2n+1)$$", "$$S=u+\\frac{1}{2}(2n-1)$$", "none of these"], "A"),
    (r"If the error in the measurement of radius of a sphere is 1%, the error in the measurement of volume is:", ["1%", "3%", "6%", "9/4", "5/4"], "B"),
    (r"An electron and a Proton are moving in the same direction with the same kinetic energy. The ratio of the de Broglie wavelength associated with these particles.", ["$$m_e/m_p$$", "$$m_p/m_e$$", "$$m_e\\times m_p$$", "$$\\sqrt{m_e/m_p}$$", "$$\\sqrt{m_p/m_e}$$"], "E"),
    (r"The Fahrenheit and Kelvin scales in temperature will give same reading at:", ["-40", "313", "574.25", "732.75", "273"], "A"),
    (r"Work function of a metal is 4ev. The wavelength of incident radiation required just to emit the electrons from the surface is", ["2700 Angstrom", "1700 Angstrom", "5900 Angstrom", "3100 Angstrom", "2500 Angstrom"], "C"),
    
       (r"What is the dimensional formula of torque and energy?", [r"$$[ML^2T^{-2}]$$ and $$[MLT^{-2}]$$", r"$$[ML^3T^{-2}]$$ and $$[MLT^{-2}]$$", r"$$[ML^2T^{-2}]$$ and $$[ML^2T^2]$$", r"$$[MLT^2]$$ and $$[ML^2T^2]$$"], "A"),
    (r"Let there be two bodies, each weighing 2 kg and the other 5 kg. Allow the same force to be applied to these bodies as they are at rest. Determine the ratio of the time each body must travel before reaching the final velocity.", ["5:3", "2:5", "4:25", "25:4"], "A"),
    (r"A body's natural ability to resist changes in its state of motion is referred to as ___?", ["Momentum", "Acceleration", "Force", "Inertia"], "D"),
    (r"Two projectiles \(P\) and \(Q\) thrown with velocities \(v\) and \(v/2\) respectively have the same range. If \(Q\) is thrown at an angle of 15° to the horizontal, \(P\) must be thrown at an angle of", ["30°", r"$$\frac{1}{2} \sin^{-1}(1/8)$$", r"$$\frac{1}{4} \sin^{-1}(1/2)$$", "60°"], "D"),
    (r"The height at which the acceleration due to gravity becomes \(g/9\) (where \(g =\) the acceleration due to gravity on the surface of the earth) in terms of \(R\), the radius of the earth, is", [r"$$R/2$$", r"$$R/3$$", r"$$2R$$", r"$$3R$$"], "B"),
    (r"What is the relationship between the number of nodes and antinodes between the ends of a vibrating wire in its second overtone?", [r"2 nodes and 2 antinodes", r"1 node and 2 antinodes", r"4 nodes and 3 antinodes", r"2 nodes and 3 antinodes", r"3 nodes and 4 antinodes"], "A"),
    (r"A resistor has a color code of green, blue, brown, and silver. What is its resistance?", [r"56 ohm ±5%", r"560 ohm ±10%", r"560 ohm ±5%", r"5600 ohm ±10%", r"56000 ohm ±10%"], "C"),
    (r"What is the angular momentum of Earth around the Sun proportional to, if the distance between the Sun and Earth is \(d\)?", [r"\(vd\)", r"\(d^2\)", r"\(d^{1/3}\)", r"\(d\)", r"\(d^{3/2}\)"], "E"),
    (r"Calculate the magnetic dipole moment of a magnetic dipole using the formula:", [r"\(M = m \times 2I\)", r"\(M = m + 2I\)", r"\(M = m - 2I\)", r"\(M = \frac{m}{2I}\)"], "A"),
    (r"A car is moving with an initial speed of 5 m/s. A constant braking force is applied, and the car is brought to rest in a distance of 10 m. What is the average speed of the car during the deceleration process?", [r"1 m/s", r"2.5 m/s", r"4 m/s", r"5 m/s"], "B"),
      (r"Two thin convex lenses \(L_1\) and \(L_2\) have focal lengths 4 cm and 10 cm, respectively. They are separated by a distance \(x\) cm as shown in the figure. A point source \(S\) is placed on the principal axis at a distance 12 cm to the left of \(L_1\). If the image of \(S\) is formed at infinity, the value of \(x\) is:", [r"6", r"16", r"14", r"24"], "A"),
    (r"A current-carrying long solenoid is formed by winding 200 turns per cm. If the number of turns per cm is increased to 201 while keeping the current constant, then the magnetic field inside the solenoid will change by:", [r"0.2%", r"0.40%", r"0.50%", r"1%"], "A"),
    (r"A series LCR circuit consists of a variable capacitor connected to an inductor of inductance 50 mH, a resistor of resistance 100 Ω, and an AC source of angular frequency 500 rad/s. The value of capacitance so that the maximum current may be drawn into the circuit is:", [r"60 µF", r"50 µF", r"100 µF", r"80 µF"], "A"),
    (r"Consider telecommunication through optical fibers. Which of the following statements is not true?", [r"Optical fibers can be of graded refractive index", r"Optical fibers are subject to electromagnetic interference from outside", r"Optical fibers have extremely low transmission loss", r"Optical fibers may have a homogeneous core with a suitable cladding"], "B"),
    (r"If the distance traveled by a particle in time \(t\) is represented by \(x = 2 \cos at - \sin (2a - 1) t(a - 1)\) and if the motion is simple harmonic motion then \(a\) is:", [r"?", r"1/4", r"1/2", r"√3 + 1"], "C"),
      (r"A solid sphere of radius \(r\) is revolving about one of its diameters with an angular velocity \(\omega\). If it suddenly expands uniformly so that its radius increases to \(n\) times its original value, then its angular velocity becomes:", [r"\(n^2\omega\)", r"\(\frac{\omega}{n^2}\)", r"\(\omega n\)", r"\(\frac{\omega}{n}\)", r"\(2n\omega\)"], "A"),
    (r"If a ring rolls down from top to bottom of an inclined plane, it takes time \(t_1\). If it slides, it takes time \(t_2\). Then the ratio \(\left(\frac{t_2}{t_1}\right)^2\) is:", [r"\(\frac{1}{3}\)", r"\(\frac{2}{3}\)", r"\(\frac{1}{4}\)", r"\(\frac{1}{2}\)", r"\(\frac{2}{5}\)"], "B"),
    (r"If the distance between the Sun and Earth is \(d\), then the angular momentum of Earth around the Sun is proportional to:", [r"\(vd\)", r"\(d^2\)", r"\(d^{1/3}\)", r"\(d\)", r"\(d^{3/2}\)"], "E"),
    (r"The net gravitational force at the midpoint of the line joining the centers of two identical objects, each of mass \(50 \, \text{kg}\), kept at a distance of \(50 \, \text{cm}\) apart on a horizontal table is:", [r"zero", r"\(6.6733 \times 10^{-9} \, \text{N}\)", r"\(13.346 \times 10^{-9} \, \text{N}\)", r"\(3.336 \times 10^{-9} \, \text{N}\)", r"\(6.673 \times 10^6 \, \text{N}\)"], "A"),
    (r"The ratio of the weight of a body at a height of \(\frac{R}{10}\) from the surface of the earth to that at a depth \(\binom{R}{10}\) is (where \(R\) is the radius of the earth):", [r"4:5", r"1:1", r"9:8", r"8:9"], "A"),
       (r"The electric flux (in SI units) through any face of a cube due to a positive charge \(Q\) situated at the center of the cube is:", [r"\(\frac{Q}{4\pi\epsilon_0}\)", r"\(4\pi\epsilon_0 Q\)", r"\(\frac{Q}{6\epsilon_0}\)", r"\(\frac{Q}{6\pi\epsilon_0}\)", r"\(6\pi\epsilon_0 Q\)"], "A"),
    (r"A capacitance of a parallel plate air capacitor is \(10 \, \mu F\). The dielectric constant of the medium to be introduced between its plates to double its capacitance is:", [r"2", r"3", r"4", r"2.5", r"1.5"], "A"),
    (r"The electric potential \(V\) at any point \((x, y, z)\) in space is given by \(V = 4x^2\) volt, where \(x\), \(y\), \(z\) are all in meters. The electric field at that point \((1m, 0, 2m)\) in \(V/m\) is:", [r"16 \, \text{along the positive x axis}", r"16 \, \text{along the negative x axis}", r"4 \, \text{along the positive x axis}", r"8 \, \text{along the negative x axis}"], "A"),
    (r"The work done in moving a point charge of \(10 \, \mu C\) through a distance of \(3 \, cm\) along the equatorial axis of an electric dipole is:", [r"\(10 \times 10^{-6} \, J\)", r"0", r"\(20 \times 10^{-6} \, J\)", r"\(5 \times 10^{-6} \, J\)"], "A"),
    (r"If a monoatomic gas is compressed adiabatically to \(\frac{1}{27}\)th of its initial volume, then its pressure becomes:", [r"27 \, \text{times}", r"125 \, \text{times}", r"243 \, \text{times}", r"81 \, \text{times}", r"64 \, \text{times}"], "A"),
     (r"The values of \(C_p\) and \(C_v\), for a diatomic gas are respectively (where \(R\) is the gas constant):", [r"\(\frac{7}{2} R\), \(\frac{5}{2} R\)", r"\(\frac{3}{2} R\), \(\frac{5}{2} R\)", r"\(3R\), \(4R\)", r"\(\frac{5}{2} R\), \(\frac{3}{2} R\)"], "A"),
    (r"Three moles of an ideal gas are in a rigid cubical box with sides of length \(0.170 \, m\). The ratio of the forces that the gas exerts on each of the six sides of the box when the gas temperature is \(27°C\) and \(127°C\) is:", [r"6:1", r"1:2", r"3:1", r"3:4", r"1:3"], "A"),
    (r"The average kinetic energy of a monoatomic gas molecule kept at temperature \(27^\circ C\) is:", [r"5.85 \times 10^{-21} \, J", r"4.12 \times 10^{-21} \, J", r"3.75 \times 10^{-21} \, J", r"2.85 \times 10^{-21} \, J", r"7.55 \times 10^{-21} \, J"], "A"),
    (r"A particle is moved in a semicircular path of radius \(R\). Then:", [r"its average velocity is zero", r"its average acceleration is zero", r"its magnitude of displacement is \(2R\)", r"its average velocity and average speed are equal", r"its distance travelled is equal to displacement"], "B"),
    (r"Two projectiles \(P\) and \(Q\) thrown with velocities \(v\) and \(v/2\) respectively have the same range. If \(Q\) is thrown at an angle of \(15°\) to the horizontal, \(P\) must be thrown at an angle of:", [r"45°", r"\(\frac{1}{2} \sin^{-1}\left(\frac{1}{8}\right)\)", r"\(\frac{1}{4} \sin^{-1}\left(\frac{1}{2}\right)\)", r"60°"], "A"),
   (r"An object is thrown vertically with a velocity \(v\). The velocity with which it strikes the ground on its return is:", [r"\(\frac{v}{2}\)", r"\(-\frac{v}{2}\)", r"\(-v\)", r"\(v\)", r"\(2v\)"], "D"),
    (r"Pick out the correct statement:", [r"Second law of motion is a vector equation.", r"Second law of motion is applicable to a particle and not to the system of particles.", r"Force is always in the direction of motion.", r"If external force on a body is zero, it does not mean the acceleration is zero.", r"Acceleration at an instant depends on the history of the motion of the particle."], "D"),
    (r"The ratio of the concentration of electrons to that of holes in a semiconductor is \(\frac{7}{5}\) and the ratio of the currents is \(\frac{7}{4}\). Then what is the ratio of their drift velocities:", [r"\(\frac{4}{7}\)", r"\(\frac{5}{8}\)", r"\(\frac{4}{5}\)", r"\(\frac{5}{4}\)", r"\(\frac{1}{2}\)"], "A")







  ]

questions_answers = [ (
        r"If \( n \) cells each of emf \( E \) are connected in parallel, the emf of the combination is",
        [
            r"A. \( \frac{E}{n} \)",
            r"B. \( \frac{n}{E} \)",
            r"C. \( n \times nE \)",
            r"D. \( E \)",
            r"E. \( \frac{n}{E} \)"
        ],
        "D"
    ),
    (
        r"A boat having a length of 3 m and breadth 2 m is floating on a lake. The boat sinks by one cm when a material is put on it. The mass of the material is",
        [
            r"A. 30 kg",
            r"B. 600 kg",
            r"C. 60 kg",
            r"D. 540 kg",
            r"E. 120 kg"
        ],
        "C"
    ),
    (
        r"If two soap bubbles of radii \( r_1 \) and \( r_2 \) (\( r_2 > r_1 \)) are in contact, the radius of their common interface is",
        [
            r"A. \( r_1 + r_2 \)",
            r"B. \( (r_1 + r_2)^2 \)",
            r"C. \( \frac{r_1 r_2}{r_2 - r_1} \)",
            r"D. \( \sqrt{r_1 r_2} \)",
            r"E. \( (r_1 - r_2)^2 \)"
        ],
        "C"
    ),
    (
        r"A body weighs 4 N in air and 3 N when immersed in a liquid. The buoyant force on the body is",
        [
            r"A. 1 N",
            r"B. 2 N",
            r"C. 3 N",
            r"D. 4 N",
            r"E. 5 N"
        ],
        "D"
    ),
    (
        r"What will be the phase difference between virtual voltage and virtual current when the current in the circuit is wattless?",
        [
            r"A. 90 degrees",
            r"B. 45 degrees",
            r"C. 180 degrees",
            r"D. 60 degrees",
            r"E. 270 degrees"
        ],
        "A"
    ),
       (
        r"The expression for the distance travelled during the \( n \)th second is:",
        [
            r"A. \( S = \frac{un + \frac{1}{2} a n^2}{2} \)",
            r"B. \( S = u + \frac{a}{2} n^2 \)",
            r"C. \( S = u + \frac{a}{2} (2n + 1) \)",
            r"D. \( S = u + \frac{a}{2} (2n - 1) \)",
            r"E. None of these"
        ],
        "D"
    ),
    (
        r"If the error in the measurement of radius of a sphere is 1%, the error in the measurement of volume is:",
        [
            r"A. 1%",
            r"B. 3%",
            r"C. 6%",
            r"D. \(\frac{9}{4}\)",
            r"E. \(\frac{5}{4}\)"
        ],
        "B"
    ),
    (
        r"An electron and a proton are moving in the same direction with the same kinetic energy. The ratio of the de Broglie wavelength associated with these particles is:",
        [
            r"A. \(\frac{m_e}{m_p}\)",
            r"B. \(\frac{m_p}{m_e}\)",
            r"C. \(m_e \times m_p\)",
            r"D. \(\sqrt{\frac{m_e}{m_p}}\)",
            r"E. \(\sqrt{\frac{m_p}{m_e}}\)"
        ],
        "E"
    ),
    (
        r"The Fahrenheit and Kelvin scales in temperature will give the same reading at:",
        [
            r"A. -40",
            r"B. 313",
            r"C. 574.25",
            r"D. 732.75",
            r"E. 273"
        ],
        "C"
    ),
    (
        r"Work function of a metal is 4 eV. The wavelength of incident radiation required just to emit the electrons from the surface is:",
        [
            r"A. 2700 Angstrom",
            r"B. 1700 Angstrom",
            r"C. 5900 Angstrom",
            r"D. 3100 Angstrom",
            r"E. 2500 Angstrom"
        ],
        "D"
    ),
      (
        r"If the radius of Earth's orbit is made \( \frac{1}{9} \)th, then the duration of a year will become:",
        [
            r"A. 27 times",
            r"B. 21 times",
            r"C. \( \frac{1}{27} \) times",
            r"D. 16 times",
            r"E. \( \frac{1}{16} \) times"
        ],
        "C"
    ),
    (
        r"A square plate of side \( l \) has mass \( m \). What is its moment of inertia about one of its diagonals?",
        [
            r"A. \( \frac{ml \times l}{6} \)",
            r"B. \( \frac{ml \times l}{12} \)",
            r"C. \( \frac{ml \times l}{3} \)",
            r"D. \( \frac{ml \times l}{4} \)",
            r"E. \( \frac{ml \times l}{5} \)"
        ],
        "B"
    ),
    (
        r"The magnitude of the electric field intensity at the distance \( x \) from a charge \( q \) is \( E \). An identical charge is placed at a distance \( 2x \) from it. Then the magnitude of the force it experiences is:",
        [
            r"A. \( qE \)",
            r"B. \( \frac{qE}{2} \)",
            r"C. \( \frac{qE}{4} \)",
            r"D. \( 2qE \)",
            r"E. \( \frac{qE}{3} \)"
        ],
        "C"
    ),
    (
        r"If a stretched wire is vibrating in the second overtone, then the number of nodes and antinodes between the ends of the string are respectively:",
        [
            r"A. 2 & 2",
            r"B. 1 & 2",
            r"C. 4 & 3",
            r"D. 2 & 3",
            r"E. 3 & 4"
        ],
        "C"
    ),
    (
        r"A resistor has a color code of green, blue, brown, and silver. What is its resistance?",
        [
            r"A. \( 56 \Omega \pm 5\% \)",
            r"B. \( 560 \Omega \pm 10\% \)",
            r"C. \( 560 \Omega \pm 5\% \)",
            r"D. \( 5600 \Omega \pm 10\% \)",
            r"E. \( 56000 \Omega \pm 10\% \)"
        ],
        "B"
    ),
     (
        r"What is the dimensional formula of torque and energy?",
        [
            r"(a) [ML^-2T^-2] and [ML^2T^-2]",
            r"(b) [ML^2T^-2] and [MLT^-2]",
            r"(c) [ML^2T^-2] and [ML^2T^2]",
            r"(d) [MLT^2] and [ML^2T^2]"
        ],
        "C"
    ),
    (
        r"Let there be two bodies, each weighing 2 kg and the other 5 kg. Allow the same force to be applied to these bodies as they are at rest. Determine the ratio of the time each body must travel before reaching the final velocity.",
        [
            r"(a) 5:3",
            r"(b) 2:5",
            r"(c) 4:25",
            r"(d) 25:4"
        ],
        "B"
    ),
    (
        r"A body's natural ability to resist changes in its state of motion is referred to as ___",
        [
            r"(a) Momentum",
            r"(b) Acceleration",
            r"(c) Force",
            r"(d) Inertia"
        ],
        "D"
    ),
    (
        r"Two projectiles P and Q thrown with velocities v and \( \frac{v}{\sqrt{2}} \) respectively have the same range. If Q is thrown at an angle of 15° to the horizontal, P must be thrown at an angle of",
        [
            r"(a) 30°",
            r"(b) \( \frac{1}{2} \sin^{-1}(1) \)",
            r"(c) \( \frac{1}{4} \sin^{-1}\left(\frac{1}{2}\right) \)",
            r"(d) 60°"
        ],
        "B"
    ),
    (
        r"The height at which the acceleration due to gravity becomes \( \frac{g}{9} \) (where \( g \) is the acceleration due to gravity on the surface of the earth) in terms of \( R \), the radius of the earth, is",
        [
            r"(a) \( \frac{R}{2} \)",
            r"(b) \( \frac{R}{3} \)",
            r"(c) \( 2R \)",
            r"(d) \( 3R \)"
        ],
        "C"
    ),
     (
        r"A 4 kg object is lifted vertically with a force of 50 N. If the object is lifted 5 meters, how much work is done?",
        [
            r"200 J",
            r"250 J",
            r"300 J",
            r"400 J"
        ],
        "B"
    ),
    (
        r"What happens to the modulus of elasticity if the temperature increases?",
        [
            r"(a) Remains constant",
            r"(b) Increases",
            r"(c) Decreases",
            r"(d) Becomes zero"
        ],
        "C"
    ),
    (
        r"Calculate the de Broglie wavelength of an electron moving with a velocity of \(10^6 \, \text{m/s}\).",
        [
            r"(a) \(7.28 \times 10^{-10}\)",
            r"(b) \(2.35 \times 10^{-7}\)",
            r"(c) \(0.728 \times 10^{-7}\)",
            r"(d) \(6.33 \times 10^{-2}\)"
        ],
        "A"
    ),
    (
        r"The magnetic dipole moment of a magnetic dipole is given by the formula ____.",
        [
            r"M = m \times 2I",
            r"M = m + 2I",
            r"M = m - 2I",
            r"M = \frac{m}{2I}"
        ],
        "A"
    ),
    (
        r"A car is moving with an initial speed of 5 m/s. A constant braking force is applied and the car is brought to rest in a distance of 10 m. What is the average speed of the car during the deceleration process?",
        [
            r"a) 1m/s",
            r"b) 2.5m/s",
            r"c) 4m/s",
            r"d) 5m/s"
        ],
        "B"
    ),
    (
        r"Two thin convex lenses L1 and L2,have focal lengths 4 cm and 10 cm, respectively. They are separated by a distance of x cm as shown in the figure. A point source S is placed on the principal axis at a distance 12 cm to the left of L1. If the image of S is formed at infinity, the value of x is:",
        [
            r"a) 6",
            r"b) 16",
            r"c) 14",
            r"d) 24"
        ],
        "B"
    ),
    (
        r"A current carrying long solenoid is formed by winding 200 turns per cm. If the number of turns per cm is increased to 201 keeping the current constant, then the magnetic field inside the solenoid will change by",
        [
            r"a) 0.2%",
            r"b) 0.40%",
            r"c) 0.50%",
            r"d) 1%"
        ],
        "C"
    ),
    (
        r"A series LCR circuit consists of a variable capacitor connected to an inductor of inductance 50 mH,resistor of resistance 100 O and an AC source of angular frequency 500 rad/s. The value of capacitance so that maximum current may be drawn into the circuit is:",
        [
            r"a)60 µF",
            r"b)50 µF",
            r"c)100 µF",
            r"d)80 µF"
        ],
        "D"
    ),
    (
        r"Consider telecommunication through optical fibres. Which of the following statements is not true?",
        [
            r"(a) Optical fibres can be of graded refractive index",
            r"(b) Optical fibres are subject to electromagnetic interference from outside",
            r"(c) Optical fibres have extremely low transmission loss",
            r"(d) Optical fibres may have a homogeneous core with a suitable cladding"
        ],
        "B"
    ),
    (
        r"If the distance traveled by a particle in time t is represented by \(x = 2 \cos at - \sin (2a - 1) t(a - 1)\) and if the motion is simple harmonic motion then a is",
        [
            r"a) ?",
            r"b) \frac{1}{4}",
            r"c) \frac{1}{2}",
            r"d) \sqrt{3} + 1"
        ],
        "C"
    ),
     (
        r"A solid sphere of radius r is revolving about one of its diameters with an angular velocity . If it suddenly expands uniformly so that its radius increases to n times its original value, then its angular velocity becomes",
        [
            r"(A) \(n^2 \omega\)",
            r"(B) \(\frac{\omega}{n^2}\)",
            r"(C) \(?\omega\)",
            r"(D) \(\frac{\omega}{n}\)",
            r"(E) \(2n\omega\)"
        ],
        "A"
    ),
    (
        r"If a ring rolls down from top to bottom of an inclined plane, it takes time \(t_1\). If it slides, it takes time \(t_2\). Then the ratio \(\frac{t_2^2}{t_1^2}\) is",
        [
            r"(A) \(\frac{1}{3}\)",
            r"(B) \(\frac{2}{3}\)",
            r"(C) \(\frac{1}{4}\)",
            r"(D) \(\frac{1}{2}\)",
            r"(E) \(\frac{2}{5}\)"
        ],
        "D"
    ),
    (
        r"If the distance between sun and earth is \(d\), then the angular momentum of earth around the sun is proportional to",
        [
            r"(A) \(vd\)",
            r"(B) \(d^2\)",
            r"(C) \(d^{\frac{1}{3}}\)",
            r"(D) \(d\)",
            r"(E) \(d^{\frac{3}{2}}\)"
        ],
        "A"
    ),
    (
        r"Two identical objects each of mass 50 kg are kept at a distance of separation of 50 cm apart on a horizontal table. The net gravitational force at the mid-point of the line joining their centres is",
        [
            r"(A) zero",
            r"(B) \(6.6733 \times 10^{-9}\, \text{N}\)",
            r"(C) \(13.346 \times 10^{-9}\, \text{N}\)",
            r"(D) \(3.336 \times 10^{-9}\, \text{N}\)",
            r"(E) \(6.673 \times 10^6\, \text{N}\)"
        ],
        "A"
    ),
    (
        r"The ratio of the weight of a body at a height of \( \frac{R}{10} \) from the surface of the earth to that at a depth binomial(R,10) is (R is radius of earth)",
        [
            r"(A) 4:5",
            r"(B) 1:1",
            r"(C) 9:8",
            r"(D) 8:9"
        ],
        "D"
    ),
    (
        r"The electric flux (in SI units) through any face of a cube due to a positive charge Q situated at the centre of a cube is",
        [
            r"(A) \(\frac{Q}{4\pi \varepsilon_0}\)",
            r"(B) \(4\pi \varepsilon_0 Q\)",
            r"(C) \(\frac{Q}{6\varepsilon_0}\)",
            r"(D) \(\frac{Q}{6\pi \varepsilon_0}\)",
            r"(?) \(6\pi \varepsilon_0 Q\)"
        ],
        "C"
    ),
    (
        r"A capacitance of a parallel plate air capacitor is 10µF. Dielectric constant of the medium to be introduced in between its plates to double its capacitance is",
        [
            r"(A) 2",
            r"(B) 3",
            r"(C) 4",
            r"(D) 2.5",
            r"(E) 1.5"
        ],
        "A"
    ),
    (
        r"The electric potential \(V\) at any point \((x, y, z)\) in space is given by \(V = 4x^2\) volt, where \(x\), \(y\), \(z\) are all in metre. The electric field at that point \((1\, \text{m}, 0, 2\, \text{m})\) in V/m is",
        [
            r"(A) 16\, \text{along the positive x axis}",
            r"(B) 16\, \text{along the negative x axis}",
            r"(C) 4\, \text{along the positive x axis}",
            r"(D) 8\, \text{along the negative x axis}"
        ],
        "D"
    ),
    (
        r"The work done in moving a point charge of \(10\mu C\) through a distance of \(3\, \text{cm}\) along the equatorial axis of an electric dipole is",
        [
            r"(A) \(10 \times 10^{-6}\, \text{J}\)",
            r"(B) 0",
            r"(C) \(20 \times 10^{-6}\, \text{J}\)",
            r"(D) \(5 \times 10^{-6}\, \text{J}\)"
        ],
        "B"
    ),
    (
        r"If a monoatomic gas is compressed adiabatically to \(\frac{1}{27}\)th of its initial volume, then its pressure becomes",
        [
            r"(A) 27\, \text{times}",
            r"(B) 125\, \text{times}",
            r"(C) 243\, \text{times}",
            r"(D) 81\, \text{times}",
            r"(E) 64\, \text{times}"
        ],
        "C"
    ),
    (
        r"The values of \(C_p\) and \(C_v\), for a diatomic gas are respectively (R = gas constant)",
        [
            r"(A) \(\frac{7}{2} R\), \(\frac{5}{2} R\)",
            r"(B) \(\frac{3}{2} R\), \(\frac{5}{2} R\)",
            r"(C) \(3R\), \(4R\)",
            r"(D) \(\frac{5}{2} R\), \(\frac{3}{2} R\)"
        ],
        "A"
    ),
    (
        r"Three moles of an ideal gas are in a rigid cubical box with sides of length \(0.170 \, \text{m}\). The ratio of the forces that the gas exerts on each of the six sides of the box when the gas temperature is \(27^\circ \text{C}\) and \(127^\circ \text{C}\) is",
        [
            r"(A) 6:1",
            r"(B) 1:2",
            r"(C) 3:1",
            r"(D) 3:4",
            r"(E) 1:3"
        ],
        "D"
    ),
    (
        r"The average kinetic energy of a monoatomic gas molecule kept at temperature \(27^\circ \text{C}\) is",
        [
            r"(A) \(5.85 \times 10^{-21} \, \text{J}\)",
            r"(B) \(4.12 \times 10^{-21} \, \text{J}\)",
            r"(C) \(3.75 \times 10^{-21} \, \text{J}\)",
            r"(D) \(2.85 \times 10^{-21} \, \text{J}\)",
            r"(E) \(7.55 \times 10^{-21} \, \text{J}\)"
        ],
        "A"
    ),
    (
        r"A particle is moved in a semi-circular path of radius \(R\). Then",
        [
            r"(A) its average velocity is zero",
            r"(B) its average acceleration is zero",
            r"(C) its magnitude of displacement is \(2R\)",
            r"(D) its average velocity and average speed are equal",
            r"(E) its distance travelled is equal to displacement"
        ],
        "C"
    ),
    (
        r"Two projectiles P and Q thrown with velocities \(v\) and \(\frac{v}{2}\) respectively have the same range. If Q is thrown at an angle of \(15^\circ\) to the horizontal, P must be thrown at an angle of",
        [
            r"(A) \(45^\circ\)",
            r"(B) \(\frac{1}{2} \sin^{-1}\left(\frac{1}{8}\right)\)",
            r"(C) \(\frac{1}{4} \sin^{-1}\left(\frac{1}{2}\right)\)",
            r"(D) \(60^\circ\)"
        ],
        "A"
    )
    ]
# Corresponding answers list
answers = [
    "D", "C", "C", "D", "A",
    "D", "B", "E", "C", "D",
    "C", "B", "C", "C", "B",
    "C", "B", "D", "B", "C",
    "B", "C", "A", "A", "B",
    "B", "C", "D", "B", "C",
    "A", "D", "A", "A", "D",
    "C", "A", "D", "B", "C",
    "A", "D", "A", "C", "A"
]
def create_question_xml(question_text, options, correct_option, question_number):
    question = ET.Element('question', type='multichoice')
    
    name = ET.SubElement(question, 'name')
    text = ET.SubElement(name, 'text')
    text.text = f'Question {question_number}'

    questiontext = ET.SubElement(question, 'questiontext', format='html')
    text = ET.SubElement(questiontext, 'text')
    text.text = html.escape(question_text)

    defaultgrade = ET.SubElement(question, 'defaultgrade')
    defaultgrade.text = '4'

    penalty = ET.SubElement(question, 'penalty')
    penalty.text = '1'

    single = ET.SubElement(question, 'single')
    single.text = 'true'

    shuffleanswers = ET.SubElement(question, 'shuffleanswers')
    shuffleanswers.text = 'true'

    answernumbering = ET.SubElement(question, 'answernumbering')
    answernumbering.text = 'abc'

    for i, option in enumerate(options):
        answer = ET.SubElement(question, 'answer', fraction="100" if chr(65 + i) == correct_option else "0")
        text = ET.SubElement(answer, 'text')
        text.text = option
        
        feedback = ET.SubElement(answer, 'feedback')
        text = ET.SubElement(feedback, 'text')
        text.text = ""

    return question

def create_quiz_xml(questions_answers, answers):
    quiz = ET.Element('quiz')
    for i, (question_text, options, _) in enumerate(questions_answers):
        correct_option = answers[i]
        question = create_question_xml(question_text, options, correct_option, i + 1)
        quiz.append(question)
    return quiz

# Create XML structure
quiz_xml = create_quiz_xml(questions_answers, answers)

# Convert to a string
xml_str = ET.tostring(quiz_xml, encoding='unicode')

# Write to file
with open('moodle_questions.xml', 'w', encoding='utf-8') as f:
    f.write(xml_str)

print("Moodle XML file has been created successfully.")
print(len(questions_answers))