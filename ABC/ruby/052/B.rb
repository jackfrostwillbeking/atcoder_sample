N = gets().to_i
S = gets().chomp

exit if !( 1 <= N && N <= 100)
exit if !( S.size == N)
exit if !( S.count('I')+S.count('D') == N )

count = 0
res = 0
S.each_char { |s|
  count += (s == 'I') ? 1 : -1
  res = count if count > res
}
puts res
