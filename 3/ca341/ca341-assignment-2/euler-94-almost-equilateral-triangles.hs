equilateralTriangles :: Int -> Int -> Int -> Bool
equilateralTriangles a b c = ((a == b && b + 1 == c) || (c == b && b + 1 == a) || (a == c && c + 1 == b)) && (((3^.5)/4) * (c * c))