type Poly = [Float]

addPolys :: Poly -> Poly -> Poly
addPolys [] p = p
addPolys p [] = p
addPolys (p:ps) (q:qs) = (p+q):(addPolys ps qs)