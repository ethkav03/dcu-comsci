data BinTree t = Empty | Root t (BinTree t) (BinTree t)
 deriving (Eq, Ord, Show)

myTree = Root 5 (Root 1 (Empty) (Root 3 Empty Empty))
 (Root 7 Empty Empty)

leaf x = Root x Empty Empty

myTree1 = Root 5 (Root 1 (Empty) (leaf 3))
 (leaf 7)

addnode :: Ord a => a -> BinTree a -> BinTree a
addnode a Empty = leaf a
addnode a (Root x left right)
    | a < x = Root x (addnode a left) right
    | otherwise = Root x left (addnode a right)

maketree :: Ord a => [a] -> BinTree a
maketree [] = Empty
maketree (a:as) = addnode a (maketree as)

inorder :: BinTree a -> [a]
inorder Empty = []
inorder (Root a left right) = inorder left ++ [a] ++ inorder right

mpsort :: Ord a => [a] -> [a]
mpsort a = inorder (maketree a)

hosort (<) a = mpsort a
hosort (>) a = reverse (mpsort a)

x = sum(map (^2) (filter even [1..100]))

evalPoly :: Int -> [Int] -> Int
evalPoly a [] = 0
evalPoly a (b:bs) = b + a * evalPoly a bs


longest :: Ord a => [[a]] -> [a]
longest [] = []
longest [a] = a
longest (a:as)
    | a > head as = longest ([a] ++ tail as)
    | otherwise = longest as