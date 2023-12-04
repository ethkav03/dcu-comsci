data BinTree t = Empty | Root t (BinTree t) (BinTree t) deriving (Eq, Ord, Show)

myTree = Root 5 (
    Root 1 (Empty)(Root 3 Empty Empty))
            (Root 7 Empty Empty)

leaf x = Root x Empty Empty

myTree1 = Root 5 (Root 1 (Empty) (leaf 3)) (leaf 7)

addnode :: Ord a => a -> BinTree a -> BinTree a
addnode a Empty = leaf a
addnode a (Root x left right)
    | a > x = Root x left (addnode a right)
    | otherwise = Root x (addnode a left) right

maketree :: Ord a => [a] -> BinTree a
maketree [] = Empty
maketree (a:as) = addnode a (maketree as)

inorder :: BinTree a -> [a]
inorder Empty = []
inorder (Root x left right) = inorder left ++ [x] ++ inorder right

mpsort :: (Ord a) => [a] -> [a]
mpsort a = inorder (maketree a)

hoAddNode :: Ord t => (t -> t -> Bool) -> t -> BinTree t -> BinTree t
hoAddNode _ a Empty = leaf a  
hoAddNode fn x (Root a left right)   
    | fn x a  = Root a (hoAddNode fn x left) right  
    | otherwise  = Root a left (hoAddNode fn x right)


hoMakeTree :: Ord t => (t -> t -> Bool) -> [t] -> BinTree t
hoMakeTree _ [] = Empty
hoMakeTree fn (x:xs) = hoAddNode fn x (hoMakeTree fn xs)


hosort :: Ord t => (t -> t -> Bool) -> [t] -> [t]
hosort fn x = inorder (hoMakeTree fn x)

{-hoaddnode :: Ord a => (a -> a -> Bool) -> a -> BinTree a -> BinTree a
hoaddnode _ a Empty = leaf a
hoaddnode fn a (Root x left right)
    | a fn x = Root x (hoaddnode fn a left) right
    | otherwise = Root x left (hoaddnode fn a right)

homaketree :: Ord a => (a -> a -> Bool) -> [a] -> BinTree a
homaketree _ [] = Empty
homaketree fn (a:as) = hoaddnode fn a (homaketree fn as)

hosort :: Ord a => (a -> a -> Bool) -> [a] -> [a]
hosort fn a = inorder (homaketree fn a)-}