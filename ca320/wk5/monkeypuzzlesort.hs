data BinTree t = Empty | Root t (BinTree t) (BinTree t)
    deriving (Eq, Ord, Show)

myTree = Root 5 (Root 1 (Empty) (Root 3 Empty Empty))
    (Root 7 Empty Empty)

leaf x = Root x Empty Empty

myTree1 = Root 5 (Root 1 (Empty) (leaf 3)) (leaf 7)

addnode :: Ord a => a -> BinTree a -> BinTree a
addnode a Empty = leaf a
addnode a (Root t left right)
    | a < t = Root t (addnode a left) right
    | otherwise = Root t left (addnode a right)

maketree :: Ord a => [a] -> BinTree a
