triangleArea :: Float -> Float -> Float -> Float
triangleArea a b c = (((a + b + c)/2.0)* (((a + b + c)/2.0) - a) * (((a + b + c)/2.0) - b) * (((a + b + c)/2.0) - c)) ** 0.5

isSum :: Float -> Float -> Float -> Bool
isSum a b c = a + b > c && a + c > b && b + c > a

triangleArea2 :: Float -> Float -> Float -> Float
triangleArea2 a b c
    | isSum a b c = triangleArea a b c
    | otherwise = error "Not a triangle!"