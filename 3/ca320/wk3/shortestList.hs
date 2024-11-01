shortest :: [[a]] -> [a]
shortest [x] = x
shortest (x:y:lst)
    | length x > length y = shortest (y:lst)
    | otherwise = shortest (x:lst)