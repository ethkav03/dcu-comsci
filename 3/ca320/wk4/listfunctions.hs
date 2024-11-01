myAppend :: [a] -> [a] -> [a]
myAppend a b = a ++ b

myHead :: [a] -> a
myHead [] = error "Must not be an empty list"
myHead (a:_) = a

myLast :: [a] -> a
myLast [] = error "Must not be an empty list"
myLast [a] = a
myLast (_:as) = myLast as

myTail :: [a] -> [a]
myTail [] = error "Must not be an empty list"
myTail (_:as) = as

myInit :: [a] -> [a]
myInit [] = error "Must not be an empty list"
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
myMaximum [] = error "Must not be an empty list"
myMaximum [a] = a
myMaximum (a:as) = do
    if a > myMaximum as
        then a
    else myMaximum as

myMinimum :: Ord a => [a] -> a
myMinimum [] = error "Must not be an empty list"
myMinimum [a] = a
myMinimum (a:as) = do
    if a < myMinimum as
        then a
    else myMinimum as

myElem :: Eq a => a -> [a] -> Bool
myElem b [] = False
myElem b (a:as)
    | b == a = True
    | otherwise = myElem b as

myDelete :: Eq a => a -> [a] -> [a]
myDelete a [] = []
myDelete a (h:t)
    | a == h = t
    | otherwise = [h] ++ myDelete a t

myUnion :: Eq a => [a] -> [a] -> [a]
myUnion [] b = b
myUnion (a:as) b
    | myElem a b = myUnion as b
    | otherwise = a:myUnion as b

myIntersect :: Eq a => [a] -> [a] -> [a]
myIntersect [] b = []
myIntersect a [] = []
myIntersect (a:as) b
    | myElem a b = a:myIntersect as b
    | otherwise = myIntersect as b