triangleArea :: Float -> Float -> Float -> Float
triangleArea a b c = sqrt ((half a b c) * ((half a b c) - a) * ((half a b c) - b) * ((half a b c) - c))

half :: Float -> Float -> Float -> Float
half a b c = (a + b + c) / 2