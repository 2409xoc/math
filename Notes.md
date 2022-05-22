## TODO:
- Understand the Pythagorean Triplet algorithm - derivation from primitive Pythagorean Triple "formula"
- Optimization of Collatz Conjecture Sequence (maybe -> using existing nodes)
- Extensions to fun questions:
  - Collatz Conjecture -> create a [graph](https://upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Collatz-graph-50-no27.svg/130px-Collatz-graph-50-no27.svg.png) relating odd numbers to their next odd node -> from (1, 1000)
    - Frequency graph
  - Program (visualization) factors being generated from a number using the prime factorization algorithm: find prime numbers upto n/2 (p1, p2..., pn) -> divide n/p(n) if (n%p == 0)
- Project Ideas:
  - Curve Image (Re)generation: input image -> identify curves -> create (predicted) f(x) for each curve -> recreate image using f(x) instead of original curve [parameters: f(x) limited to quadratic, cubic, (linear), etc]

### General:
- Better understand every "optimization" found within the Euler page
- Go through current iPython Notebooks to find optimizations for each algorithm (-> significant optimizations)
  - Factors: currently iterating/creating prime factorization for each triangle number (p1^e1 * p2^e2 * p3^e3... * pn^en) and finding amount of factors using ((e1+1) * (e2+1) * (e3+1)...(en+1))
  - Maximum Path Sum: find a more effective method of generating orders -> 2^n (currently iterating through numbers upto 2^n+1 and going through (if) statements... (inefficient)) -> find more effective way of getting solution -> comparing values?

## Notes:

### <https://www.math.utah.edu/~alfeld/math.html>:
Mathematics requires no memorization, it requires connective understanding. Everything within the field of math is interconnected, and built up of smaller simpler concepts.

**Understanding Mathematics means to**:

- Be able to explain mathematical concepts and facts in terms of simpler concepts and facts
- Making logical connections between different facts and concepts
- Recognize the connection when you encounter something new (both within and outside of mathematics), that's similar and connected to the mathematics
- Identify the principles within a given piece of mathematics that make it work

**Acquiring Mathematical Understanding:**

- Strive for understanding, rather than memorization
- Do exercises
- Always check answers for plausibility
- Don't use technology to create your answers:
	- Use it to check your answers
	- Take care of routine tasks efficiently
	- Do things that cannot be done by hand

>> "The purpose of computing is insight, not numbers"

## Sources:
- "What is Mathematics" - Courant and Robbins
- Unsolved Conjectures: "http://www.math.utah.edu/~pa/math/conjectures.html"
- How to Solve it - G. Polya ISBN 0-691-08097-6


