A,B,C = gets().chomp.split(' ')
ALEN = A.length
BLEN = B.length
CLEN = C.length

exit if !( 1 <= ALEN && ALEN <= 10 && 1 <= BLEN && BLEN <= 10 && 1 <= CLEN && CLEN <= 10 )
exit if !( /[[:lower:]]/.match(A) && /[[:lower:]]/.match(B) && /[[:lower:]]/.match(C) )

puts A[-1] == B[0] && B[-1] == C[0] ? 'YES' : 'NO'