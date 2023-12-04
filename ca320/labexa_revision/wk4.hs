myAppend :: [a] -> [a] -> [a]
myAppend a b = a ++ b

myHead :: [a] -> a
myHead [] = error "Empty list"
myHead (a:_) = a

myLast :: [a] -> a
myLast [] = error "Empty list"
myLast [a] = a
myLast (_:b) = myLast b

myTail :: [a] -> [a]
myTail [] = error "Empty list"
myTail (_:b) = b

myInit :: [a] -> [a]
myInit [] = error "Empty list"
myInit [a] = []
myInit (a:as) = [a] ++ myInit as

myLength :: [a] -> Int
myLength [] = 0
myLength (_:as) = 1 + myLength as

myReverse :: [a] -> [a]
myReverse [] = []
myReverse (a:as) = myReverse as ++ [a]

myConcat :: [[a]] -> [a]
myConcat [] = []
myConcat (a:as) = a ++ myConcat as

mySum :: Num a => [a] -> a
mySum [] = 0
mySum (a:as) = a + mySum as

myProduct :: Num a => [a] -> a
myProduct [] = 1
myProduct (a:as) = a * myProduct as

myMaximum :: Ord a => [a] -> a
myMaximum [] = error "Empty list"
myMaximum [a] = a
myMaximum (a:as)
    | a > head as = myMaximum ([a] ++ (myTail as))
    | otherwise = myMaximum as

myMinimum :: Ord a => [a] -> a
myMinimum [] = error "Empty list"
myMinimum [a] = a
myMinimum (a:as)
    | a < head as = myMinimum ([a] ++ (myTail as))
    | otherwise = myMinimum as

myElem :: Eq a => a -> [a] -> Bool
myElem a [] = False
myElem a (b:bs)
    | a == b = True
    | otherwise = myElem a bs

myDelete :: Eq a => a -> [a] -> [a]
myDelete a [] = []
myDelete a (b:bs)
    | a == b = bs
    | otherwise =  [b] ++ myDelete a bs

myUnion :: Eq a => [a] -> [a] -> [a]
myUnion a [] = a
myUnion a (b:bs)
    | myElem b a = myUnion a bs
    | otherwise = myUnion (myAppend a [b]) bs

myIntersect :: Eq a => [a] -> [a] -> [a]
myIntersect [] [] = []
myIntersect a [] = []
myIntersect [] a = []
myIntersect (a:as) b
    | myElem a b = [a] ++ myIntersect as b
    | otherwise = myIntersect as b