type Poly = [Float]

evalPoly :: Poly -> Float -> Float
evalPoly [p] _ = p
evalPoly (p:ps) x = p + (x * (evalPoly ps x))