data Bintree t = Empty | Root t (Bintree t) (Bintree t) deriving (Ord, Eq, Show)
leaf x = Root x Empty Empty