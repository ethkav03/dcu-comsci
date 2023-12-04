q1 = [(x * 3) | x <- [1..33], odd x]

q2 = 10 `mod` 3 == 1

evalInts :: Int -> Int -> Int
evalInts a b
    | odd a || odd b = a + b
    | otherwise = a - b

myUnion :: (Eq a) => [a] -> [a] -> [a]
myUnion a [] = a
myUnion a (b:bs)
    | elem b a = myUnion a bs
    | otherwise = myUnion (a ++ [b]) bs

data BinTree t = Empty | Root t (BinTree t) (BinTree t) deriving (Eq, Ord, Show)

myTree1 = Root 1 (Root 2 (Root 4 Empty Empty) (Root 5 Empty Empty)) (Root 3 (Root 6 Empty Empty) (Root 7 Empty Empty))

preorder :: BinTree a -> [a]
preorder Empty = []
preorder (Root x left right) = [x] ++ preorder left ++ preorder right

inorder :: BinTree a -> [a]
inorder Empty = []
inorder (Root x left right) = inorder left ++ [x] ++ inorder right

postorder :: BinTree a -> [a]
postorder Empty = []
postorder (Root x left right) = postorder left ++ postorder right ++ [x]