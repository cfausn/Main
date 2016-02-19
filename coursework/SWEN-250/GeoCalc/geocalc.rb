# Require (load) the geometric figure classes. Note that the ".rb"
# extension is not required.

require './point'
require './line'
require './rectangle'
require './circle'

# Process each line from standard input as a command.
#
# Commands consist of a lower case letter and four numbers,
# separated by commas:
#
# C,X0,Y0,X1,Y1
#
# where C is the command, X0/Y0 define the first point
# and X1/Y1 define the second point.
#
# Supported commands are:
# l     Create a line from (X0,Y0) to (X1,Y1)
#       Print the line and its length
# r     Create a rectangle whose diagonal corners are (X0,Y0) and (X1,Y1)
#       Print the rectangle, its perimeter and its area
# c     Create a circle whose center if (X0,Y0) and with (X1,Y1) a point on
#       the circle.
#       Print the circle, its circumference, and its area.

$stdin.each do | line; figure, command, x0, y0, x1, y1, p1, p2 |

  command, x0, y0, x1, y1 = line.split(',')

  p1 = Point.new(x0, y0)
  p2 = Point.new(x1, y1)
  puts "Command = #{command} points = #{p1} and #{p2}"

  case command
  when 'l'
    figure = Line.new(p1, p2)
    puts figure
    puts "Length: #{figure.length}"
  when 'r'
    figure = Rectangle.new(p1, p2)
    puts figure
    puts "Height: #{figure.height}"
    puts "Width: #{figure.width}"
    puts "Perimeter: #{figure.perimeter}"
    puts "Area: #{figure.area}"
  when 'c'
    figure = Circle.new(p1, p2)
    puts figure
    puts "Diameter: #{figure.diameter}"
    puts "Circumference: #{figure.circumference}"
    puts "Area: #{figure.area}"
  else
    puts "Unknown command"
  end
end
