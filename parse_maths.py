import xml.etree.ElementTree as ET
import html

# Input questions and answers as a list of tuples (question_text, options, correct_option)
questions_answers = [
   (
        r"If \(\vec{u}=\hat{i}-3 \hat{j}+2 \hat{k}\) and \(\vec{v}=2 \hat{i}+4 \hat{j}-5 \hat{k}\), then \(|\vec{u} \times \vec{v}|^{2}+|\vec{u} \cdot \vec{v}|^{2}=\)",
        [
            r"(A) 640",
            r"(B) 630",
            r"(C) 690",
            r"(D) 740",
            r"(E) 730"
        ],
        "B"
    ),
    (
        r"If \(\vec{a}=\hat{i}+\hat{j}-\hat{k}\), \(\vec{b}=2 \hat{i}+3 \hat{j}+\hat{k}\), and \(\theta\) is the angle between them, then \(\tan \theta=\)",
        [
            r"(A) \(\frac{\sqrt{38}}{4}\)",
            r"(B) \(\frac{\sqrt{26}}{4}\)",
            r"(C) \(\frac{\sqrt{26}}{5}\)",
            r"(D) \(\frac{\sqrt{26}}{6}\)",
            r"(E) \(\frac{\sqrt{38}}{6}\)"
        ],
        "B"
    ),
    (
        r"The values of \(\alpha\) so that \(|\alpha \hat{i}+(\alpha+1) \hat{j}+2 \hat{k}|=3\), are",
        [
            r"(A) \(2,-4\)",
            r"(B) 1,2",
            r"(C) \(-1,2\)",
            r"(D) \(-2,4\)",
            r"(E) \(1,-2\)"
        ],
        "E"
    ),
    (
        r"If \(\vec{a}=2 \hat{i}+2 \hat{j}+3 \hat{k}\) and \(\vec{b}=2 \hat{i}-\hat{j}+\hat{k}\), then the value of \((\vec{a}+\vec{b}) \cdot(\vec{a}-\vec{b})\) is equal to",
        [
            r"(A) 8",
            r"(B) 7",
            r"(C) 9",
            r"(D) 11",
            r"(E) 13"
        ],
        "D"
    ),
    (
        r"The value of \(\int_{e}^{e^{2}} \frac{1}{x} dx\) is equal to",
        [
            r"(A) \(e\)",
            r"(B) 1",
            r"(C) \(e^{2}\)",
            r"(D) \(e^{2}-e\)",
            r"(E) 0"
        ],
        "B"
    ),
      (
        r"The value of \(\int_{-10}^{10}\left(0.0002 x^{3}-0.3 x+20\right) dx\) is equal to",
        [
            r"(A) 423",
            r"(B) 400",
            r"(C) 378",
            r"(D) 410",
            r"(E) 390"
        ],
        "B"
    ),
    (
        r"The area enclosed by the curve \(x=3 \cos \theta, y=2 \sin \theta, 0 \leq \theta \leq \pi\), is (in square units)",
        [
            r"(A) \(9 \pi\)",
            r"(B) \(6 \pi\)",
            r"(C) \(4 \pi\)",
            r"(D) \(3 \pi\)",
            r"(E) \(2 \pi\)"
        ],
        "B"
    ),
    (
        r"If \(x^{3}+2 x y+\frac{1}{3} y^{3}=\frac{11}{3}\), then \(\frac{d y}{d x}\) at \((2,-1)\) is",
        [
            r"(A) -2",
            r"(B) 2",
            r"(C) 5",
            r"(D) -5",
            r"(E) -10"
        ],
        "A"
    ),
    (
        r"The equation of the tangent to \(y=-2 x^{2}+3\) at \(x=1\) is",
        [
            r"(A) \(y=-4 x\)",
            r"(B) \(y=-4 x+5\)",
            r"(C) \(y=4 x\)",
            r"(D) \(y=4 x+5\)",
            r"(E) \(y=-4 x+3\)"
        ],
        "B"
    ),
    (
        r"The integrating factor of the differential equation \(3 x y^{\prime}-y=1+\log x, x>0\) is",
        [
            r"(A) \(\log x\)",
            r"(B) \(\frac{1}{x}\)",
            r"(C) \(x^{-1 / 3}\)",
            r"(D) \(\frac{1}{x^{3}}\)",
            r"(E) \(x^{1 / 3}\)"
        ],
        "C"
    ),
     (
        r"If \(\left(\begin{array}{ll}e & f \\ g & h\end{array}\right)\) is the inverse of the matrix \(\left(\begin{array}{ll}a & b \\ c & d\end{array}\right)\) where \(a d-b c=1\), then \(g\) equals",
        [
            r"(A) \(c\)",
            r"(B) \(-c\)",
            r"(C) \(b\)",
            r"(D) \(-b\)",
            r"(E) \(d\)"
        ],
        "B"
    ),
    (
        r"If \(f: \mathbb{R} \rightarrow \mathbb{R}\) is a function defined by \(f(x)=x^{2}\), then which of the following is true?",
        [
            r"(A) \(f\) is 1-1 but not onto",
            r"(B) \(f\) is onto but not 1-1",
            r"(C) \(f\) is neither 1-1 nor onto",
            r"(D) \(f\) is both 1-1 and onto",
            r"(E) \(f^{-1}: \mathbb{R} \rightarrow \mathbb{R}\) exists"
        ],
        "C"
    ),
    (
        r"Let \(\mathrm{A}=\left(\begin{array}{ll}\alpha & 0 \\ 1 & 1\end{array}\right)\) and \(\mathrm{B}=\left(\begin{array}{ll}1 & 0 \\ 5 & 1\end{array}\right)\) be two matrices where \(\alpha\) is a real number. Then",
        [
            r"(A) \(\mathrm{A}^{2}=\mathrm{B}\) for some \(\alpha\)",
            r"(B) \(\mathrm{A}^{2} \neq \mathrm{B}\) for any \(\alpha\)",
            r"(C) \(\mathrm{A}^{2}=-\mathrm{B}\) for some \(\alpha\)",
            r"(D) \(\left|\mathrm{A}^{2}\right| \neq|B|\) for any \(\alpha\)",
            r"(E) \(A=-B\) for some \(\alpha\)"
        ],
        "B"
    ),
    (
        r"If the lines \(\frac{x+3}{-3}=\frac{y-1}{k}=\frac{z-5}{5}\) and \(\frac{x+1}{-1}=\frac{y-2}{2}=\frac{z-5}{5}\) are coplanar, then the value of \(k\) is",
        [
            r"(A) 1",
            r"(B) 2",
            r"(C) 3",
            r"(D) 4",
            r"(E) 5"
        ],
        "A"
    ),
    (
        r"If \(\frac{d y}{d x}=\frac{2}{x+y}\) and \(y(1)=0\), then \(x+y+2\) equals",
        [
            r"(A) \(3 e^{\left(\frac{y}{2}\right)}\)",
            r"(B) \(2 e^{\left(\frac{y}{2}\right)}\)",
            r"(C) \(e^{\left(\frac{y}{2}\right)}\)",
            r"(D) 0",
            r"(E) \(5 e^{\left(\frac{y}{2}\right)}\)"
        ],
        "A"
    ),
     (
        r"The points with position vector \(60 \hat{i}+3 \hat{j}, 40 \hat{i}-8 \hat{j}\) and \(a \hat{i}-52 \hat{j}\) are collinear if",
        [
            r"(A) \(a=-10\)",
            r"(B) \(a=40\)",
            r"(C) \(a=20\)",
            r"(D) \(a=10\)",
            r"(E) \(a=-40\)"
        ],
        "E"
    ),
    (
        r"The area enclosed within the curve \(|x|+|y|=1\) is",
        [
            r"(A) 1",
            r"(B) \(\sqrt{2}\)",
            r"(C) \(\frac{3}{2}\)",
            r"(D) \(2 \sqrt{2}\)",
            r"(E) 2"
        ],
        "E"
    ),
    (
        r"The value of \(\tan \left[\sin ^{-1} \frac{5}{13}+\cot ^{-1} \frac{4}{3}\right]\) is",
        [
            r"(A) \(\frac{26}{11}\)",
            r"(B) \(\frac{56}{33}\)",
            r"(C) \(\frac{63}{41}\)",
            r"(D) \(\frac{65}{43}\)",
            r"(E) \(\frac{32}{13}\)"
        ],
        "B"
    ),
    (
        r"If \(\sqrt{\frac{y}{x}}+\sqrt{\frac{x}{y}}=1\), then \(\frac{d y}{d x}\) equals",
        [
            r"(A) \(\sqrt{\frac{y}{x}}\)",
            r"(B) \(\sqrt{\frac{x}{y}}\)",
            r"(C) \(\frac{y}{x}\)",
            r"(D) \(\frac{x}{y}\)",
            r"(E) \(x y\)"
        ],
        "C"
    ),
    (
        r"The value of the integral \(\int_{0}^{\frac{\pi}{2}} \log \tan \theta d \theta\) is",
        [
            r"(A) 0",
            r"(B) 1",
            r"(C) \(\frac{\pi}{2}\)",
            r"(D) \(\log 2\)",
            r"(E) 2"
        ],
        "A"
    ),
     (
        r"Let \(\Delta=\left|\begin{array}{ccc}1 & 1 & 1 \\ 1 & -1-w^{2} & w^{2} \\ 1 & w & w^{4}\end{array}\right|\), where \(w \neq 1\) is a complex number such that \(w^{3}=1\). Then \(\Delta\) equals",
        [
            r"(A) \(3 w+w^{2}\)",
            r"(B) \(3 w^{2}\)",
            r"(C) \(3\left(w-w^{2}\right)\)",
            r"(D) \(-3 w^{2}\)",
            r"(E) \(3 w^{2}+1\)"
        ],
        "B"
    ),
    (
        r"If \(\left|\begin{array}{rrr}3 i & -9 i & 1 \\ 2 & 9 i & -1 \\ 10 & 9 & i\end{array}\right|=x+i y\), then",
        [
            r"(A) \(x=1, y=1\)",
            r"(B) \(x=0, y=1\)",
            r"(C) \(x=1, y=0\)",
            r"(D) \(x=0, y=0\)",
            r"(E) \(x=-1, y=0\)"
        ],
        "D"
    ),
    (
        r"The number of \(3 \times 3\) matrices with entries -1 or +1 is",
        [
            r"(A) \(2^{4}\)",
            r"(B) \(2^{5}\)",
            r"(C) \(2^{6}\)",
            r"(D) \(2^{7}\)",
            r"(E) \(2^{9}\)"
        ],
        "E"
    ),
    (
        r"Let \(S\) be the set of all \(2 \times 2\) symmetric matrices whose entries are either zero or one. A matrix \(\mathrm{X}\) is chosen from \(S\). The probability that the determinant of \(\mathrm{X}\) is not zero is",
        [
            r"(A) \(\frac{1}{3}\)",
            r"(B) \(\frac{1}{2}\)",
            r"(C) \(\frac{3}{4}\)",
            r"(D) \(\frac{1}{4}\)",
            r"(E) \(\frac{2}{9}\)"
        ],
        "B"
    ),
    (
        r"The order of the differential equation \(\left(\frac{d^{3} y}{d x^{3}}\right)^{2}+\left(\frac{d^{2} y}{d x}\right)^{2}+\left(\frac{d y}{d x}\right)^{5}=0\) is",
        [
            r"(A) 3",
            r"(B) 4",
            r"(C) 1",
            r"(D) 5",
            r"(E) 6"
        ],
        "A"
    ),
     (
        r"For all real numbers \(x\) and \(y\), it is known that the real valued function \(f\) satisfies \(f(x)+f(y)=f(x+y)\). If \(f(1)=7\), then \(\sum_{r=1}^{100} f(r)\) is equal to",
        [
            r"(A) \(7 \times 51 \times 102\)",
            r"(B) \(6 \times 50 \times 102\)",
            r"(C) \(7 \times 50 \times 102\)",
            r"(D) \(6 \times 25 \times 102\)",
            r"(E) \(7 \times 50 \times 101\)"
        ],
        "E"
    ),
    (
        r"If \(f(x)=\left|\begin{array}{ccc}x & x^{2} & x^{3} \\ 1 & 2 x & 3 x^{2} \\ 0 & 2 & 6 x\end{array}\right|\), then \(f^{\prime}(x)\) is equal to",
        [
            r"(A) \(x^{3}+6 x^{2}\)",
            r"(B) \(6 x^{3}\)",
            r"(C) \(3 x\)",
            r"(D) \(6 x^{2}\)",
            r"(E) 0"
        ],
        "D"
    ),
    (
        r"The equations \(\lambda x-y=2,2 x-3 y=-\lambda\) and \(3 x-2 y=-1\) are consistent for",
        [
            r"(A) \(\lambda=-4\)",
            r"(B) \(\lambda=1,4\)",
            r"(C) \(\lambda=1,-4\)",
            r"(D) \(\lambda=-1,4\)",
            r"(E) \(\lambda=-1\)"
        ],
        "D"
    ),
    (
        r"The area of the parallelogram with vertices \((0,0),(7,2)(5,9)\) and \((12,11)\) is",
        [
            r"(A) 50",
            r"(B) 54",
            r"(C) 51",
            r"(D) 52",
            r"(E) 53"
        ],
        "E"
    ),
    (
        r"If \(\left[\begin{array}{lll}1 & x & 1\end{array}\right]\left[\begin{array}{ccc}1 & 3 & 2 \\ 2 & 5 & 1 \\ 15 & 3 & 2\end{array}\right]\left[\begin{array}{l}1 \\ 2 \\ x\end{array}\right]=0\), then \(x\) can be",
        [
            r"(A) -2",
            r"(B) 2",
            r"(C) 14",
            r"(D) -14",
            r"(E) 0"
        ],
        "A"
    ),
    (
        r"If \(\Delta(x)=\left|\begin{array}{ccc}1 & \cos x & 1-\cos x \\ 1+\sin x & \cos x & 1+\sin x-\cos x \\ \sin x & \sin x & 1\end{array}\right|\), then \(\int_{0}^{\pi / 2} \Delta(x) d x=\)",
        [
            r"(A) \(\frac{-1}{2}\)",
            r"(B) \(\frac{1}{2}\)",
            r"(C) 1",
            r"(D) -1",
            r"(E) 0"
        ],
        "A"
    ),
    (
        r"If \(A=\left(\begin{array}{lll}0 & 1 & 2 \\ 1 & 2 & 3 \\ 3 & 1 & 1\end{array}\right)\), then the sum of all the diagonal entries of \(A^{-1}\) is",
        [
            r"(A) 2",
            r"(B) 3",
            r"(C) -3",
            r"(D) -4",
            r"(E) 4"
        ],
        "E"
    ),
    (
        r"If \(x=A \cos 4 t+B \sin 4 t\), then \(\frac{d^{2} x}{d t^{2}}=\)",
        [
            r"(A) \(x\)",
            r"(B) \(-16 x\)",
            r"(C) \(15 x\)",
            r"(D) \(16 x\)",
            r"(E) \(-15 x\)"
        ],
        "B"
    ),
    (
        r"\(\int \frac{(\sin x+\cos x)(2-\sin 2 x)}{\sin ^{2} 2 x} d x=\)",
        [
            r"(A) \(\frac{\sin x+\cos x}{\sin 2 x}+c\)",
            r"(B) \(\frac{\sin x-\cos x}{\sin 2 x}+c\)",
            r"(C) \(\frac{\sin x}{\sin x+\cos x}+c\)",
            r"(D) \(\frac{\sin x}{\sin x-\cos x}+c\)",
            r"(E) \(\frac{\sin x-\cos x}{\sin x+\cos x}+c\)"
        ],
        "B"
    ),
    (
        r"\(\int_{\pi / 4}^{3 \pi / 4} \frac{x}{1+\sin x} d x=\)",
        [
            r"(A) \(\pi(\sqrt{2}-1)\)",
            r"(B) \(\pi(\sqrt{2}+1)\)",
            r"(C) \(2 \pi(\sqrt{2}-1)\)",
            r"(D) \(2 \pi(\sqrt{2}+1)\)",
            r"(E) \(\frac{\pi}{\sqrt{2}+1}\)"
        ],
        "A"
    ),
     (
        r"If \(|\vec{a}|=13,|\vec{b}|=5\) and \(\vec{a} \cdot \vec{b}=30\), then \(|\vec{a} \times \vec{b}|\) is equal to",
        [
            r"(A) 30",
            r"(B) \(\frac{30}{25} \sqrt{233}\)",
            r"(C) \(\frac{30}{33} \sqrt{193}\)",
            r"(D) \(\frac{65}{23} \sqrt{493}\)",
            r"(E) \(\frac{65}{13} \sqrt{133}\)"
        ],
        "E"
    ),
    (
        r"Let \(f\) and \(g\) be differentiable functions such that \(f(3)=5, g(3)=7\), \(f^{\prime}(3)=13, g^{\prime}(3)=6, f^{\prime}(7)=2\) and \(g^{\prime}(7)=0\). If \(h(x)=(f \circ g)(x)\), then \(h^{\prime}(3)=\)",
        [
            r"(A) 14",
            r"(B) 12",
            r"(C) 16",
            r"(D) 0",
            r"(E) 10"
        ],
        "B"
    ),
    (
        r"If a circular plate is heated uniformly, its area expands \(3 c\) times as fast as its radius, then the value of \(c\) when the radius is 6 units, is",
        [
            r"(A) \(4 \pi\)",
            r"(B) \(2 \pi\)",
            r"(C) \(6 \pi\)",
            r"(D) \(3 \pi\)",
            r"(E) \(8 \pi\)"
        ],
        "A"
    ),
     (
        r"The organization awarded 48 medals in event ' A ', 25 in event ' B ' and 18 in event ' C '. If these medals went to a total of 60 men and only five men got medals in all the three events, then, how many received medals in exactly two of three events?",
        [
            r"A) 15",
            r"B) 9",
            r"C) 21",
            r"D) 10",
            r"E) 28"
        ],
        "C"
    ),
    (
        r"The domain of the function \(\operatorname{cosec}^{-1}\left(\frac{1+x}{x}\right)\) is",
        [
            r"A) \((-1,-\frac{1}{2}]\cup(0, \infty)\)",
            r"B) \((-\frac{1}{2}, \infty)-\{0\}\)",
            r"C) \([- \frac{1}{2}, 0) \cup[1, \infty)\)",
            r"D) \([- \frac{1}{2}, \infty)-\{0\}\)",
            r"E) \((-1,-\frac{1}{2}) \cup\{1\}\)"
        ],
        "D"
    ),
    (
        r"Let \(\odot\) be a binary operation on \(\mathbb{Q}-\{0\}\) defined by \(a \odot b=\frac{a}{b}\). Then \(1 \odot(2 \odot(3 \odot 4))\) is equal to",
        [
            r"(A) \(\frac{3}{2}\)",
            r"(B) \(\frac{8}{3}\)",
            r"(C) \(\frac{4}{3}\)",
            r"(D) \(\frac{3}{4}\)",
            r"(E) \(\frac{3}{8}\)"
        ],
        "E"
    ),
    (
        r"The number of arrangements containing all the seven letters of the word ALRIGHT that begins with LG is",
        [
            r"(A) 720",
            r"(B) 120",
            r"(C) 600",
            r"(D) 540",
            r"(E) 760"
        ],
        "B"
    ),
    (
        r"If \(\tan 15^{\circ}+\frac{1}{\tan 75^{\circ}}+\frac{1}{\tan 105^{\circ}}+\tan 195^{\circ}=2 \mathrm{a}\) then the value of \(\left(a+\frac{1}{a}\right)\) is :",
        [
            r"(A) 4",
            r"(B) \(4-2 \sqrt{3}\)",
            r"(C) 2",
            r"(D) \(5-\frac{3}{2} \sqrt{3}\)",
            r"(E) 1"
        ],
        "A"
    ),
    (
        r"If one real root of the quadratic equation \(81 x^{2}+k x+256=0\) is cube of the other root, then a value of \(k\) is :",
        [
            r"(A) -81",
            r"(B) 100",
            r"(C) 144",
            r"(D) -300",
            r"(E) 178"
        ],
        "D"
    ),
    (
        r"Let \(t_{n}=\frac{1}{n} \sum_{k=1}^{n}\left(\frac{k}{n}\right)^{2}\) for \(n=1,2,3, \cdots\). Then \(t_{10}\) is equal to",
        [
            r"(A) \(\frac{7}{600}\)",
            r"(B) \(\frac{231}{100}\)",
            r"(C) \(\frac{206}{600}\)",
            r"(D) \(\frac{11}{200}\)",
            r"(E) \(\frac{77}{200}\)"
        ],
        "B"
    ),
    (
        r"The number of integral values of \(m\) for which the equation \((1+m^{2}) x^{2}-2(1+3 m) x+(1+8 m)=0\) has no real root is :",
        [
            r"(A) 1",
            r"(B) 2",
            r"(C) infinitely many",
            r"(D) 3",
            r"(E) 4"
        ],
        "C"
    ),
    (
        r"Let \((3+x)^{10}=a_{0}+a_{1}(1+x)+a_{2}(1+x)^{2}+\cdots a_{10}(1+x)^{10}\), where \(a_{1}, a_{2}, \cdots a_{10}\) are constants. Then the value of \(a_{0}+a_{1}+a_{2}+\cdots a_{10}\) is equal to",
        [
            r"(A) \(2^{20}\)",
            r"(B) \(2^{10}\)",
            r"(C) \(3^{10}\)",
            r"(D) \(2^{11}\)",
            r"(E) \(2^{15}\)"
        ],
        "C"
    ),
    (
        r"The sum of all those terms which are rational numbers in the expansion of \((2^{1 / 3}+3^{1 / 4})^{12}\) is",
        [
            r"(A) 89",
            r"(B) 27",
            r"(C) 35",
            r"(D) 43",
            r"(E) 52"
        ],
        "D"
    ),
     (
        r"If \(a y=x+b\) is the equation of the line passing through the points \((-5,-2)\) and \((4,7)\), then the value of \(2 a+b\) is equal to",
        [
            r"(A) 1",
            r"(B) 5",
            r"(C) 3",
            r"(D) -3",
            r"(E) -1"
        ],
        "B"
    ),
    (
        r"The two diameters of a circle are segments of the straight lines \(x-y=5\) and \(2 x+y=4\). If the radius of the circle is 5, then the equation of the circle is",
        [
            r"(A) \(X^{2}+Y^{2}-6 X+4 Y=12\)",
            r"(B) \(X^{2}+Y^{2}-3 X+2 Y=12\)",
            r"(C) \(X^{2}+Y^{2}-6 X+2 Y=12\)",
            r"(D) \(X^{2}+Y^{2}-8 X+6 Y-18 =0\)",
            r"(E) \(X^{2}+Y^{2}-8 X+6 Y=-7\)"
        ],
        "A"
    ),
    (
        r"The eccentricity of the hyperbola \(\frac{(x-3)^{2}}{9}-\frac{4(y-1)^{2}}{45}=1\) is equal to",
        [
            r"(A) \(\sqrt{5}\)",
            r"(B) 5",
            r"(C) 10",
            r"(D) \(2 \sqrt{5}\)",
            r"(E) 3"
        ],
        "D"
    ),
    (
        r"The values of \(\alpha\) so that the vectors \(\alpha \hat{i}+(\alpha-1) \hat{j}+3 \hat{k}\) and \((\alpha+2) \hat{i}+\alpha \hat{j}-2 \hat{k}\) are perpendicular, are",
        [
            r"(A) \(\frac{3}{2},-2\)",
            r"(B) \(2, \frac{3}{2}\)",
            r"(C) \(-2, \frac{-3}{2}\)",
            r"(D) \(2, \frac{-3}{2}\)",
            r"(E) \(-4, \frac{3}{2}\)"
        ],
        "A"
    ),
    (
        r"\(\lim _{x \rightarrow 0} \frac{\log (1+x)+1-e^{x}}{4 x^{2}-9 x}\) is equal to",
        [
            r"(A) 3",
            r"(B) -3",
            r"(C) 9",
            r"(D) -9",
            r"(E) 0"
        ],
        "A"
    ),
     (
        r"The derivative of a function \(f\) is given by \(f^{\prime}(x)=\frac{x-5}{\sqrt{x^{2}+4}}\). Then the interval in which \(f\) is increasing, is",
        [
            r"(A) \((5, \infty)\)",
            r"(B) \((0, \infty)\)",
            r"(C) \((-4, \infty)\)",
            r"(D) \((-\infty,-4)\)",
            r"(E) \((-\infty, 5)\)"
        ],
        "A"
    ),
    (
        r"\(\lim _{x \rightarrow-3} \frac{x^{2}+16 x+39}{2 x^{2}+7 x+3}\) is equal to",
        [
            r"(A) 2",
            r"(B) \(\frac{8}{3}\)",
            r"(C) \(\frac{-8}{3}\)",
            r"(D) -2",
            r"(E) 0"
        ],
        "D"
    ),
    (
        r"\(\frac{d}{d x}\left(\frac{1}{x} \frac{d^{2}}{d x^{2}}\left(\frac{1}{x^{3}}\right)\right)=\)",
        [
            r"(A) \(-36 x^{-7}\)",
            r"(B) \(36 x^{-7}\)",
            r"(C) \(72 x^{-6}\)",
            r"(D) \(72 x^{-7}\)",
            r"(E) \(-72 x^{-7}\)"
        ],
        "E"
    ),
    (
        r"\(\cos ^{4} \frac{\pi}{12}-\sin ^{4} \frac{\pi}{12}\) is equal to",
        [
            r"(A) \(\frac{1}{2}\)",
            r"(B) \(\frac{\sqrt{3}}{2}\)",
            r"(C) \(\frac{\sqrt{3}+1}{2}\)",
            r"(D) \(\frac{\sqrt{3}-1}{2}\)",
            r"(E) \(\frac{\sqrt{2}}{2}\)"
        ],
        "B"
    ),
    (
        r"The number of solutions of \(|\cos x|=\sin x\), such that \(-4 \pi \leq x \leq 4 \pi\) is :",
        [
            r"(A) 3",
            r"(B) 4",
            r"(C) 6",
            r"(D) 8",
            r"(E) 12"
        ],
        "D"
    ),
       (
        r"Let \(f(x)=6 \sqrt[3]{x^{5}}\). If \(f^{\prime}(x)=a x^{p}\), where \(a\) and \(p\) are constants, then the value of \(p\) is equal to",
        [
            r"(A) \(\frac{3}{5}\)",
            r"(B) \(\frac{-2}{5}\)",
            r"(C) \(\frac{2}{3}\)",
            r"(D) \(\frac{-2}{3}\)",
            r"(E) \(\frac{2}{5}\)"
        ],
        "C"
    ),
    (
        r"For \(x \in \mathbb{R}\), two real valued functions \(f(x)\) and \(g(x)\) are such that, \(g(x)=\sqrt{x}+1\) and \(f \circ g(x)=x+3-\sqrt{x}\). Then \(f(0)\) is equal to",
        [
            r"(A) 5",
            r"(B) 0",
            r"(C) -3",
            r"(D) 1",
            r"(E) -2"
        ],
        "A"
    ),
    (
        r"If the sum of an infinite GP \(a, a r, a r^{2}, a r^{3}, \ldots\) is 15 and the sum of the squares of its each term is 150, then the sum of \(a r^{2}, a r^{4}, a r^{6}, \ldots\) is",
        [
            r"(A) \(\frac{5}{2}\)",
            r"(B) \(\frac{1}{2}\)",
            r"(C) \(\frac{25}{2}\)",
            r"(D) \(\frac{17}{2}\)",
            r"(E) \(\frac{9}{2}\)"
        ],
        "B"
    ),
    (
        r"The sum of 10 terms of the series \(\frac{3}{1^{2} \times 2^{2}}+\frac{5}{2^{2} \times 3^{2}}+\frac{7}{3^{2} \times 4^{2}}+\ldots\) is",
        [
            r"(A) 1",
            r"(B) \(\frac{120}{121}\)",
            r"(C) \(\frac{99}{100}\)",
            r"(D) \(\frac{143}{144}\)",
            r"(E) \(\frac{79}{80}\)"
        ],
        "B"
    ),
    (
        r"Let \(z\) be a complex number such that \(\left|\frac{Z-i}{Z+2 i}\right|=1\) and \(|Z|=\frac{5}{2}\). Then the value of \(|Z+3 i|\) is:",
        [
            r"(A) \(\sqrt{5}\)",
            r"(B) \(\frac{7}{2}\)",
            r"(C) \(\frac{15}{4}\)",
            r"(D) \(2 \sqrt{3}\)",
            r"(E) \(\sqrt{3}\)"
        ],
        "B"
    ),
      (
        r"The sum of the cubes of all the roots of the equation \(x^{4}-3 x^{3}-2 x^{2}+3 x+1=0\) is",
        [
            r"(A) 36",
            r"(B) 18",
            r"(C) 24",
            r"(D) 17",
            r"(E) 54"
        ],
        "A"
    ),
    (
        r"A survey shows that \(73 \%\) of the persons working in an office like coffee, whereas \(65 \%\) like tea. If \(x\) denotes the percentage of them, who like both coffee and tea, then \(x\) cannot be:",
        [
            r"(A) 63",
            r"(B) 54",
            r"(C) 28",
            r"(D) 17",
            r"(E) 36"
        ],
        "E"
    ),
    (
        r"If the perpendicular bisector of the line segment joining the points \(P(1,4)\) and \(Q(k, 3)\) has \(y\)-intercept equal to -4 then a value of \(k\) is :",
        [
            r"(A) -2",
            r"(B) 4",
            r"(C) \(\sqrt{14}\)",
            r"(D) \(\sqrt{15}\)",
            r"(E) -4"
        ],
        "E"
    ),
    (
        r"Number of ways of arranging 8 identical books into 4 identical shelves where any number of shelves may remain empty is equal to",
        [
            r"(A) 18",
            r"(B) 16",
            r"(C) 12",
            r"(D) 15",
            r"(E) 11"
        ],
        "D"
    ),
    (
        r"The sum, of the coefficients of the first 50 terms in the binomial expansion of \((1-x)^{100}\), is equal to",
        [
            r"(A) \(-\binom{101}{50}\)",
            r"(B) \(\binom{99}{49}\)",
            r"(C) \(\binom{101}{50}\)",
            r"(D) \(-\binom{99}{49}\)",
            r"(E) none of these"
        ],
        "D"
    ),
     (
        r"Let \(S=\{n \in \mathbb{N} \mid n^3+3n^2+5n+3\) is not divisible by 3\). Then which of the following statements is true about \(S\)",
        [
            r"(A) \(S=\varnothing\)",
            r"(B) \(|S| \geq 2\) and \(|S|\) is a multiple of 5",
            r"(C) \(S\) is non-empty but \(|S|\) is finite",
            r"(D) \(|S|\) is infinite",
            r"(E) \(S\) is non-empty and \(|S|\) is a multiple of 3"
        ],
        "A"
    ),
    (
        r"For any real number \(x\), the least value of \(4 \cos x-3 \sin x+5\) is",
        [
            r"(A) 10",
            r"(B) 2",
            r"(C) 0",
            r"(D) 8",
            r"(E) 4"
        ],
        "C"
    ),
    (
        r"The centre of the circle passing through \((0,0)\) and \((1,0)\) and touching the circle \(x^{2}+y^{2}=9\) is",
        [
            r"(A) \(\left(\frac{1}{2}, \frac{1}{2}\right)\)",
            r"(B) \(\left(\frac{3}{2}, \frac{1}{2}\right)\)",
            r"(C) \(\left(\frac{1}{2}, \frac{3}{2}\right)\)",
            r"(D) \(\left(\frac{1}{2}, \sqrt{2}\right)\)",
            r"(E) \(\left(\frac{1}{2},-\sqrt{2}\right)\)"
        ],
        "B"
    ),
    (
        r"Air is blown into a spherical balloon. If its diameter \(d\) is increasing at the rate of \(3 \mathrm{~cm} / \mathrm{min}\), then the rate at which the volume of the balloon is increasing when \(d=10 \mathrm{~cm}\), is",
        [
            r"(A) \(120 \pi \mathrm{cm}^{3} / \mathrm{min}\)",
            r"(B) \(150 \pi \mathrm{cm}^{3} / \mathrm{min}\)",
            r"(C) \(100 \pi \mathrm{cm}^{3} / \mathrm{min}\)",
            r"(D) \(180 \pi \mathrm{cm}^{3} / \mathrm{min}\)",
            r"(E) \(210 \pi \mathrm{cm}^{3} / \mathrm{min}\)"
        ],
        "B"
    ),
    (
        r"The function \(f(x)=x^{5} e^{-x}\) is increasing in the interval",
        [
            r"(A) \((5, \infty)\)",
            r"(B) \((4, \infty)\)",
            r"(C) \((-4, \infty)\)",
            r"(D) \((-\infty, 5)\)",
            r"(E) \((-\infty,-5)\)"
        ],
        "D"
    ),
     (
        r"If \( p \) and \( q \) are positive integers such that \( { }^{(p+q)} P_{2}=42 \) and \( { }^{(p-q)} P_{2}=20 \) then values of \( p \) and \( q \) are respectively:",
        [
            r"(A) 5,2",
            r"(B) 4,3",
            r"(C) 6,1",
            r"(D) 7,2",
            r"(E) 7,5"
        ],
        "C"
    ),
    (
        r"If \( x+13 y=40 \) is normal to the curve \( y=5 x^{2}+\alpha x+\beta \) at the point \( (1,3) \), then the value of \( \alpha \beta \) is equal to",
        [
            r"(A) 15",
            r"(B) 2",
            r"(C) -6",
            r"(D) 13",
            r"(E) -15"
        ],
        "E"
    )
    ]

# Corresponding answers list
answers = [ "B", "B", "E", "D", "B", 
    "B", "B", "A", "B", "C", 
    "B", "C", "B", "A", "A", 
    "E", "E", "B", "C", "A", 
    "B", "D", "E", "B", "A", 
    "E", "D", "D", "E", "A", 
    "A", "E", "B", "B", "A", 
    "E", "B", "A",
    "C", "D", "E", "B", "A", "D", "B", "C", "C", "D", 
    "B", "A", "D", "A", "A", "A", "D", "E", "B", "D", 
    "C", "A", "B", "B", "B", "A", "E", "E", "D", "D", 
    "A", "C", "B", "B", "D", "C", "E"
]
def create_question_xml(question_text, options, correct_option, question_number):
    question = ET.Element('question', type='multichoice')
    
    name = ET.SubElement(question, 'name')
    text = ET.SubElement(name, 'text')
    text.text = f'Maths Question {question_number}'

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
with open('moodle_math_questions.xml', 'w', encoding='utf-8') as f:
    f.write(xml_str)

print("Moodle XML file has been created successfully.")
print(len(questions_answers))