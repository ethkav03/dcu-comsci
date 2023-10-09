shortest :: [[a]] -> [a]
shortest [] = []
shortest [x] = x
shortest (x:xs)
        (length x) < (length maxTail) = x
        otherwise maxTail
    where maxTail = shortest xs