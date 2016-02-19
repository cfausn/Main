# Rectangles are defined by to diagonal corner Points.
# Rectangles are immutable - once constructed the corner
# points cannot be changed.

require './point'

class Rectangle
  # Methods below are private.
  private

  # Initialize the Rectangle corner points from those
  # provided to Rectangle.new.
  # The instance variables are @c1 and @c2
  def initialize(c1 = Point.new, c2 = Point.new)
## TO BE FILLED IN BY STUDENT
    @c1 = c1
    @c2 = c2
  end

  # Methods below are public
  public

  # Allow read access to the two corner points.
  attr_reader :c1, :c2

  # Return the width of the rectangle (absolute value of difference between
  # the corner X coordinates).
  # You must define the method named 'width' in its entirety. Use the code in
  # line.rb and circle.rb as templates for creating such a method.
## TO BE FILLED IN BY STUDENT
  def width
    return (@c1.x - @c2.x).abs
  end

  # Return the height of the rectangle (absolute value of difference between
  # the corner Y coordinates).
  # You must define the method named 'height' in its entirety. Use the code in
  # line.rb and circle.rb as templates for creating such a method.
## TO BE FILLED IN BY STUDENT
  def height
    return (@c1.y - @c2.y).abs
  end
  # Return the perimeter of the rectangle.
  # You must define the method named 'perimeter' in its entirety.
  # This *MUST* be written using the width and height methods
## TO BE FILLED IN BY STUDENT
  def perimeter
    return ((2 * width) + (2 * height))
  end
  # Return the area of the rectangle
  # You must define the method named 'area' in its entirety.
  # This *MUST* be written using the width and height methods
## TO BE FILLED IN BY STUDENT
  def area
    return height * width
  end

  def to_s
    "Rectangle corners #{c1} and #{c2}"
  end
end
