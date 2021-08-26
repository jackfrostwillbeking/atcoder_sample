x = []
x = gets().chomp.split(' ').map { |n| n.to_i }

exit if !( 1 <= x[0] && x[0] <= 12 && 1 <= x[1] && x[1] <= 12 && x[0] < x[1] )

group_1 = [1,3,5,7,8,10,12]
group_2 = [4,6,9,11]

# puts (group_1 & x).length
puts (group_1 & x).length == 2 || (group_2 & x).length == 2  ? 'Yes' : 'No' 
# print if group_1.include?(%w[x y]) || group_2.include?(%w[x y]) ? 'Yes' : 'No'