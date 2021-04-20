import Control.Monad

permute [] = []
permute (x : xs) = [head xs, x] ++ permute (tail xs)

main = do
  t <- readLn :: IO Int
  forM_
    [1 .. t]
    ( \_ -> do
        line <- getLine
        putStrLn (permute line)
    )