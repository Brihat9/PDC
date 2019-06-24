### PDC LAB 4 (MAXIMUM SUM SUB SEGMENT)

#### Steps

1. d<sub>j</sub> be input array, i and j are index
2. S<sub>j</sub> = &sum; d<sub>i</sub> | i &le; j
3. M<sub>j</sub> = &cap; S<sub>i</sub> | i &ge; j
4. e<sub>j</sub> = &cap; i | S<sub>i</sub> = M<sub>j</sub>
5. m<sub>j</sub> = M<sub>j</sub> - S<sub>j</sub> + d<sub>j</sub>
6. t = &cap; m<sub>i</sub>

#### Result
1. Start Index (x) = &cap; i | m<sub>i</sub> = t
2. End Index (y) = e<sub>x</sub>
3. Maximum sum = t
