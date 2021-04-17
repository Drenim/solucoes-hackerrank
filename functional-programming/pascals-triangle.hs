import Control.Monad

stifel n k
  | n < 0 = 0
  | k < 0 = 0
  | n == 0 && k == 0 = 1
  | otherwise = stifel (n - 1) (k - 1) + stifel (n - 1) k

pascal 0 = [[1]]
pascal k = pascal (k - 1) ++ [map (stifel k) [0 .. k]]

listToString lst = concatMap (\(i, x) -> if i /= 0 then ' ' : show x else show x) (zip [0 ..] lst)

main = do
  n <- readLn :: IO Int
  let triangle = concatMap (\x -> listToString x ++ "\n") (pascal (n - 1))
  putStr triangle