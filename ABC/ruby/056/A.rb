a,b = gets().chomp.split(' ')

exit if !( a == 'D' || a == 'H' )
exit if !( b == 'D' || b == 'H' )

puts ( a == 'H' && b == 'H' ) || ( a == 'D' && b == 'D' ) ? 'H' : 'D'
