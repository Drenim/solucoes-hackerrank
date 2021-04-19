import Control.Monad

triangle h w
  | h == 1 = [buildOnes (onesAmmount 1)]
  | otherwise = triangle (h - 1) w ++ [buildOnes (onesAmmount h)]
  where
    onesAmmount i = 2 * i - 1
    buildOnes size = concat (replicate size "1")

buildUnderlines x w = concat (replicate (div (w - length x) 2) "_")

fill t w =
  map
    ( \x ->
        let underlines = buildUnderlines x w
         in underlines ++ x ++ underlines
    )
    t

combine t1 t2 w1 w2 = t1' ++ merge t2' t2'
  where
    t1' = fill t1 w1
    t2' = fill t2 w2
    merge t1 t2 = zipWith concatSep t1 t2
      where
        concatSep line1 line2 =
          if even (length line1 + length line2)
            then line1 ++ "_" ++ line2
            else line1 ++ line2

sierpinski h w i
  | i == 0 = fill (triangle h w) w
  | otherwise =
    let subproblem = sierpinski (div h 2) (div w 2) (i - 1)
     in combine subproblem subproblem w (div w 2)

main = do
  let height = 32
  let width = 63
  n <- readLn :: IO Int
  putStrLn (unlines (sierpinski height width n))