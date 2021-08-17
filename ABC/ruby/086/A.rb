array_input=gets.split(' ')
a=array_input[0].to_i
b=array_input[1].to_i

exit() if array_input.length >= 3
exit() if !(1 <= a) | !(a <= 10000)
exit() if !(1 <= b) | !(b <= 10000)

puts (a*b)%2 == 0 ? "Even" : "Odd"
