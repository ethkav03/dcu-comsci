-- Definition of a 2-3 Tree data type
data Tree23 a
  = Empty
  | TwoNode a (Tree23 a) (Tree23 a)
  | ThreeNode a a (Tree23 a) (Tree23 a) (Tree23 a)
  deriving (Eq, Ord, Show)

-- Sample 2-Node and 3-Node trees for testing
my2Tree = TwoNode 6 Empty Empty
my3Tree = ThreeNode 3 10 Empty (TwoNode 6 Empty Empty) (ThreeNode 15 20 Empty (TwoNode 18 Empty Empty) Empty)
my4tree = add 4 (add 19 my3Tree)

-- Function to add an element to a 2-3 Tree
add :: (Ord a) => a -> Tree23 a -> Tree23 a
add x Empty = TwoNode x Empty Empty
add x (TwoNode y left right)
  | x <= y = ThreeNode x y Empty Empty right  -- Add element to the left of a 2-Node
  | otherwise = ThreeNode y x Empty Empty right  -- Add element to the right of a 2-Node
add x (ThreeNode y z left middle right)
  | x <= y = ThreeNode y z (add x left) middle right  -- Add element to the left subtree of a 3-Node
  | x > z = ThreeNode y z left middle (add x right)  -- Add element to the right subtree of a 3-Node
  | otherwise = ThreeNode y z left (add x middle) right  -- Add element to the middle subtree of a 3-Node

-- Function to check if an element is in the 2-3 Tree
member :: (Ord a) => a -> Tree23 a -> Bool
member _ Empty = False
member x (TwoNode y left right)
  | x == y = True  -- Element found in a 2-Node
  | x < y = member x left  -- Recursively search left subtree
  | otherwise = member x right  -- Recursively search right subtree
member x (ThreeNode y z left middle right)
  | x == y || x == z = True  -- Element found in a 3-Node
  | x < y = member x left  -- Recursively search left subtree
  | x <= z = member x middle  -- Recursively search middle subtree
  | otherwise = member x right  -- Recursively search right subtree

-- Function to calculate the height of the 2-3 Tree
height :: Tree23 a -> Int
height Empty = 0
height (TwoNode _ left right) = 1 + max (height left) (height right)  -- Height of a 2-Node
height (ThreeNode _ _ left middle right) = 1 + max (height left) (max (height middle) (height right))  -- Height of a 3-Node

-- Helper function to print the 2-3 Tree vertically
prettyPrintVertical :: (Show a) => Tree23 a -> String
prettyPrintVertical tree = unlines $ reverse $ prettyPrintLines tree ""
  where
    prettyPrintLines Empty indent = [indent ++ "nil"]  -- Display 'nil' for an empty subtree
    prettyPrintLines (TwoNode x left right) indent =
      prettyPrintLines right (indent ++ "             ") ++  -- Recursively print right subtree
      [indent ++ show x] ++  -- Display the value of the root node
      prettyPrintLines left (indent ++ "             ")  -- Recursively print left subtree
    prettyPrintLines (ThreeNode x y left middle right) indent =
      prettyPrintLines right (indent ++ "             ") ++  -- Recursively print right subtree
      [indent ++ show x ++ "," ++ show y] ++  -- Display values of the root node
      prettyPrintLines middle (indent ++ "             ") ++  -- Recursively print middle subtree
      prettyPrintLines left (indent ++ "             ")  -- Recursively print left subtree

-- Function to print the 2-3 Tree in a nice format
prettyPrint :: (Show a) => Tree23 a -> IO()
prettyPrint a = do
  putStrLn $ prettyPrintVertical a
