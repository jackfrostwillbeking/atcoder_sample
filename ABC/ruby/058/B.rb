O = gets().chomp.split('')
E = gets().chomp.split('')

exit if !( 1 <= O.length && O.length <= 50 &&  1 <= E.length && E.length <= 50 )
length = O.length - E.length
exit if !( 0 <= length || length <= 1 )
O.map { |o| exit if !(o =~ /^[a-z]*$/)  }
E.map { |e| exit if !(e =~ /^[a-z]*$/)  }

E.length.times { |n|
    print O[n]
    print E[n]
 }
if length == 1
    print O[-1]
end