data AVLTree t = Empty | Root t (AVLTree t) (AVLTree t) deriving (Eq, Ord, Show)

leaf x = Root x Empty Empty

myTree1 = Root 5 (Root 1 (Empty) (leaf 3)) (leaf 7)

addnode :: Ord a => a -> AVLTree a -> AVLTree a
addnode a Empty = leaf a
addnode a (Root x left right)
    | a > x = Root x left (addnode a right)
    | otherwise = Root x (addnode a left) right

maketree :: Ord a => [a] -> AVLTree a
maketree [] = Empty
maketree (a:as) = addnode a (maketree as)

tree1 = Root 3 (Root 2 (Root 1 Empty Empty) Empty) (Root 7 (Root 4 Empty (Root 5 Empty (Root 6 Empty Empty))) Empty)

height :: (Ord a, Num a) => AVLTree a -> a
height Empty = -1
height (Root k l r) = 1 + (max (height l) (height r))

left :: AVLTree a -> AVLTree a
left Empty = Empty
left (Root n l r) = l

right :: AVLTree a -> AVLTree a
right Empty = Empty
right (Root n l r) = r

value :: (Ord a, Num a) => AVLTree a -> a
value Empty = 0
value (Root n l r) = n


ins :: (Num a, Ord a) => AVLTree a -> a -> AVLTree a
ins Empty a =  (Root a Empty Empty)
ins (Root b l r) k
    | b < k = rotate ((Root b l (ins r k)))
    | otherwise = rotate (Root b (ins l k) r)

rotate :: (Ord a, Num a) => AVLTree a -> AVLTree a
rotate Empty = Empty
rotate (Root n l r)
    | not (abs ((height l) - (height r)) > 1) = Root n (rotate l) r
    | not (abs ((height r) - (height l)) > 1) = Root n l (rotate r)
    | (height l) + 1 < (height r) && (height (left r))  < (height (right r)) = Root (value r) (Root n l (left r)) (right r)
    | (height r) + 1 < (height l) &&  (height (right l))  < (height (left l)) = Root (value l) (left l) (Root n (right l) r)
    | (height l) + 1 < (height r) && (height (left r))  > (height (right r)) = Root (value (left r)) (Root n l (left (left r))) (Root (value r) (right (left r)) (right r))
    | (height r) + 1 < (height l) && (height (right l))  > (height (left l)) = Root (value (right l)) (Root (value l) (left l) (left (right l))) (Root n (right (right l)) r)
    | otherwise = Root n l r

balanced :: (Ord a, Num a) => AVLTree a -> AVLTree a
balanced Empty = Empty
balanced (Root k l r)
    | not (abs ((height l) - (height r)) > 1) = rotate (Root k l r)
    | not (abs ((height r) - (height l)) > 1) = rotate (Root k l r)
    | otherwise = (Root k l r)

buildTree :: (Num a, Ord a) => [a] -> AVLTree a
buildTree [] = Empty
buildTree (x:xs) = foldl ins Empty (x:xs)