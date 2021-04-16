import Text.Printf (printf)

-- This function should return a list [area, volume].
--solve :: Int -> Int -> [Int] -> [Int] -> [Double]
solve l r a b = [area, volume]
  where
    func = poli a b
    area = integrate func l r
    volume = calcVol func l r

poli :: [Double] -> [Double] -> Double -> Double
poli a b x = sum [a' * x ** b' | (a', b') <- zip a b]

integrate func l r = sum [func (c i) * delta | i <- [1 .. n]]
  where
    delta = 0.001
    n = (r - l) / delta
    c i = l + delta * i

calcVol func l r = sum [pi * func (c i) ^ 2 * delta | i <- [1 .. n]]
  where
    delta = 0.001
    n = (r - l) / delta
    c i = l + delta * i

--Input/Output.
main :: IO ()
main = getContents >>= mapM_ (printf "%.1f\n") . (\[a, b, [l, r]] -> solve l r a b) . map (map read . words) . lines