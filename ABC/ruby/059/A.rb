S1,S2,S3 = gets().chomp.split(' ')

exit if !( /[[:lower:]]/.match(S1) && /[[:lower:]]/.match(S2) && /[[:lower:]]/.match(S3))
exit if !( 1 <= S1.length && S1.length <= 10 && 1 <= S2.length && S2.length <= 10 && 1 <= S3.length && S3.length <= 10)

puts S1[0].upcase+S2[0].upcase+S3[0].upcase