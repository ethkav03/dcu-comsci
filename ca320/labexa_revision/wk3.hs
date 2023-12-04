isPalindrome :: (Eq a) => [a] -> Bool
isPalindrome a = a == reverse a

shortest :: [[a]] -> [a]
shortest [a] = a
shortest (a:as)
    | length a < length (head as) = shortest ([a] ++ tail as)
    | otherwise = shortest as

type Poly = [Int]
sumPoly :: Poly -> Poly -> Poly
sumPoly [] [] = []
sumPoly [a] [] = [a]
sumPoly [] [a] = [a]
sumPoly (a:as) (b:bs) = (a + b):sumPoly as bs

evalPoly :: Int -> [Int] -> Int
evalPoly a [] = 0
evalPoly a [b] = b
evalPoly a (b:bs) = b + (a * evalPoly a bs)