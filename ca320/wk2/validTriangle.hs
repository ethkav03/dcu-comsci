checkSides :: Float -> Float -> Float -> Bool
checkSides a b c = a + b > c && c + b > a && a + c > b