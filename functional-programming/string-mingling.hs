import Control.Monad

mingling [] [] = []
mingling (x : xs) (y : ys) = [x, y] ++ mingling xs ys

main = do
  p <- getLine
  q <- getLine
  putStrLn (mingling p q)